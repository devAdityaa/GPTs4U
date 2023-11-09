import g4f
import json
from fastapi import FastAPI, Header, Body
from typing import Annotated


app = FastAPI()

#Models endpoints

#GPT 3.5
@app.post('/gpt-3.5-turbo')
def gptTurbo(data :list = Body(...)):
    messages = data[0]
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages #[{"role": "user", "content": prompt}]
    )
    return response


#GPT 4 
@app.post('/bingChat')
def bingGPT4(data :list = Body(...)):
    messages = data[0]
    response = g4f.ChatCompletion.create(
        model=g4f.models.default,
        messages=messages, #[{"role": "user", "content": prompt}]
        provider=g4f.Provider.Bing
    )
    return response

@app.post('/bardChat')
def bardGPT4(data :list = Body(...)):
    messages = data[0]
    response = g4f.ChatCompletion.create(
        model=g4f.models.default,
        messages=messages, #[{"role": "user", "content": prompt}]
        provider=g4f.Provider.Bard
    )
    return response

@app.post('/geekGPT')
def geekGPT(data :list = Body(...)):
    messages = data[0]
    response = g4f.ChatCompletion.create(
        model=g4f.models.default,
        messages=messages, #[{"role": "user", "content": prompt}]
        provider=g4f.Provider.GeekGpt
    )
    return response

@app.post('/liaobots')
def liaobots(data :list = Body(...)):
    messages = data[0]
    response = g4f.ChatCompletion.create(
        model=g4f.models.default,
        messages=messages, #[{"role": "user", "content": prompt}]
        provider=g4f.Provider.Liaobots
    )
    return response

@app.post('/phind')
def liaobots(data :list = Body(...)):
    messages = data[0]
    response = g4f.ChatCompletion.create(
        model=g4f.models.default,
        messages=messages, #[{"role": "user", "content": prompt}]
        provider=g4f.Provider.Phind
    )
    return response

#Other LLMs
@app.post('/davinci3')
def davinci3(data :list = Body(...)):
    messages = data[0]
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
def curie(data :list = Body(...)):
    messages = data[0]
    response = g4f.ChatCompletion.create(
        model="text-curie-001",
        messages=messages, #[{"role": "user", "content": prompt}]
    )
    return response

@app.post('/code-davinci2')
def davinciCode(data :list = Body(...)):
    messages = body[0]
    response = g4f.ChatCompletion.create(
        model="code-davinci-002",
        messages=messages, #[{"role": "user", "content": prompt}]
    )
    return response


@app.post('/ada')
def ada(data :list = Body(...)):
    messages = data[0]
    response = g4f.ChatCompletion.create(
        model="text-ada-001",
        messages=messages, #[{"role": "user", "content": prompt}]
    )
    return response

@app.post('/babbage')
def babbage(data :list = Body(...)):
    messages = data[0]
    response = g4f.ChatCompletion.create(
        model="text-babbage-001",
        messages=messages, #[{"role": "user", "content": prompt}]
    )
    return response
