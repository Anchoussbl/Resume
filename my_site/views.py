from django.shortcuts import render

posts = [
    {
        'name': 'ANNA SOBOLEVA',
        'profession': 'Junior Python-Developer',
    }
]


def home(request):
    context = {
        'posts': posts,
        'active' : 'Home'
    }
    return render(request, 'my_site/home.html', context)


def skills(request):
    return render(request, 'my_site/skills.html', {'title': 'Skills', 'active' : 'Skills'})

def education(request):
    return render(request, 'my_site/education.html', {'title': 'Education', 'active' : 'Education'})

def experience(request):
    return render(request, 'my_site/experience.html', {'title': 'Experience', 'active': 'Experience'})

def base(request):
    return render(request, 'my_site/base.html', {'title': 'Base'})