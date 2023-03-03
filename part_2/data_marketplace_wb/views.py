from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
import aiohttp
import asyncio
from pydantic import BaseModel
import json


class wb_item(BaseModel):
    id: int
    brand: str
    name: str


async def aiohttp_request(article: str):
    async with aiohttp.ClientSession() as session:
        data = {}
        url = f"https://card.wb.ru/cards/detail?nm={article}"
        async with session.get(url) as response:
            print("Status:", response.status)
            data = await response.text()
    return data


class wb_data_apiview(APIView):
    def get(self, request, article):
    
        data = json.loads(asyncio.run(aiohttp_request(str(article))))
    
        if len(data["data"]["products"]) >0:
            wb_card = wb_item(**data["data"]["products"][0])
            return Response({"data": wb_card.dict()})
        return Response({"data":"article not found"})
    

def index_page(request):
    
    return render(request, 'data_marketplace_wb/index.html')


def set_articles_page(request):
    if request.POST:
        return redirect(f'api/wb_data/{request.POST["article"]}?format=json') 
    
    return render(request, 'data_marketplace_wb/wb_set_articles.html')

    
