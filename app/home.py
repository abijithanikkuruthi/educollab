from django.shortcuts import render, get_object_or_404
from app.models import Member, ChangeLog, Subscription, Subject, Upvote
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

        member = Member.objects.filter(u_id=current_user).first()

    # Only distinct feeds allowed
    changelogs = sorted(list(set(chain(changelog_sub, changelog_curriculum))),
                        key=lambda instance: instance.created_on, reverse=True)

    for c_log in changelogs:
            u_obj = Upvote.objects.filter(member=Member(id=request.user.id), changelog=c_log, bit=None, curriculum=None)
            c_log.is_upvoted = len(u_obj) > 0

    context = {
        "changelogs": changelogs,
        "current_user": current_user,
        "member": member
    }
    return render(request, 'feeds/index.html', context)
