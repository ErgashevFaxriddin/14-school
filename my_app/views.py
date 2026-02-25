from django.http import HttpResponse

def first_view(request):
    html = """
    <h1>Welcome to the books world!</h1>
    <h2>Main</h2>
    <a href="/blog/">Blog >> </a><br> 
    <a href="/second/">Second page >> </a><br>
    <a href="/countries/">Countries >> </a><br>
    """
    return HttpResponse(html)

def second_view(request):
    html = """
    <h1>Second page</h1>
    <a href="/"><< First page</a>
    """
    return HttpResponse(html)

def blog(request):
    html = """
    <h1>Blog</h1>
    <a href="/"><< First page</a>
    """
    return HttpResponse(html)