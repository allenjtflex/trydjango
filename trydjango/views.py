from django.shortcuts import render

def home(request):
    title = "Home Index"
    return render(request, "index.html", locals())
