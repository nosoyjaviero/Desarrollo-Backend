from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    lastest_question_list=Question.objects.all()
   
    return render(request, "polls/index.html",{'lastest_question_list':lastest_question_list})

def detail(request, id):
    return HttpResponse(f'Estas viendo la pregunta {id}')

def results(request, id):
    return HttpResponse(f'Estas viendo los resultados de la pregunta {id}')

def vote(request, id):
    return HttpResponse(f'Estas votando a la pregunta {id}')
    

