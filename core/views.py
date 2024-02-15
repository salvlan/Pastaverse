from django.shortcuts import render

# Create your views here.

# display the homepage
def home(request):
    return render(request, 'index.html')


