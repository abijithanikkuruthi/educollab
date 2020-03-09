from django.shortcuts import render, get_object_or_404
from app.models import Member, ChangeLog, Subscription, Subject, Upvote
from .utils import check_user_id
from itertools import chain


def feed(request):
    
    # Create user if not present - hacky hack
    check_user_id(request.user)
    current_user = get_object_or_404(Member, u_id=request.user)
    user_subs = Subscription.objects.filter(member=current_user)

    subbed_curriculums = []

    for sub in user_subs:
        # for feeds related to subject
        if sub.subject is not None:
            # add all curriculums that belong the subject
            subbed_curriculums.extend(sub.subject.curriculum.all())
                
        # for feeds related to curriculum
        elif sub.curriculum is not None:
            subbed_curriculums.append(sub.curriculum)
        else:
            print("No Changelog")
            changelogs = []

    # Get all changelogs to all 
    changelog_curriculum = ChangeLog.objects.filter(curriculum__in=subbed_curriculums)

    # TODO: Bit Updates by quering all bits are referenced by curriculums

    # Only distinct feeds allowed
    changelogs = sorted(list(set(chain(changelog_curriculum))),
                        key=lambda instance: instance.created_on, reverse=True)

    for c_log in changelogs:
            u_obj = Upvote.objects.filter(member=current_user, changelog=c_log, bit=None, curriculum=None)
            c_log.is_upvoted = len(u_obj) > 0

    context = {
        "changelogs": changelog_curriculum,
        "current_user": current_user,
        "member": current_user
    }
    return render(request, 'feeds/index.html', context)
