from django.forms import NullBooleanField, inlineformset_factory, modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from .models import Questionario
from .forms import QuestionarioForm
from django.db.models import Avg
from django.db.models import Q
from django.db.models import Sum, Count, Value, CharField
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User

def cadastroQuestionario(request):
    form = QuestionarioForm()
    if request.method == 'POST':
        form = QuestionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Agradecimento')

    return render(request, 'cadastro.html', {'form': form})

def agradecimento(request):
    return render(request, 'agradecimento.html')

def resultado(request):
    template_name = 'resultado.html'
    questao01 = Questionario.objects.aggregate(Avg('questao01'))
    questao02 = Questionario.objects.aggregate(Avg('questao02'))
    questao03 = Questionario.objects.aggregate(Avg('questao03'))
    questao04 = Questionario.objects.aggregate(Avg('questao04'))
    questao05 = Questionario.objects.aggregate(Avg('questao05'))
    questao06 = Questionario.objects.aggregate(Avg('questao06'))
    questao07 = Questionario.objects.aggregate(Avg('questao07'))
    questao08 = Questionario.objects.aggregate(Avg('questao08'))
    questao09 = Questionario.objects.aggregate(Avg('questao09'))
    questao10 = Questionario.objects.aggregate(Avg('questao10'))
    questao11 = Questionario.objects.aggregate(Avg('questao11'))
    questao12 = Questionario.objects.aggregate(Avg('questao12'))
    questao01 = questao01['questao01__avg']
    questao02 = questao02['questao02__avg']
    questao03 = questao03['questao03__avg']
    questao04 = questao04['questao04__avg']
    questao05 = questao05['questao05__avg']
    questao06 = questao06['questao06__avg']
    questao07 = questao07['questao07__avg']
    questao08 = questao08['questao08__avg']
    questao09 = questao09['questao09__avg']
    questao10 = questao10['questao10__avg']
    questao11 = questao11['questao11__avg']
    questao12 = questao12['questao12__avg']
    capacidadeDeInovacao = [questao01, questao02]
    inteligenciaCompetitiva = [questao03, questao04, questao05]
    desenvolvimentoDeProdutos = [questao06, questao07]
    monitoramento = [questao08, questao09]
    desempenhoDaInovacao = [questao10, questao11, questao12]
    quantidadeParticipantes = Questionario.objects.count()
    capacidadeDeInovacao = round(sum(capacidadeDeInovacao) / len(capacidadeDeInovacao), 2)
    inteligenciaCompetitiva = round(sum(inteligenciaCompetitiva) / len(inteligenciaCompetitiva), 2)
    desenvolvimentoDeProdutos = round(sum(desenvolvimentoDeProdutos) / len(desenvolvimentoDeProdutos), 2)
    monitoramento = round(sum(monitoramento) / len(monitoramento), 2)
    desempenhoDaInovacao = round(sum(desempenhoDaInovacao) / len(desempenhoDaInovacao), 2)
    data = [capacidadeDeInovacao, inteligenciaCompetitiva, desenvolvimentoDeProdutos, monitoramento, desempenhoDaInovacao]
    context = {
        'quantidadeParticipantes': quantidadeParticipantes,
        'data': data
    }
    return render(request, template_name, context)   