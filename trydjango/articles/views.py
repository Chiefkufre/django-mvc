from types import new_class 
from django.shortcuts import render, redirect
from django.http import response
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

from .models import Article

def search_article_views(request, id=None, *args, **kwargs):


    # query_dict = request.GET

    # if query_dict:
    #     try:
    #         query = query_dict.get('q')
    #     except:
    #         query = None
    #     query = None
    #     article_obj = None
    #     if query is not None:
            # lookup = Q(title__icontains=query) | Q(content__icontains=query)
            # article_obj = Article.object.filter(lookup).order_by('created')
    query = request.GET.get('q')
    article_obj = Article.objects.search(query)
    context = {
        "object": article_obj
    }

    template = 'article/article.html'
    return render(request, template, context=context)

@login_required
def create_article_view(request, *args, **kwargs):

    form = ArticleForm(request.POST or None)
    context = {
        'form': form
    }
    
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()
        # not neccessary 
        return redirect(article_object.get_absolute_url()) 


        # title = form.cleaned_data['title']
        # content = form.cleaned_data['content']
        # new_article = Article.objects.create(title=title, content=content)
        # context['objects'] = new_article
        # context['created'] = True
    return render(request, 'login.html', context=context)
    

def login_view(request, *args, **kwargs):
    method = request.method
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)

        if user is None:
            context = {'username or passwoord is incorrect'}
            return render(request, 'login.html', context=context)
        else:
            login(request, user)
            return redirect('admin/')

    context = {}
    return render(request, 'login.html', context=context)

def login_view2(request, user=None):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.Post)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(url_for('login'))
    else:
        form = AuthenticationForm(request)
    return render(request, 'login.html', {'form': form})
 
