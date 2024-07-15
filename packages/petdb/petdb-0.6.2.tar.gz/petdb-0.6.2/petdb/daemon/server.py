
import sys

import uvicorn
from fastapi import FastAPI, Request, Response, status, Body
from passlib.context import CryptContext

from petdb import PetDB
from petdb.daemon.qlock import QLock

if sys.platform != "linux":
	raise Exception("PetDB.daemon supports only Linux system")

STORAGE_PATH = "/var/lib/petdb"

db = PetDB.get(STORAGE_PATH)
app = FastAPI()
crypt = CryptContext(schemes=["pbkdf2_sha256"], default="pbkdf2_sha256")
lock = QLock()

@app.post("/collections")
def get_collections():
	with lock:
		return db.collections()

@app.post("/drop")
def drop_collections():
	with lock:
		db.drop()

@app.post("/reload")
def drop_collections():
	with lock:
		db.reload()

@app.post("/drop/{name}")
def drop_collection(name: str):
	with lock:
		db.drop_collection(name)

@app.post("/get/{name}")
def get_collection(name: str):
	with lock:
		return db.collection(name).list()

@app.post("/set/{name}")
def set_collection(name: str, data: list = Body(embed=True)):
	with lock:
		db.collection(name).replace(data)

def run(port: int = 3944, password_hash: str = ""):

	@app.middleware("http")
	async def authentication(request: Request, call_next):
		body = await request.json()
		if crypt.verify(body["password"], password_hash):
			return await call_next(request)
		return Response(status_code=status.HTTP_401_UNAUTHORIZED)

	uvicorn.run(app, host="127.0.0.1", port=port)
