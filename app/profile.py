from .models import Member, Curriculum, Bit, Upvote, Comment, ChangeLog
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm
from educollab import settings
import os

def view_profile(request, uname):
    member_details = get_object_or_404(Member, username=uname)
    user_details = get_object_or_404(User, username=uname)
    
    # TODO: (?) user curriculums need not be displayed in my profile - (my curricula shows it there)
    #
    # curriculums = Curriculum.objects.filter(posted_by=user_details.id)

    # c_list = []
    # for c in curriculums:
    #     bits = Bit.objects.filter(curriculum=c)
    #     b_list = []

    #     for b in bits:
    #         b_obj = b.__dict__
    #         b_obj["likes"] = len(Upvote.objects.filter(bit=b))
    #         b_obj["comments"] = len(Comment.objects.filter(bit=b))

    #         b_list.append(b_obj)

    #     c_obj = c.__dict__
    #     c_obj["b_list"] = b_list
        
    #     c_list.append(c_obj)

    changelogs = ChangeLog.objects.filter(member=user_details.id)

    for c in changelogs:
        c.likes = len(Upvote.objects.filter(changelog=c))
        c.comments = len(Comment.objects.filter(changelog=c))

    context = {
        'member' : member_details,
        'changelogs' : changelogs,
        'is_my_profile' : request.user.username==uname
    }
    return render(request, 'profile/index.html', context)

def file_upload(request):
    save_path = os.path.join(settings.MEDIA_ROOT, request.FILES['image'])
    path = default_storage.save(save_path, request.FILES['image'])
    return default_storage.path(path)

def edit_profile(request):
    u_id = request.user.id
    member_details = get_object_or_404(Member, u_id=u_id)
    user_details = get_object_or_404(User, id=u_id)

    if request.method == 'POST':
        data = request.POST

        member_details.full_name = data["full_name"]
        member_details.email = data["email"]
        member_details.institution = data["institution"]
        member_details.designation = data["designation"]

        if 'image' in request.FILES:
            member_details.image = request.FILES["image"]
        
        member_details.save()

        return redirect('my_profile')
        
    else:
        form = ProfileForm()

    context = {
        'form' : form
    }
    return render(request, 'profile/edit.html', context)