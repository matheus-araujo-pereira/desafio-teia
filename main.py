from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil
import os
from transcribe import transcribe_audio
from generate_pdf import generate_bo_pdf

app = FastAPI()

class BORequest(BaseModel):
    audio_file: UploadFile

@app.post("/generate-bo")
async def generate_bo(audio_file: UploadFile = File(...)):
    # Criar o diretório temp se não existir
    os.makedirs("temp", exist_ok=True)
    
    audio_path = f"temp/{audio_file.filename}"
    with open(audio_path, "wb") as buffer:
        shutil.copyfileobj(audio_file.file, buffer)
    
    # Verificar se o arquivo foi salvo corretamente
    if not os.path.exists(audio_path):
        return {"error": "Erro ao salvar o arquivo de áudio."}
    
    print(f"Arquivo de áudio salvo em: {audio_path}")
    
    # Transcrever o áudio para texto
    transcribed_text = transcribe_audio(audio_path)
    print(f"Texto transcrito: {transcribed_text}")
    
    # Gerar o PDF do Boletim de Ocorrência
    pdf_path = generate_bo_pdf(transcribed_text)
    print(f"PDF gerado em: {pdf_path}")
    
    # Remover o arquivo de áudio temporário
    os.remove(audio_path)
    
    return {"pdf_path": pdf_path}
