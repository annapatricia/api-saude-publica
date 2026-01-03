from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API Saúde Pública")

# Base simples de documentos médicos
doencas = [
    {
        "id": 1,
        "nome": "Diabetes Mellitus",
        "descricao": "Doença crônica caracterizada por níveis elevados de glicose no sangue.",
        "sintomas": ["sede excessiva", "urinar frequentemente", "fadiga"],
        "tratamento": "Dieta, atividade física, controle glicêmico e uso de medicamentos como insulina."
    },
    {
        "id": 2,
        "nome": "Hipertensão Arterial",
        "descricao": "Elevação persistente e sustentada da pressão arterial.",
        "sintomas": ["dor de cabeça", "tontura", "visão embaçada"],
        "tratamento": "Mudanças no estilo de vida e uso de anti-hipertensivos."
    }
]

# Modelo para cadastro de doença
class Doenca(BaseModel):
    nome: str
    descricao: str
    sintomas: list[str]
    tratamento: str

@app.get("/")
def home():
    return {"mensagem": "Sistema de regulação e consulta médica"}

@app.get("/doencas")
def listar_doencas():
    return doencas

@app.get("/doencas/{nome_doenca}")
def buscar_doenca(nome_doenca: str):
    for d in doencas:
        if nome_doenca.lower() in d["nome"].lower():
            return d
    return {"erro": "Doença não encontrada"}

# 🔹 Novo endpoint: cadastrar doença
@app.post("/doencas")
def cadastrar_doenca(doenca: Doenca):
    novo_id = max(d["id"] for d in doencas) + 1 if doencas else 1
    nova_doenca = doenca.dict()
    nova_doenca["id"] = novo_id
    doencas.append(nova_doenca)
    return {"mensagem": "Doença cadastrada com sucesso!", "doenca": nova_doenca}
