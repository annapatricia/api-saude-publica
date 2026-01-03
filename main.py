from fastapi import FastAPI

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

@app.get("/")
def home():
    return {"mensagem": "Sistema de regulação e consulta médica"}

# 🔹 Listar todas as doenças
@app.get("/doencas")
def listar_doencas():
    return doencas

# 🔹 Buscar doença pelo nome
@app.get("/doencas/{nome_doenca}")
def buscar_doenca(nome_doenca: str):
    for d in doencas:
        if nome_doenca.lower() in d["nome"].lower():
            return d
    return {"erro": "Doença não encontrada"}
