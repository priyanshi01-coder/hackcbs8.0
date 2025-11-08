from django.shortcuts import render , redirect

# Create your views here.
def home_view(request):
    return render(request, "home.html")

def about_view(request):
    return render(request, "about.html")

def how_to_view(request):
    return render(request, "how_to.html")