from django.shortcuts import render, get_object_or_404
from app.models import Member, ChangeLog, Subscription, Subject, Upvote
from .utils import check_user_id
from itertools import chain


def feed(request):

    # Create user if not present - hacky hack
    check_user_id(request.user)
    current_user = get_object_or_404(Member, u_id=request.user)
    user_subs = Subscription.objects.filter(member=current_user)

    total_subbed_curriculums = []
    curriculums_for_subbed_subjects = []
    subbed_curriculums = []

    for sub in user_subs:
        # for feeds related to subject
        if sub.subject is not None:
            # add all curriculums that belong the subject

            curriculums_for_subject = sub.subject.curriculum.all()
            curriculums_for_subbed_subjects.extend(curriculums_for_subject)
            total_subbed_curriculums.extend(curriculums_for_subject)

        # for feeds related to curriculum
        elif sub.curriculum is not None:
            subbed_curriculums.append(sub.curriculum)
            total_subbed_curriculums.append(sub.curriculum)
        else:
            print("No Changelog")
            changelogs = []

    # Get all changelogs to all 
    changelog_curriculum = ChangeLog.objects.filter(curriculum__in=total_subbed_curriculums).order_by('-created_on')

    # TODO: Bit Updates by quering all bits are referenced by curriculums
    # ANSWER: No need to^. I have updated the changelog such that querying for curriculum also fetch bit updates ;)

    for c_log in changelog_curriculum:
            u_obj = Upvote.objects.filter(member=current_user, changelog=c_log, bit=None, curriculum=None)
            c_log.is_upvoted = len(u_obj) > 0

    # Top 10 upvoted curriculum suggestions (excluding already followed curriculums)
    suggested_curriculums = list(set(curriculums_for_subbed_subjects) - set(subbed_curriculums)) 
    upvote_count = dict((curriculum, Upvote.objects.filter(curriculum=curriculum).count()) for curriculum in suggested_curriculums)
    sorted_suggested_curriculums = sorted(upvote_count.items(), key=lambda upvote: upvote[1], reverse=True)

    context = {
        "changelogs": changelog_curriculum,
        "current_user": current_user,
        "member": current_user,
        "suggestions":sorted_suggested_curriculums,
    }
    return render(request, 'feeds/index.html', context)
