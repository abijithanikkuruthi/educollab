from django.shortcuts import render, get_object_or_404
from app.models import Member, ChangeLog, Subscription, Subject
from .utils import check_user_id

def feed(request):
    current_user = Member.objects.filter(u_id=request.user.id).first()

    """
    Filtering feeds according to user's
    subscriptions.

    """
    user_subs = Subscription.objects.filter(member=current_user)
    changelogs = []
    for sub in user_subs:
        # for feeds related to subject
        if sub.curriculum is None:
            changelog = ChangeLog.objects.filter(subject=sub.subject)
            changelogs.extend(changelog)
        # for feeds related to curriculum 
        elif sub.subject is None:
            changelog = ChangeLog.objects.filter(curriculum=sub.curriculum)
            changelogs.extend(changelog)
        else:
            print("something really went wrong.")
            changelogs =[]
    
    # print(changelogs)
    # Only distinct feeds allowed
    changelogs = list(set(changelogs))
    
    context = {
        "changelogs": changelogs,
        "current_user": current_user,
    }
    return render(request, 'feeds/index.html', context)