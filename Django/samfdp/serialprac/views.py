from django.shortcuts import render
from .models import music_library
from rest_framework import viewsets
from .serializers import music_librarySerializer
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class music_libraryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = music_library.objects.all()
    serializer_class = music_librarySerializer

class IndexView(generic.ListView):
    template_name = 'index.html '
    context_object_name = 'albums' #if this line is not used then in template we have to use object_list
    queryset = music_library.objects.all()

class DetailsView(generic.DetailView):
    model = music_library
    template_name = 'details.html'

class MusicCreate(CreateView):
    model = music_library
    fields = '__all__'
    success_url = reverse_lazy('index')
    template_name = 'addform.html'