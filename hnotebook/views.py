from django.http import HttpResponse
from django.shortcuts import render_to_response

def homepage(self):
    return render_to_response('home.html', {})

def signup(self):
    return render_to_response('signup.html', {})
