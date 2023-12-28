import g4f
import json
from fastapi import FastAPI, Header, Body
from typing import Annotated


app = FastAPI()

#Handling Errors
def error_handler(e:Exception):
    return {"error":str(e)}
#Models endpoints

#GPT 3.5
@app.post('/chatbase')
def cbase(messages :list = Body(...)):
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages #[{"role": "user", "content": prompt}]
        )
        return response
    except Exception as e:
        return error_handler(e)

@app.post('/llama2')
def llama2(messages :list = Body(...)):
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=messages, #[{"role": "user", "content": prompt}]
            provider=g4f.Provider.Llama2
        )
        return response
    except Exception as e:
        return error_handler(e)
#GPT 4 
@app.post('/bingChat')
def bingGPT4(messages :list = Body(...)):
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=messages, #[{"role": "user", "content": prompt}]
            provider=g4f.Provider.Bing
        )
        return response
    except Exception as e:
        return error_handler(e)

@app.post('/bardChat')
def bardGPT4(messages :list = Body(...)):
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=messages, #[{"role": "user", "content": prompt}]
            provider=g4f.Provider.Bard
        )
        return response
    except Exception as e:
        return error_handler(e)

@app.post('/geekGPT')
def geekGPT(messages :list = Body(...)):
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=messages, #[{"role": "user", "content": prompt}]
            provider=g4f.Provider.GeekGpt
        )
        return response
    except Exception as e:
        return error_handler(e)

@app.post('/liaobots')
def liaobots(messages :list = Body(...)):
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=messages, #[{"role": "user", "content": prompt}]
            provider=g4f.Provider.Liaobots
        )
        return response
    except Exception as e:
        return error_handler(e)



#Other LLMs
@app.post('/davinci3')
def davinci3(messages :list = Body(...)):
    response = g4f.ChatCompletion.create(
        model="text-davinci-003",
        messages=messages, #[{"role": "user", "content": prompt}]
    )
    return response

@app.post('/davinci2')
def davinci2(data :list = Body(...)):
    messages = data[0]
    response = g4f.ChatCompletion.create(
        model="text-davinci-002",
        messages=messages, #[{"role": "user", "content": prompt}]
    )
    return response

@app.post('/curie')
def curie(messages :list = Body(...)):
    response = g4f.ChatCompletion.create(
        model="text-curie-001",
        messages=messages, #[{"role": "user", "content": prompt}]
    )
    return response

@app.post('/code-davinci2')
def davinciCode(messages :list = Body(...)):
    response = g4f.ChatCompletion.create(
        model="code-davinci-002",
        messages=messages, #[{"role": "user", "content": prompt}]
    )
    return response


@app.post('/ada')
def ada(messages :list = Body(...)):
    response = g4f.ChatCompletion.create(
        model="text-ada-001",
        messages=messages, #[{"role": "user", "content": prompt}]
    )
    return response

@app.post('/babbage')
def babbage(messages :list = Body(...)):
    response = g4f.ChatCompletion.create(
        model="text-babbage-001",
        messages=messages, #[{"role": "user", "content": prompt}]
    )
    return response


@app.post('/FakeGPT')
def geekGPT(messages :list = Body(...)):
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=messages, #[{"role": "user", "content": prompt}]
            provider=g4f.Provider.FakeGpt
        )
        return response
    except Exception as e:
        return error_handler(e)
    
@app.post('/GptGo')
def geekGPT(messages :list = Body(...)):
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=messages, #[{"role": "user", "content": prompt}]
            provider=g4f.Provider.GptGo
        )
        return response
    except Exception as e:
        return error_handler(e)
    
@app.post('/koala')
def geekGPT(messages :list = Body(...)):
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=messages, #[{"role": "user", "content": prompt}]
            provider=g4f.Provider.Koala
        )
        return response
    except Exception as e:
        return error_handler(e)
    
@app.post('/YouAi')
def geekGPT(messages :list = Body(...)):
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=messages, #[{"role": "user", "content": prompt}]
            provider=g4f.Provider.You
        )
        return response
    except Exception as e:
        return error_handler(e)

@app.post('/AiAssistant')
def geekGPT(messages :list = Body(...)):
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=messages, #[{"role": "user", "content": prompt}]
            provider=g4f.Provider.AiChatOnline
        )
        return response
    except Exception as e:
        return error_handler(e)

@app.post('/Aura')
def aura(messages :list = Body(...)):
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=messages, #[{"role": "user", "content": prompt}]
            provider=g4f.Provider.Aura
        )
        return response
    except Exception as e:
        return error_handler(e)
    
@app.post('/Phind')
def aura(messages :list = Body(...)):
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=messages, #[{"role": "user", "content": prompt}]
            provider=g4f.Provider.Phind
        )
        return response
    except Exception as e:
        return error_handler(e)
    
@app.post('/Gpt6')
def aura(messages :list = Body(...)):
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=messages, #[{"role": "user", "content": prompt}]
            provider=g4f.Provider.Gpt6
        )
        return response
    except Exception as e:
        return error_handler(e)