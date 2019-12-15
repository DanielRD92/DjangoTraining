from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    first_graph="My first bokeh graph will be rendered on this page"
    return HttpResponse(first_graph)