from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import os
import requests
from dotenv import load_dotenv
from django.shortcuts import render

load_dotenv()

GITHUB_USERNAME = 'owenleungg'
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

def fetch_github_builds():
    headers = {'Authorization': f'token {GITHUB_TOKEN}'} if GITHUB_TOKEN else {}
    runs_url = 'https://api.github.com/repos/owenleungg/Slipdeck/actions/runs?per_page=20'
    runs = requests.get(runs_url, headers=headers).json()
    jobs = []

    if not isinstance(runs, dict):
        return jobs

    for run in runs.get('workflow_runs', []):
        conclusion = run.get('conclusion')

        if conclusion == 'success':
            status = 'passing'
        elif conclusion in ('failure', 'cancelled'):
            status = 'failing'
        else:
            status = 'running'

        jobs.append({
            'name':         run.get('name', 'Slipdeck'),
            'status':       status,
            'branch':       run.get('head_branch', 'main'),
            'triggered_by': run.get('event', 'push'),
            'created_at':   run.get('created_at', ''),
            'url':          run.get('html_url', '#'),
        })

    return jobs

def dashboard(request):
    jobs = fetch_github_builds()
    context = {
        'jobs':          jobs,
        'total':         len(jobs),
        'passing_count': sum(1 for j in jobs if j['status'] == 'passing'),
        'failing_count': sum(1 for j in jobs if j['status'] == 'failing'),
        'running_count': sum(1 for j in jobs if j['status'] == 'running'),
    }
    return render(request, 'monitor/dashboard.html', context)