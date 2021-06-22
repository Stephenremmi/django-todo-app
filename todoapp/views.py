from django.shortcuts import render
from django.http import HttpResponse
from 
# Create your views here.
# Create List View to display List of Todo items
class TaskList(ListView):
    model = Task


    