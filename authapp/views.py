from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth import login
from django.shortcuts import redirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            login(request, user)  # Log the user in after successful registration
            return redirect('blog/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    return render(request, 'login.html')
