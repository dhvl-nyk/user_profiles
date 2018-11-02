from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.http import HttpResponse

from django.http import *
from django.contrib.auth import logout
from django.core.management import call_command
from django.conf import settings
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.forms.models import model_to_dict
# from django.views.decorators.csrf import csrf_exempt
# from bson import json_util
from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect



def addUser(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('addUser')
    else:
        f = CustomUserCreationForm()
    return render(request, 'addUser.html', {'form': f})

def api(request):
    html = "<html><body>It is now </body></html>"
    return HttpResponse(html)    

