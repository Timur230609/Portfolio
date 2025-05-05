from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # .env faylini yuklash

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        text = f"📩 Yangi kontakt so‘rovi:\n\n👤 Ism: {name}\n📧 Email: {email}\n📌 Mavzu: {subject}\n📝 Xabar: {message}"

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": text
        }

        requests.post(url, data=payload)

        return JsonResponse({"message": "Xabaringiz yuborildi!"})

    return JsonResponse({"message": "Faqat POST so‘rovi qabul qilinadi."}, status=400)


class ArticleList(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def api_home(request):
    return JsonResponse({"message": "Hello, API!"})


def home_view(request):
    return render(request, 'index.html')
