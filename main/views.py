from django.shortcuts import render, redirect
from .forms import ApplicationForm

# Create your views here.
def index(request):
    context = {
        'active_page': 'homepage'
    }
    return render(request, "main/index.html", context)


def projects(request):
    context = {
        'active_page': 'projects'
    }
    return render(request, "main/projects.html", context)


def faq(request):
    context = {
        'active_page': 'faq'
    }
    return render(request, 'main/faq.html', context)


def contact(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')  # Редирект после успешной отправки
    else:
        form = ApplicationForm()
    context = {
        'active_page': 'contact',
        'form': form
    }
    return render(request, 'main/contact.html', context)


def not_found(request, exception):
    return render(request, 'main/not_found.html', status=404)
