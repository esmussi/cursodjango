from django.shortcuts import render
from .models import Post
from .models import Contact

def hello_blog(request):
    lista = [
        'Django','Python','Git','Html',
        'Banco de dados','Linux','Nginx','Uwsgi',
        'Sistem CTL',
    ]
    list_posts = Post.objects.all()
    list_contacts = Contact.objects.all()
    
    data = {
        'name': 'Curso de Django 3',
        'Lista_tecnologias': lista,
        'posts': list_posts,
        'contacts': list_contacts
        }
    
    
    return render(request, 'index.html', data)
