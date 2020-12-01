from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
atext = ["hello" , "hi", "igi"]
def index(request):
     return render(request, "index.html" , {
     "heading": atext[2],
     "text": atext[1]
     })
