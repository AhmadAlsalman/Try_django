from django.http import HttpResponse
from django.template.loader import render_to_string
from blog.models import Article



"""
to render html web pages
"""
'''
def home(request):
    return response
the function take in  a request(django send request) and return HTML response
'''

#HTML_STRING=""" <h1>Hello World </h1> """

def home_view(request,id=None, *args, **kwargs):

    article_obj =Article.objects.get(id=1)
    my_list=[300,250,200,150,100,50,0]
    my_objects=Article.objects.all()

    context= {
         "my_objects":my_objects,
         "my_list":my_list,
         "title":article_obj.title,
         "id":article_obj.id,
         "content":article_obj.content
     }
     #django templates
    HTML_STRING=render_to_string("home-view.html",context=context)

    return HttpResponse(HTML_STRING)

