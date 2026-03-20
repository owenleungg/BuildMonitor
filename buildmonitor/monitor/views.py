from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render
from .models import BuildJob

def dashboard(request):
    jobs = BuildJob.objects.all()
    context = {
        'jobs':          jobs,
        'total':         jobs.count(),
        'passing_count': jobs.filter(status='passing').count(),
        'failing_count': jobs.filter(status='failing').count(),
        'running_count': jobs.filter(status='running').count(),
    }
    return render(request, 'monitor/dashboard.html', context)