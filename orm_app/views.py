from django.shortcuts import render
from .models import Countries
from django.http import HttpResponse

def index_page(request):
    return render(request, "index.html")

# def orm_list(request):
#     queryset = Countries.objects.filter(region_id=2)
#     print(queryset.query)
#     country_list = ""
#     for c in queryset:
#         country_list += f"<li>{c}</li>"
#     return HttpResponse(f"<ol>{country_list}</ol>")