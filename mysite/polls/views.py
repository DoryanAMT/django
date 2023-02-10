from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Question,Choice
from django.template import loader
from django.urls import reverse


def index(request):
    # ORM pedir preguntas
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
        }
    return render(request, 'polls/index.html', context)


def detalle(request, id):
    # Pide al ORM la pregunta con ese id
    # Y si no la encuentra levanta una excepcion 404
    encuesta = get_object_or_404(Question, pk=id)
    return render(
        request,
        'polls/detalle.html',
        {
            'encuesta': encuesta
        }
    )

def vote(request, id):
    question = get_object_or_404(Question, pk=id)
    try:
        selected_choice = question.options.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detalle.html', {
            'encuesta': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # return HttpResponseRedirect(f"/polls/{question.id}/resultado/")
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:resultado', args=(question.id,)))

def resultado(request, id):
    question = get_object_or_404(Question, pk=id)
    return render(request, 'polls/resultado.html',{
        'encuesta':question
    })