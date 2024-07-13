import requests
from .base import Base

class Meli(Base):
    def __init__(self, url: str):
        super().__init__(f"{url}/meli")

    def update(self, params: dict) -> dict:
        response = requests.put(self.url, json=params, headers=self.headers)
        payload = response.json()
        if not response.ok:
            raise Exception(payload)
        return payload

    def find_one(self, params: dict) -> dict:
        response = requests.get(self.convert(params), headers=self.headers)
        payload = response.json()
        if not response.ok:
            raise Exception(payload)
        return payload