from django.shortcuts import render
from django.conf import settings

import requests
from github import Github
import logging
from .forms import SubmitGit
from .serializer import GitSerializer
from github import Github, GithubException

def GitSearch(request):
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        user = response.json()

    return render(request, 'index.html', {'search_result': user})
