from fastapi import FastAPI, HTTPException, File, UploadFile
import os
import uvicorn
import requests
import json

# Import class
# from ollama_test_chatprompt import LocalLLM
# from avatar.avatar_main import run_llm_worker
from knowledgeworkers.workers_main import run_llm_worker
from voiceservice.stt import transcribe_audio
from voiceservice.tts import synthesize_audio
# from streaming_server.test_client import run_audio_2_face
import threading


HOME = os.getcwd()
# print(HOME)
UPLOAD_DIR = os.path.join(HOME, r"voiceservice\audiofile")
# print(UPLOAD_DIR)


app = FastAPI()

# get_model_name = {
#     'llama 3.1' : 'llama3.1:latest',
#     'mistral' : 'mistral:latest',
#     'nemotron' : 'nemotron-mini:latest',
#     'llama3.2-small' :'llama3.2:1b',
#     'gemma2':'gemma2:latest'
# }

# Groq Model
get_model_name = {
    "gpt-4o": "gpt-4o",
    "mistral": "mixtral-8x7b-32768",
    "llama3.1": "llama-3.1-8b-instant",
    "llama3.2_small": "llama-3.2-1b-preview",
    "gemma2": "gemma2-9b-it"
}

@app.get('/')
def greeting():
    return {"message": "Hello from Shubham"}

# Todo: Perform Speech To Text Here
@app.post('/speechtotext')
async def generate_response():
    try:
        test_input = transcribe_audio() # change this to user_input
        print("Transcribed text is: ",test_input)
        
        return {"Audio To Text": test_input}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        

# Generating response from LLM 
@app.post("/generate")
def generate_response(model_name: str, worker_id: str, user_voice:str, user_tone: str, user_input: str):
    try:
        # 2. LLM
        model_name = get_model_name[model_name]

        response = run_llm_worker(model_name, worker_id, user_tone, user_input)
        
        # 3. Text To Speech
        tts_generated = synthesize_audio(user_voice = user_voice, text = response)
        print(tts_generated)
        
        if tts_generated:
            # 4: Audio2Face
            # run_audio_2_face()
            # params = dict(audio_fpath = r"C:\Users\ov-developer\Desktop\AvatarAI\LLMs\LLMCode\streaming_server\out.wav",
            # instance_name =  "/World/audio2face/PlayerStreaming")
            resp = requests.post("http://127.0.0.1:8001/audio2face")
            # data = resp.json
            pass
            
        else:
            print("Not Success: ",tts_generated)
        
        # LLM response to front end
        return {"Response": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))     
        
    
    

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
