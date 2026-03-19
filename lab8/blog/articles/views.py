from django.shortcuts import render, redirect
from django.http import Http404
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404("Статья не найдена")

def create_post(request):
    if request.user.is_anonymous:
        raise Http404("Только авторизованные пользователи могут создавать статьи")
    
    if request.method == "POST":
        form = {
            'text': request.POST.get('text', ''),
            'title': request.POST.get('title', '')
        }
        
        if form['text'] and form['title']:
            try:
                Article.objects.get(title=form['title'])
                form['errors'] = "Статья с таким названием уже существует"
                return render(request, 'create_post.html', {'form': form})
            except Article.DoesNotExist:
                article = Article.objects.create(
                    text=form['text'],
                    title=form['title'],
                    author=request.user
                )
                return redirect('get_article', article_id=article.id)
        else:
            form['errors'] = "Не все поля заполнены"
            return render(request, 'create_post.html', {'form': form})
    else:
        return render(request, 'create_post.html', {})

def register(request):
    if request.method == "POST":
        form = {
            'username': request.POST.get('username', ''),
            'email': request.POST.get('email', ''),
            'password': request.POST.get('password', ''),
            'password2': request.POST.get('password2', '')
        }
        
        if form['username'] and form['password'] and form['password2']:
            if form['password'] != form['password2']:
                form['errors'] = "Пароли не совпадают"
                return render(request, 'register.html', {'form': form})
            
            try:
                User.objects.get(username=form['username'])
                form['errors'] = "Пользователь с таким именем уже существует"
                return render(request, 'register.html', {'form': form})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=form['username'],
                    email=form['email'],
                    password=form['password']
                )
                login(request, user)
                return redirect('archive')
        else:
            form['errors'] = "Не все поля заполнены"
            return render(request, 'register.html', {'form': form})
    else:
        return render(request, 'register.html', {})

def user_login(request):
    if request.method == "POST":
        form = {
            'username': request.POST.get('username', ''),
            'password': request.POST.get('password', '')
        }
        
        if form['username'] and form['password']:
            user = authenticate(
                username=form['username'],
                password=form['password']
            )
            if user is not None:
                login(request, user)
                return redirect('archive')
            else:
                form['errors'] = "Неверный логин или пароль"
                return render(request, 'login.html', {'form': form})
        else:
            form['errors'] = "Не все поля заполнены"
            return render(request, 'login.html', {'form': form})
    else:
        return render(request, 'login.html', {})
from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('archive')
