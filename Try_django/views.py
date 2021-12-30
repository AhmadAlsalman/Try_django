from django.http import HttpResponse


"""
to render html web pages
"""
'''
def home(request):
    return response
the function take in  a request(django send request) and return HTML response
'''

HTML_STRING=""" <h1>Hello World </h1> """

def home_view(request):
    return HttpResponse(HTML_STRING)

