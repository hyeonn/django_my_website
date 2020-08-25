from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.http import HttpResponse


# Create your views here.

def main(request):
    return  render(
        request,
        'startbootstrap/main.html'
    )

