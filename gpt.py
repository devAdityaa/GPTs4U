import g4f
import json
from fastapi import FastAPI, Header, Body
from typing import Annotated


app = FastAPI()

#Models endpoints
@app.post('/gpt-3.5-turbo')
def gptResponse(data :list = Body(...)):
    print(type(data[1]))
    messages = data[0]
    temparature = data[1]
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages, #[{"role": "user", "content": prompt}]
        top_p=4
    )
    return response

@app.post('/davinci3')
def bingGPT4(messages :list = Body(...)):
    response = g4f.ChatCompletion.create(
        model="text-davinci-003",
        messages=messages, #[{"role": "user", "content": prompt}]
    )
    return response

@app.post('/davinci2')
def bingGPT4(messages :list = Body(...)):
    response = g4f.ChatCompletion.create(
        model="text-davinci-002",
        messages=messages, #[{"role": "user", "content": prompt}]
    )
    return response

@app.post('/curie')
def bingGPT4(messages :list = Body(...)):
    response = g4f.ChatCompletion.create(
        model="text-curie-001",
        messages=messages, #[{"role": "user", "content": prompt}]
    )
    return response

@app.post('/code-davinci2')
def bingGPT4(messages :list = Body(...)):
    response = g4f.ChatCompletion.create(
        model="code-davinci-002",
        messages=messages, #[{"role": "user", "content": prompt}]
    )
    return response


@app.post('/ada')
def bingGPT4(messages :list = Body(...)):
    response = g4f.ChatCompletion.create(
        model="text-ada-001",
        messages=messages, #[{"role": "user", "content": prompt}]
    )
    return response

@app.post('/babbage')
def bingGPT4(messages :list = Body(...)):
    response = g4f.ChatCompletion.create(
        model="text-babbage-001",
        messages=messages, #[{"role": "user", "content": prompt}]
    )
    return response