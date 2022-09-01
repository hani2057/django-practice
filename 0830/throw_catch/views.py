from django.shortcuts import render

# Create your views here.

def first(reqest):
    return render(reqest, 'first.html')