from django.contrib.auth.models import User
from .models import Member, Subject, Comment, Bit, Curriculum, ChangeLog, Upvote
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404


def check_user_id(user):
    if not Member.objects.filter(u_id=user.id):
        m_obj = Member(
            u_id=user,
            username=user.username,
            email=user.email,
        )
        m_obj.save()
    return 1


def create_member_obj(user, u_id):
    m_obj = Member(
        u_id=User(id=u_id),
        username=user['username'],
        email=user['email'],
        full_name=user['first_name'] + ' ' + user['last_name'],
        institution=user['institution'],
        designation=user['designation']
    )
    m_obj.save()


def add_comment(request, c_type, c_id):

    current_user = get_object_or_404(Member, u_id=request.user)
    data = request.POST
    u_obj = Comment(
        member=current_user,
        comment=data["comment"]
    )
    if 'bit' in c_type:
        u_obj.bit = Bit(id=c_id)
    elif 'curriculum' in c_type:
        u_obj.curriculum = Curriculum(id=c_id)
    elif 'changelog' in c_type:
        u_obj.changelog = ChangeLog(id=c_id)

    u_obj.save()

    return redirect(request.META['HTTP_REFERER'])


def add_upvote(request, u_type, u_id):

    current_user = get_object_or_404(Member, u_id=request.user)
    data = request.POST
    u_obj = Upvote(
        member=current_user
    )
    if 'bit' in u_type:
        u_obj.bit = Bit(id=u_id)
    elif 'curriculum' in u_type:
        u_obj.curriculum = Curriculum(id=u_id)
    elif 'changelog' in u_type:
        u_obj.changelog = ChangeLog(id=u_id)

    u_obj.save()

    return redirect(request.META['HTTP_REFERER'])


def remove_upvote(request, u_type, u_id):

    current_user = get_object_or_404(Member, u_id=request.user)
    data = request.POST
    if 'changelog' in u_type:
        u_obj = Upvote.objects.filter(
            member=current_user, changelog=ChangeLog(id=u_id), bit=None, curriculum=None)
    elif 'bit' in u_type:
        u_obj = Upvote.objects.filter(member=current_user, bit=Bit(
            id=u_id), changelog=None, curriculum=None)
    elif 'curriculum' in u_type:
        u_obj = Upvote.objects.filter(
            member=current_user, bit=None, changelog=None, curriculum=Curriculum(id=u_id))

    u_obj.delete()

    return redirect(request.META['HTTP_REFERER'])
