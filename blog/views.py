from django.db.models import query
from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm

# Create your views here.
def login_view(request):
    
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request, username=username, password=password)
        if user is None:
            context={"Error":"Invalid username or password"}
            return render(request, "accounts/login.html", context)
        login(request, user)
        return redirect('/')

    return render(request, "accounts/login.html", {})


def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect("/login/")

    return render(request, "accounts/logout.html", {})

def register_view(request):
    return render(request, "accounts/register.html", {})

@login_required
def blog_create_view(request):
    context={
        "form":ArticleForm()
    }
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