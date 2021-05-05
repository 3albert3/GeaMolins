from django.urls import path, include
from .views import BlogListView,EntradaDetailView, SearchResultsView, Seccion1ListView




urlpatterns = [
    path('',BlogListView.as_view(), name='Blog_list'),
   
    path('Entrada/<slug:slug>/', EntradaDetailView.as_view(), name='entrada_detail'),

    path('search/',SearchResultsView.as_view(), name='search_results'), 

    path('Escalada/',Seccion1ListView.as_view(), name='Escalada_list'),
    
]