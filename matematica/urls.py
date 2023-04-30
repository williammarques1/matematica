from django.urls import path
from provas.views import (
    PerguntaListView, 
    PerguntaCreateView, 
    PerguntaDetailView, 
    PerguntaUpdateView, 
    PerguntaDeleteView,
    TemaCreateView,
    TemaDetailView,
    TemaUpdateView,
    TemaDeleteView,
    TemaListView,
)

urlpatterns = [
    # URLs para as views de Pergunta
    path('pergunta/', PerguntaListView.as_view(), name='pergunta_list'),
    path('pergunta/create/', PerguntaCreateView.as_view(), name='pergunta_create'),
    path('pergunta/<int:pk>/', PerguntaDetailView.as_view(), name='pergunta_detail'),
    path('pergunta/<int:pk>/update/', PerguntaUpdateView.as_view(), name='pergunta_update'),
    path('pergunta/<int:pk>/delete/', PerguntaDeleteView.as_view(), name='pergunta_delete'),
    
    # URLs para as views de Tema
    path('tema/', TemaListView.as_view(), name='tema_list'),
    path('tema/criar/', TemaCreateView.as_view(), name='tema_create'),
    path('tema/<int:pk>/', TemaDetailView.as_view(), name='tema_detail'),
    path('tema/<int:pk>/update/', TemaUpdateView.as_view(), name='tema_update'),
    path('tema/<int:pk>/delete/', TemaDeleteView.as_view(), name='tema_delete'),
]
