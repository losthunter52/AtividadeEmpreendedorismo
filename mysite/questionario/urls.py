from django.urls import include, path
from . import views

# Generic
urlpatterns = [
    path('', views.cadastroQuestionario, name='Questionario'),
    path('agradecimento/', views.agradecimento, name='Agradecimento'),
    path('resultado/', views.resultado, name='Resultado'),
]

