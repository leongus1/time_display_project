from django.shortcuts import render, HttpResponse
from time import strftime, localtime



def show_time(request):
    context = {
        "time": strftime("%B %d, %Y   %I:%M %p", localtime()),
    }
    return render(request, 'index.html', context)

# Create your views here.
