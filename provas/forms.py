from django.forms import ModelForm, ModelChoiceField, ChoiceField, Select, Textarea
from .models import Pergunta, Tema

class PerguntaForm(ModelForm):
    tema = ModelChoiceField(queryset=Tema.objects.all(), empty_label=None, widget=Select(attrs={'class': 'form-control'}))
    DIFICULDADE_CHOICES = (
        ('FACIL', 'Fácil'),
        ('MEDIO', 'Médio'),
        ('DIFICIL', 'Difícil')
    )
    dificuldade = ChoiceField(choices=DIFICULDADE_CHOICES, widget=Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Pergunta
        fields = '__all__'
        widgets = {
            'enunciado': Textarea(attrs={'class': 'form-control'}),
        }

class TemaForm(ModelForm):
    class Meta:
        model = Tema
        fields = ['nome']
