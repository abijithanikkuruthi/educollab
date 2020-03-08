from django.shortcuts import render, get_object_or_404
from app.models import Member, ChangeLog, Subscription, Subject
from .utils import check_user_id
from itertools import chain


def feed(request):
    current_user = Member.objects.filter(u_id=request.user.id).first()

    """
    Filtering feeds according to user's
    subscriptions.

    """
    user_subs = Subscription.objects.filter(member=current_user)
    changelog_sub, changelog_curriculum = [], []

    for sub in user_subs:
        # for feeds related to subject
        if sub.curriculum is None:
            changelog_sub.extend(ChangeLog.objects.filter(subject=sub.subject))
        # for feeds related to curriculum
        elif sub.subject is None:
            changelog_curriculum.extend(
                ChangeLog.objects.filter(curriculum=sub.curriculum))
        else:
            print("No Changelog")
            changelogs = []

    # Only distinct feeds allowed
    changelogs = sorted(list(set(chain(changelog_sub, changelog_curriculum))),
                        key=lambda instance: instance.created_on, reverse=True)

    context = {
        "changelogs": changelogs,
        "current_user": current_user,
    }
    return render(request, 'feeds/index.html', context)
