from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def student_attend_view(request):
    return HttpResponse("<h2>Student Attendance App</h2>")