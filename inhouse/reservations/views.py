from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def new_help_session(request):
    return render(request, 'new_help_session_student_view.html')