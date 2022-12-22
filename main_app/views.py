from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Villain

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def villains_index(request):
  villains = Villain.objects.all()
  return render(request, 'villains/index.html', { 'villains': villains })

def villains_detail(request, villain_id):
  villain = Villain.objects.get(id=villain_id)
  return render(request, 'villains/detail.html', { 'villain': villain })

class VillainCreate(CreateView):
  model = Villain
  fields = '__all__'

class VillainUpdate(UpdateView):
  model = Villain
  fields = ['description', 'badness_scale'] ##<-- (because name and identity will not be updated)

class VillainDelete(DeleteView):
  model = Villain
  success_url = '/villains/'