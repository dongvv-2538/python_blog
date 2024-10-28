from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .forms import UserForm
from django.utils.translation import gettext as _
import yaml

def i18n():
    with open('messages.yml', 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    if not request.user.is_staff and request.user != user:
        messages.error(request, i18n()['en']["accounts"]["forbidden"])
        return redirect('index')

    return render(request, 'accounts/user_detail.html', {'user': user})

def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if not request.user.is_staff and request.user != user:
        messages.error(request, i18n()['en']["accounts"]["forbidden"])
        return redirect('index')

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserForm(instance=user)

    return render(request, 'accounts/user_form.html', {'form': form})

def delete_confirm(request, pk):
    user = get_object_or_404(User, pk=pk)
    if not request.user.is_staff and request.user != user:
        messages.error(request, i18n()['en']["accounts"]["forbidden"])
        return redirect('index')

    return render(request, 'accounts/user_confirm_delete.html', {'user': user})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if not request.user.is_staff and request.user != user:
        messages.error(request, i18n()['en']["accounts"]["forbidden"])
        return redirect('index')

    if request.method == 'POST':
        user.delete()
        messages.success(request, i18n()['en']["accounts"]["deleted"])
        return redirect('index')

    return render(request, 'accounts/user_confirm_delete.html', {'user': user})
