from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
from django.utils import timezone
import datetime



def show_time(request):
    context = {
        "time": strftime("%B %d, %Y \n%H:%M %p", gmtime())
    }
    return render(request, 'index.html', context)

# Create your views here.
