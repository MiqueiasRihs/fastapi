from fastapi import FastAPI
import redis

app = FastAPI()

# Crie uma conexão com o Redis
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.post("/set/{key}/{value}")
async def set_value(key: str, value: str):

    redis_client.hmset("meu_hash", {"nome": "João", "idade": 30, "cidade": "Exemplo"})
    redis_client.set(key, value)
    
    return {"message": "Valor definido com sucesso"}


@app.get("/get/{key}")
async def get_value(key: str):
    
    value = redis_client.get(key)
    name = redis_client.hget("meu_hash", "nome")
    
    if not value:
        return {"message": "Chave não encontrada"}
    
    return {"key": key, "value": value.decode("utf-8"), "name": name}
