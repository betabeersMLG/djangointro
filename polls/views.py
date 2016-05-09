from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import *


def index(request):
    latest_question_list = Question.objects.order_by('-pk')[:5]
    return render(request, 'index.html', {"latest_question_list":latest_question_list})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    error = False
    success = False

    if request.method == 'POST':
        try:
            selected_choice = question.choices.get(pk=request.POST['choice'])
        except Choice.DoesNotExist:
            error = True
        else:
            selected_choice.votes += 1
            selected_choice.save()
            success = True

    return render(request, 'detail.html', {"question":question, "error":error, "success":success})