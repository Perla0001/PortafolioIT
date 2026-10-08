from django.shortcuts import render
from .models import Project, Technology, Certificate, Greeting

def home(request):
    context= {
        "projects": Project.objects.filter(is_visible=True),
        "technologies": Technology.objects.all(),
        "certificates": Certificate.objects.all(),
        "greetings": list(Greeting.objects.values_list("text", flat=True)),
    }
    return render(request, "portfolio/home.html", context)