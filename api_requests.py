import aiohttp
import asyncio
import hashlib
import time
import json
import random

URL_CONST = "http://gateway.marvel.com/v1/public/"
ts = str(int(time.time()))
public_key = "721d0aab910e7f3daa868a730590ed09"
private_key = "2e534c8eddfa7c31dc31a408ae572d856137d649"

hash_1 = hashlib.md5(f"{ts + private_key + public_key}".encode())

hash_result = hash_1.hexdigest()


def letra_inicial():
    abc = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    letra_elegida = random.choice(abc)
    return letra_elegida


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text


async def get_data():
    url = f"{URL_CONST}characters?ts={ts}&apikey={public_key}&hash={hash_result}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    print(f"Data retrived successfully: {data}")
                    return data
    except Exception as e:
        return f"Error{e}"


async def obtener_personajes():
    url = f"{URL_CONST}characters?nameStartsWith={letra_inicial()}&limit={9}&ts={ts}&apikey={public_key}&hash={hash_result}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data
    except Exception as e:
        return f"Error{e}"


async def buscar(starts, numero_personaje=3):
    url = f"{URL_CONST}characters?nameStartsWith={starts}&limit={numero_personaje}&ts={ts}&apikey={public_key}&hash={hash_result}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    data = data['data']['results']
                    return data
    except Exception as e:
        return  f"Error{e}"


async def personaje_id(id):
    url = f"{URL_CONST}characters/{id}?&ts={ts}&apikey={public_key}&hash={hash_result}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    data = data['data']['results']
                    return data
    except Exception as e:
        return  f"Error{e}"