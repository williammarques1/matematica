from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Pergunta, Tema
from .forms import PerguntaForm, TemaForm

class PerguntaListView(ListView):
    model = Pergunta
    template_name = 'provas/pergunta_list.html'
    context_object_name = 'perguntas'

class PerguntaCreateView(CreateView):
    model = Pergunta
    form_class = PerguntaForm
    template_name = 'provas/pergunta_form.html'

    def get_success_url(self):
        return reverse('pergunta_list')

class PerguntaDetailView(DetailView):
    model = Pergunta
    template_name = 'provas/pergunta_detail.html'
    context_object_name = 'pergunta'

class PerguntaUpdateView(UpdateView):
    model = Pergunta
    form_class = PerguntaForm
    template_name = 'provas/pergunta_form.html'

    def get_success_url(self):
        return reverse('pergunta_list')

class PerguntaDeleteView(DeleteView):
    model = Pergunta
    template_name = 'provas/pergunta_confirm_delete.html'
    success_url = reverse_lazy('pergunta-list')

class PerguntaListView(ListView):
    model = Pergunta
    template_name = 'provas/pergunta_list.html'
    context_object_name = 'perguntas'


class TemaCreateView(CreateView):
    model = Tema
    form_class = TemaForm
    template_name = 'provas/tema_form.html'

    def get_success_url(self):
        return reverse('tema_detail', args=[self.object.pk])


class TemaUpdateView(UpdateView):
    model = Tema
    form_class = TemaForm
    template_name = 'provas/tema_form.html'

    def get_success_url(self):
        return reverse('tema_detail', args=[self.object.pk])
    

class TemaDetailView(DetailView):
    model = Tema
    template_name = 'provas/tema_detail.html'


class TemaDeleteView(DeleteView):
    model = Tema
    success_url = reverse_lazy('tema_list')
    template_name = 'provas/tema_confirm_delete.html'


class TemaListView(ListView):
    model = Tema
    template_name = 'provas/tema_list.html'
    context_object_name = 'temas'