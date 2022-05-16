from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import CharactorModel
from django.urls import reverse_lazy

# Create your views here.
def helloworldfunction(request):
    return render(request, 'helloworld.html')
  
def index(request):
    return render(request, 'index.html')

def create(request):
    return render(request, 'create.html')

def list(request):
    return render(request, 'list.html')
  

class CharactorCreate(CreateView):
  template_name = 'create.html'
  model = CharactorModel
  fields = ('name', 'gender', 'feature')
  success_url = reverse_lazy('list')
  

class CharactorList(ListView):
  template_name = 'list.html'
  model = CharactorModel