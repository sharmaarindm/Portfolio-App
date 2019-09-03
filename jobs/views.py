from django.shortcuts import render


def home(request):
    # will be looking for it inside the templates directory/modelname
    return render(request, 'jobs/home.html')
