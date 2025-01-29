import os
import httpx
import pytz

from fastapi import FastAPI, Query
from datetime import datetime

from LeadGenSchema import LeadGenSchema

app = FastAPI()
chave = os.getenv("CHAVE_SECRETA") # chave secreta de validação do webhook
url_lead = os.getenv("URL_OBTER_LEAD") # URL para obter os dados da lead
system_user_token = os.getenv("SYSTEM_USER_TOKEN") # token usado na requisição para obter os dados da lead


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

    for entry in request.entry:
        for change in entry.changes:
            if change.field == "leadgen":
                lead_data = change.value

                lead_id = lead_data.leadgen_id
                created_time = lead_data.created_time

                fuso_brasilia = pytz.timezone("America/Sao_Paulo")
                created_time = (datetime.utcfromtimestamp(created_time).replace(tzinfo=pytz.utc))
                data_legivel = created_time.astimezone(fuso_brasilia).strftime('%d/%m/%Y %H:%M:%S')

                # Obter dados da lead da API do Facebook
                async with httpx.AsyncClient() as client:
                    response = await client.get(
                        f"{url_lead}/{lead_id}",
                        params={"access_token": system_user_token}
                    )

                if response.status_code == 200:
                    dados_dict = response.json()
                    print("Dados do Lead:", dados_dict)
                    print("Criado em:", data_legivel)

                # Salvar no CRM
                return {"status": "success"}
    return {"status": "error"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
