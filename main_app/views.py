from django.shortcuts import render
from .models import Item

# Create your views here.
def wish_index(request):
  return render(request, 'index.html')