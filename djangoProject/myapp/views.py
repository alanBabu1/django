from django.shortcuts import render
from .models import Question
from .models import Choice

# Create your views here.
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

from django.shortcuts import render

def question_list(request):
	context ={}
	context["dataset"] = Question.objects.all()
	return render(request,"ques.html",context)


def index(request,id):
	context ={}
	context["dataset"] = Choice.objects.filter(question=id)
	return render(request,"index.html",context)

