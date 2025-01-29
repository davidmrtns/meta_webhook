import os

from fastapi import FastAPI, Query

from LeadGenSchema import LeadGenSchema

app = FastAPI()
chave = os.getenv("CHAVE_SECRETA")


@app.get("/meta_webhook")
async def root(
    hub_mode: str = Query(..., alias="hub.mode"),
    hub_challenge: int = Query(..., alias="hub.challenge"),
    hub_verify_token: str = Query(..., alias="hub.verify_token")
):
    if hub_verify_token == chave:
        return hub_challenge
    return None


@app.post("/meta_webhook")
async def root(
    request: LeadGenSchema
):
    print(request.model_dump())
    return {"status": "success"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
