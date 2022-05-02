from django.http import Http404
from django.shortcuts import render
from .models import Question,Choice
from django.shortcuts import render
from .models import Question


def index(request):
    latest_question_list = Question.objects.all()[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)
    
def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'detail.html', {'question': question})


def results(request, question_id):
    question = Choice.objects.get(pk=question_id)
    return render(request, 'results.html', {'question': question})
