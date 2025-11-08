from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dashboard_view(request):
    return render(request, "dashboard/dashboard.html")

@login_required
def my_sessions(request):
    return render(request, "dashboard/my_sessions.html")

@login_required
def uploaded_items(request):
    return render(request, "dashboard/uploaded_items.html")

@login_required
def analytics(request):
    from dashboard.models import InterviewSession, SessionAnalytics
    from django.db.models import Avg, Count, Max