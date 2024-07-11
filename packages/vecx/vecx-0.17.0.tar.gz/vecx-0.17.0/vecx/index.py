import requests, json
from .libvx import encode, decode
from .vectorx import VectorX
from .crypto import encrypt_ecb, decrypt_ecb
from .exceptions import raise_exception

class Index:
    def __init__(self, name:str, key:str, vx:VectorX):
        self.name = name
        self.key = key
        self.vx = vx

    def __str__(self):
        return self.name

    def upsert(self, vectors):
        if len(vectors) > 1000:
            raise ValueError("Cannot insert more than 1000 vectors at a time")
        checksum = self.vx.checksum(self.key)
        for vector in vectors:
            vector["vector"] = encode(self.key, vector["vector"])
            vector["meta"] = encrypt_ecb(self.key, json.dumps(vector["meta"]))

        headers = {
            'Authorization': f'{self.vx.token}',
            'Content-Type': 'application/json'
        }
        data = {
            'checksum': checksum,
            'vectors': vectors,
        }
        response = requests.post(f'{self.vx.base_url}/vector/{self.name}/upsert', headers=headers, json=data)
        print(response.text)
        if response.status_code != 200:
            raise_exception(response.status_code)
        return "Vectors inserted successfully"

    def query(self, vector, top_k=10, include_vectors=False, log=False):
        checksum = self.vx.checksum(self.key)
        vector = encode(self.key, vector)
        headers = {
            'Authorization': f'{self.vx.token}',
            'Content-Type': 'application/json'
        }
        data = {
            'checksum': checksum,
            'vector': vector,
            'top_k': top_k,
        }
        response = requests.post(f'{self.vx.base_url}/vector/{self.name}/query', headers=headers, json=data)
        if response.status_code != 200:
            raise_exception(response.status_code)
        if log == True:
            print(response.text)
        results = response.json()
        round_off = True
        for result in results:
            if include_vectors:
                result["vector"] = decode(self.key, result["vector"])
                if round_off:
                    result["vector"] = [round(x, 6) for x in result["vector"]]
            else:
                # Delete vector from result
                del result["vector"]
            result["meta"] = json.loads(decrypt_ecb(self.key, result["meta"]))
        return results

    def delete(self, id):
        checksum = self.vx.checksum(self.key)
        headers = {
            'Authorization': f'{self.vx.token}',
            }
        response = requests.get(f'{self.vx.base_url}/vector/{self.name}/delete/{id}', headers=headers)
        if response.status_code != 200:
            raise_exception(response.status_code)
        return f'Vector {id} deleted successfully'
