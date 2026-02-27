from django.shortcuts import render
from .models import Countries
from django.http import HttpResponse

def orm_list(request):
    countries = Countries.objects.all()
    country_list = ""
    for c in countries:
        country_list += f"<li>{c.country_name}</li>"
    return HttpResponse(f"<ol>{country_list}</ol>")