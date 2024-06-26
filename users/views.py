# users/views.py

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sua conta foi criada com sucesso! Você já pode fazer login.')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



# users/views.py
from django.shortcuts import render

def login_view(request):
    # Lógica para exibir o formulário de login
    return render(request, 'login.html')  # Renderiza o template de login

def register_view(request):
    # Lógica para exibir o formulário de registro
    return render(request, 'registration/register.html')  # Renderiza o template de registro
