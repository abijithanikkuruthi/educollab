from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .utils import check_user_id, create_member_obj, add_comment
from .forms import SignUpForm
from app.models import Field, Subject, ChangeLog
from app import curriculum, subject, home, profile

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html', {})
    return home.feed(request)

def myprofile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return profile.view_profile(request, request.user.username)

def profile_edit(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return profile.edit_profile(request)

def profile_user(request, uname):
    if not request.user.is_authenticated:
        return redirect('login')
    return profile.view_profile(request, uname)

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            create_member_obj(request.POST, user.id)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def explore(request):
    fields = Field.objects.all()
    return render(request, 'explore.html', {"fields": fields})


def subject_index(request, sid):
    if not request.user.is_authenticated:
        return redirect('login')
    return subject.showsubject(request, sid)


def curriculum_index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return curriculum.indexcurriculum(request)


def curriculum_create(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return curriculum.createcurriculum(request)


def curriculum_show(request, c_id):
    if not request.user.is_authenticated:
        return redirect('login')
    return curriculum.showcurriculum(request, c_id)


def curriculum_update(request, c_id):
    if not request.user.is_authenticated:
        return redirect('login')
    return curriculum.updatecurriculum(request, c_id)


def curriculum_comment_create(request, c_id):
    if not request.user.is_authenticated:
        return redirect('login')
    return add_comment(request, "changelog", c_id)


def create_bit(request, c_id):
    if not request.user.is_authenticated:
        return redirect('login')
    return curriculum.createbit(request, c_id)


def update_bit(request, c_id, b_id):
    if not request.user.is_authenticated:
        return redirect('login')
    return curriculum.updatebit(request, c_id, b_id)


def comment(request, c_type, c_id):
    if not request.user.is_authenticated:
        return redirect('login')
    return add_comment(request, c_type, c_id)
