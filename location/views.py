from django.shortcuts import render

# Create your views here.

# display the about page
def about(request):
    return render(request, 'about.html')