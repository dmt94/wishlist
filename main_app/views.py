from django.shortcuts import render

# Create your views here.
def wish_index(request):
  return render(request, 'index.html')