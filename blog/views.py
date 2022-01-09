from django.core.exceptions import MultipleObjectsReturned
from django.db.models import query
from django.http.response import Http404
from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm, ArticleFormOld
from django.db.models import Q


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

def blog_detail_view(request,slug=None):
    article_obj=None
    if slug is not None:
        article_obj=Article.objects.get(slug=slug)
        try:
            article_obj=Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404

        except Article.MultipleObjectsReturned:
            article_obj=Article.objects.filter(slug=slug).first()
        except:
            raise Http404

    context={
        "object":article_obj,
    }

    return render(request,"blog/detail.html",context=context)

def article_search_view(request):
    query=request.GET.get('q')
    qs=Article.objects.all()
    if query is not None:
        lookups=Q(title__icontains=query) #we can use multible Q lookuos =Q(title__icontains=query)|Q(content__icontains=query)
        qs=Article.objects.filter(lookups)
    context={
        "object_list":qs

    }
    return render(request, "blog/search.html", context=context)