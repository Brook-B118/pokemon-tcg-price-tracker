from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'homepage/home.html')  # Make sure to create this template