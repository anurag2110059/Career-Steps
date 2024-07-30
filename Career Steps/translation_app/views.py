from django.shortcuts import render,redirect
from googletrans import Translator
from django.utils.translation import activate
from .forms import TextForm
from .utils import analyze_text
from django.http import HttpResponse
import subprocess
import pandas as pd
from django.contrib.auth import authenticate, login
from django.urls import reverse

def my_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
       
        # 


def index(request):
   return render(request,'translation_app/index.html')
def predictor(request):
   return render(request,'translation_app/predictor.html')
def chatbot(request):
   return render(request,'translation_app/chatbot.html')
def courses(request):
   return render(request,'translation_app/courses.html')
def team(request):
   return render(request,'translation_app/team.html')
def testimonial(request):
   return render(request,'translation_app/testimonial.html')
def four(request):
   return render(request,'translation_app/404.html')
def future(request):
   return render(request,'translation_app/future.html')
def doctor(request):
   return render(request,'translation_app/doctor.html')
def engineer(request):
   return render(request,'translation_app/Engineering.html')
def sports(request):
   return render(request,'translation_app/sports.html')
def connect(request):
   return render(request,'translation_app/index.html')
def courses(request):
   return render(request,'translation_app/courses.html')
def login(request):
   return render(request,'translation_app/login.html')

def activate_voice_assistant(request):
    subprocess.Popen(['python', r'D:\multi\language_translation\translation_app\assistant.py'])
    return HttpResponse('Voice assistant activated!')


def predict_career(request):
    predicted_career = None
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text_message = form.cleaned_data['text_message']
            predicted_career = analyze_text(text_message)
    else:
        form = TextForm()

    return render(request, 'translation_app/predict_career.html', {'form': form, 'predicted_career': predicted_career})


