from django import forms
from .models import Questionario


class QuestionarioForm(forms.ModelForm):
    class Meta:
        model = Questionario
        labels = {
            "questao01": "1 - Com relação a empresa onde você trabalha, existe incentivo para que os colaboradores busquem por inovação nos processos/produtos?",
            "questao02": "2 - Na sua percepção, existem possíveis mudanças/melhorias nos processos/produtos que possam ser realizadas?",
            "questao03": "3 - Em relação às outras empresas do ramo classifique sua empresa:",
            "questao04": "4 - A empresa busca maneiras inteligentes de lidar com a concorrência?",
            "questao05": "5 - Como você caracterizaria os diferenciais da sua empresa em relação às demais empresas do setor?",
            "questao06": "6 - A empresa frequentemente melhora seus produtos/serviços?",
            "questao07": "7 - Ocorrem pesquisas com os consumidores para aprimorar seus produtos/serviços?",
            "questao08": "8 - A empresa busca sugestões dos consumidores para desenvolver melhorias em seus produtos/serviços?",
            "questao09": "9 - Existe um controle de qualidade nos processos/produtos?",
            "questao10": "10 - Os colaboradores da empresa aceitam evoluções tecnológicas ou preferem utilizar as ferramentas que já estão familiarizados?",
            "questao11": "11 - Com qual frequência a empresa pesquisa formas de melhoria?",
            "questao12": "12 - No cotidiano dos colaboradores da empresa, qual frequência em que é utilizado dos meios tecnológicos para melhorar o desempenho nos processos",
        }
        widgets = {
            'questao01': forms.RadioSelect(),
            'questao02': forms.RadioSelect(),
            'questao03': forms.RadioSelect(),
            'questao04': forms.RadioSelect(),
            'questao05': forms.RadioSelect(),
            'questao06': forms.RadioSelect(),
            'questao07': forms.RadioSelect(),
            'questao08': forms.RadioSelect(),
            'questao09': forms.RadioSelect(),
            'questao10': forms.RadioSelect(),
            'questao11': forms.RadioSelect(),
            'questao12': forms.RadioSelect(),
        }
        fields = "__all__"
