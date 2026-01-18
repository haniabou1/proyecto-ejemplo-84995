from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {"form": form})

@login_required
def profile_view(request):
    return render(request, "accounts/profile.html")

@login_required
def profile_edit_view(request):
    user_form = UserUpdateForm(request.POST or None, instance=request.user)
    profile_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profile)

    if request.method == "POST":
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")

    return render(request, "accounts/profile_edit.html", {"user_form": user_form, "profile_form": profile_form})

class CustomPasswordChangeView(PasswordChangeView):
    template_name = "registration/password_change_form.html"
    success_url = reverse_lazy("password_change_done")
