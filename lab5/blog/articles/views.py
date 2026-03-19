from django.shortcuts import render
from django.http import Http404
from .models import Article
from django.shortcuts import redirect
from django.contrib.auth.models import User

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
        # Получаем данные из формы
        form = {
            'text': request.POST.get('text', ''),
            'title': request.POST.get('title', '')
        }
        
        # Проверка на заполненность
        if form['text'] and form['title']:
            # Проверка на уникальность названия
            try:
                Article.objects.get(title=form['title'])
                form['errors'] = "Статья с таким названием уже существует"
                return render(request, 'create_post.html', {'form': form})
            except Article.DoesNotExist:
                # Создаём статью
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
        # Просто показываем пустую форму
        return render(request, 'create_post.html', {})
