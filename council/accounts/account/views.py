from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user  = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to a success page or dashboard
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form}) #delete this line after fin register.html