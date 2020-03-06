from django.contrib.auth.models import User
from .models import Member, Subject, Comment, Bit, Curriculum, ChangeLog
from django.shortcuts import render, redirect

def check_user_id(user):
    if not Member.objects.filter(u_id=user.id):
        m_obj = Member(
            u_id = user,
            username = user.username,
            email = user.email, 
        )
        m_obj.save()
    return 1

def create_member_obj(user, u_id):
    m_obj = Member(
        u_id = User(id=u_id),
        username = user['username'],
        email = user['email'],
        full_name = user['first_name'] + ' ' + user['last_name'],
        institution = user['institution'],
        designation = user['designation']
    )
    m_obj.save()

def add_comment(request, c_type, c_id):

    data = request.POST
    u_obj = Comment(
        member = Member(id=request.user.id),
        comment = data["comment"]
    )
    if 'bit' in c_type:
        u_obj.bit = Bit(id=c_id)
    elif 'curriculum' in c_type:
        u_obj.curriculum = Curriculum(id=c_id)
    elif 'changelog' in c_type:
        u_obj.changelog = ChangeLog(id=c_id)

    u_obj.save()

    return redirect(request.META['HTTP_REFERER'])