from django.db import models

Q01_CHOICES = (
    (1, 'Não ocorre incentivo'),
    (4, 'Não buscamos por inovação no momento'),
    (6, 'Raramente acontece algum incentivo'),
    (10, 'Sim, frequentemente ocorrem incentivos')
)

Q02_CHOICES = (
    (1, 'Não, os produtos já estão bons'),
    (4, 'Sim, porém, não podem ser realizadas no momento'),
    (6, 'Não, pois já realizamos melhorias recentemente'),
    (10, 'Sim, estamos sempre buscando por melhorias')
)

Q03_CHOICES = (
    (1, 'Igual a algumas empresas já existentes na mesma cidade '),
    (4, 'Igual a algumas empresas já existentes em outras cidades '),
    (8, 'Inovadora, pois apesar de existirem empresas parecidas, temos diferenciais'),
    (9, 'Completamente única em nossa cidade'),
    (10, 'Completamente única no nosso país')
)

Q04_CHOICES = (
    (1, 'Não temos concorrência'),
    (2, 'Não nos preocupamos com a concorrência '),
    (6, 'Raramente buscamos maneiras de lidar com a concorrência'),
    (8, 'Frequentemente buscamos maneiras de lidar com a concorrência'),
    (10, 'Sempre buscamos maneiras de lidar com a concorrência ')
)

Q05_CHOICES = (
    (1, 'Não temos diferenciais'),
    (4, 'Não temos diferenciais, apenas focamos em fazer o básico bem feito'),
    (6, 'Temos alguns diferenciais, mas não são muitos '),
    (10, 'Temos inúmeros diferenciais, nossa empresa é inovadora em relação às demais')
)

Q06_CHOICES = (
    (1, 'Não buscamos por melhorias'),
    (3, 'Não, nossos produtos/serviços já são de total agrado'),
    (7, 'Sim, mas raramente buscamos melhorar nossos produtos/serviços'),
    (10, 'Sim, sempre buscamos melhorar nossos produtos/serviços')
)

Q07_CHOICES = (
    (1, 'Não precisamos de pesquisas para aprimorar nossos produtos/serviços'),
    (4, 'Não ocorrem pesquisas'),
    (7, 'Não temos pesquisas, mas toda sugestão dada pelos consumidores é bem vinda '),
    (8, 'Sim, mas raramente fazemos pesquisas para aprimorar nossos produtos/serviços'),
    (10, 'Sim, sempre que possível fazemos pesquisas para aprimorar nossos produtos/serviços')
)

Q08_CHOICES = (
    (1, 'Não buscamos sugestões dos consumidores'),
    (6, 'Buscamos sugestões apenas dos maiores consumidores'),
    (6, 'Raramente buscamos sugestões dos consumidores'),
    (10, 'Sempre buscamos sugestões dos consumidores')
)

Q09_CHOICES = (
    (1, 'Não existe nenhum controle de qualidade '),
    (4, 'Não existe controle de qualidade pois já fazemos o mesmo produto a muito tempo '),
    (7, 'Sim, alguns produtos são submetidos a um controle de qualidade'),
    (10, 'Sim, todos os produtos são submetidos a um controle de qualidade')
)

Q10_CHOICES = (
    (1, 'Não, nossos colaboradores não aceitam evoluções tecnológicas'),
    (4, 'Não, nossos colaboradores já estão satisfeitos com as ferramentas existentes'),
    (6, 'Sim, se for algo que facilite o seu trabalho'),
    (10, 'Sim, nossos colaboradores sempre aceitam evoluções tecnológicas que contribuam com a empresa')
)

Q11_CHOICES = (
    (1, 'Nunca pesquisamos formas de melhoria'),
    (6, 'Raramente pesquisamos formas de melhoria '),
    (6, 'Quando o rendimento da empresa diminui, pesquisamos melhorias'),
    (10, 'Sempre pesquisamos melhorias ')
)

Q12_CHOICES = (
    (1, 'Não usamos meios tecnológicos'),
    (1, 'Não precisamos usar de meios tecnológicos'),
    (6, 'Somente quando necessário usamos meios tecnológicos'),
    (10, 'Diariamente usamos de meios tecnológicos')
)

# Create your models here.

class Questionario(models.Model):
    questao01 = models.IntegerField(choices=Q01_CHOICES, default=1)
    questao02 = models.IntegerField(choices=Q02_CHOICES, default=1)
    questao03 = models.IntegerField(choices=Q03_CHOICES, default=1)
    questao04 = models.IntegerField(choices=Q04_CHOICES, default=1)
    questao05 = models.IntegerField(choices=Q05_CHOICES, default=1)
    questao06 = models.IntegerField(choices=Q06_CHOICES, default=1)
    questao07 = models.IntegerField(choices=Q07_CHOICES, default=1)
    questao08 = models.IntegerField(choices=Q08_CHOICES, default=1)
    questao09 = models.IntegerField(choices=Q09_CHOICES, default=1)
    questao10 = models.IntegerField(choices=Q10_CHOICES, default=1)
    questao11 = models.IntegerField(choices=Q11_CHOICES, default=1)
    questao12 = models.IntegerField(choices=Q12_CHOICES, default=1)