from django.shortcuts import render

# Create your views here.

# display the homepage
def home(request):
    return render(request, 'index.html')

# display the about page
def about(request):
    return render(request, 'about.html')
