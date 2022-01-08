from django.db.models import query
from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm, ArticleFormOld


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj=form.save()
        return redirect('/login')
    context={"form": form }
    
    return render(request,"accounts/register.html", context)

# Create your views here.
def login_view(request):
    
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST) 
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('/')
    else:
        form=AuthenticationForm(request)
    context={"form":form}
    return render(request, "accounts/login.html", context)


def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect("/login/")

    return render(request, "accounts/logout.html", {})

@login_required
def blog_create_view(request):
    
    form=ArticleForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        article_object=form.save()
        context["form"]=ArticleForm()

        #title=request.POST.get("title")
        #content=request.POST.get("content")
        #article_object=Article.objects.create(title=title, content=content)
        #context['object']=article_object
        #context['created']=True
    
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