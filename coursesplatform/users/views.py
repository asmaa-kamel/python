from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import StudentRegisterForm
from .models import Student


def register(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Student.objects.create(
                user=user,
                f_name=form.cleaned_data['first_name'],
                l_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                age=form.cleaned_data['age'],
            )
            return redirect('login')
    else:
        form = StudentRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('login')
    return render(request, 'users/logout.html')


@login_required
def profile(request):
    student = get_object_or_404(Student, user=request.user)
    enrollments = student.enrollment_set.all()

    return render(request, 'users/profile.html', {
        'student': student,
        'enrollments': enrollments,
    })