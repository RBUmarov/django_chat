from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User, Group

def is_bunned(user):
    return user.groups.filter(name='Bunned').exists()