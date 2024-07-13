import requests
from .base import Base

class Template(Base):
    def __init__(self, url: str):
        super().__init__(f"{url}/template")

    def view(self, params: dict = None) -> list:
        response = requests.get(self.convert(params), headers=self.headers)
        payload = response.json()
        if not response.ok:
            raise Exception(payload)
        return payload

    def create(self, params: dict) -> dict:
        response = requests.post(self.url, json=params, headers=self.headers)
        payload = response.json()
        if not response.ok:
            raise Exception(payload)
        return payload

    def update(self, params: dict) -> str:
        response = requests.put(self.url, json=params, headers=self.headers)
        payload = response.text
        if not response.ok:
            raise Exception(payload)
        return payload

    def delete(self, params: dict) -> str:
        response = requests.delete(self.convert(params), headers=self.headers)
        payload = response.text
        if not response.ok:
            raise Exception(payload)
        return payload

    def find_one(self, params: dict) -> dict:
        response = requests.get(self.convert(params), headers=self.headers)
        payload = response.json()
        if not response.ok:
            raise Exception(payload)
        return payload