from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.shortcuts import render, redirect
from app.forms import *


class StartPageView(TemplateView):
    template_name = 'app/start_page.html'


class RegisterPageView(CreateView):
    template_name = 'app/register_page.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('start')


class LoginPageView(LoginView):
    template_name = 'app/login_page.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('start')


class LogoutPageView(LogoutView):
    next_page = reverse_lazy('start')


def main_page(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            auther = form.save(commit=False)
            auther.auther = request.user
            auther.save()
            BotMessage.objects.create(user=request.user,
                                      message=auther.message)
            return redirect('start')
    else:
        context = {'form': MessageForm(),
                   'users': UserMessage.objects.all(),
                   'bots': BotMessage.objects.all()}
        return render(request, 'app/start_page.html', context)
