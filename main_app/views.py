from django.shortcuts import render
from .models import Item
from django.views.generic.edit import CreateView, DeleteView

# Create your views here.
def wish_index(request):
  item_list = Item.objects.all()
  return render(request, 'index.html', {
    'item_list': item_list
  })

class ItemCreate(CreateView):
  model = Item
  fields = ['description']
  success_url = '/'

class ItemDelete(DeleteView):
  model = Item
  success_url = '/'