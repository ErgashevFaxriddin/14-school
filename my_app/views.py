from django.http import HttpResponse

def first_view(request):
    html = """
    <h1>Welcome books world!</h1>
    <h2>Main</h2>
    <a href="blog/"> blog >> </a><br> 
    <a href="second/"> second page >> </a><br>
    """
    return HttpResponse(html)


def second_view(request):
    html = """
    <h1>Second page</h1>
    <a href="/"> << First page </a>
    """
    return HttpResponse(html)

def blog(request):
    html = """
    
    <h1>Blog</h1>
    <a href="/" << First page </a>
    """
    return HttpResponse(html)
