from django.db.models import query
from django.shortcuts import render
from .models import Article

# Create your views here.

def blog_create_view(request):
    context={}
    if request.method=="POST":

        title=request.POST.get("title")
        content=request.POST.get("content")
        article_object=Article.objects.create(title=title, content=content)
        context['object']=article_object
        context['created']=True
    
    return render(request,"blog/create.html",context=context)

def blog_detail_view(request,id):
    article_obj=None
    if id is not None:
        article_obj=Article.objects.get(id=id)

    context={
        "object":article_obj,
    }

    return render(request,"blog/detail.html",context=context)

def article_search_view(request):
    query_dict=request.GET  #this is dictionary
    #query=query_dict.get("q") #<input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" name="q"
    
    try:
        query=int(query_dict.get("q"))
    except:
        query=None

    article_obj=None
    if query is not None:
        article_obj=Article.objects.get(id=query)

    context={
        "object":article_obj

    }
    return render(request, "blog/search.html", context=context)