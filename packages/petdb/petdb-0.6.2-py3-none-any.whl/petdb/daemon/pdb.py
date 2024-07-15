
from typing import Any
import requests

class PetDB:

	def __init__(self, password: str, port: int = 8080):
		self.password = password
		self.port = port

	def __get_collection(self, name: str) -> list:
		return self.__request(f"get/{name}")

	def __set_collection(self, name: str, data: list):
		self.__request(f"set/{name}", {"data": data})

	def __request(self, endpoint: str, body: dict = None) -> Any:
		if body is None:
			body = {}
		body["password"] = self.password
		return requests.post(f"http://127.0.0.1:{self.port}/{endpoint}", json=body).json()
