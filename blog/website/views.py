from django.shortcuts import render

def hello_blog(request):
    lista = [
        'Django','Python','Git','Html',
        'Banco de dados','Linux','Nginx','Uwsgi',
        'Sistem CTL',
    ]
    data = {'name': 'Curso de Django 3', 'Lista_tecnologias': lista}
    return render(request, 'index.html', data)