from django.shortcuts import render, get_object_or_404
from app.models import Member, ChangeLog, Subscription, Subject
from .utils import check_user_id

def feed(request):
    member = Member.objects.filter(u_id=request.user.id).first()

    changelogs = ChangeLog.objects.filter(member=member).order_by('-created_on')

    context = {
        "changelogs": changelogs,
        "current_user": member,
    }
    return render(request, 'feeds/index.html', context)