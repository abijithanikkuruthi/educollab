from django.shortcuts import render, get_object_or_404
from app.models import Member, Subscription, Subject, Upvote, Curriculum, Contributor, Field


def subject_show(request, sid):
    # Shitty solution for now
    if not Subject.objects.filter(id=sid):
        return render(request, 'registration/login.html', {})

    # Fetching the current user and subject for associated sid
    current_user = get_object_or_404(Member, u_id=request.user)
    subject = get_object_or_404(Subject, id=sid)

    # 1. Fetching list of curriculums for the subject
    # 2. Fetch upvote count for all curriculums and store as a dictionary
    # 3. Sort the curriculums according to no. of upvotes
    curriculums = Curriculum.objects.filter(subject=subject)
    upvote_count = dict((curriculum, Upvote.objects.filter(
        curriculum=curriculum).count()) for curriculum in curriculums)
    sorted_curriculums = sorted(
        upvote_count.items(), key=lambda upvote: upvote[1], reverse=True)

    # Fetching number of contributors for every curriculum
    contributors = dict((curriculum, Contributor.objects.filter(curriculum=curriculum).count(
    )) if Contributor.objects.filter(curriculum=curriculum) else (curriculum, 0) for curriculum in upvote_count.keys())
    print(contributors)

    # Check if user is subscribed to the subject
    user_subscription = Subscription.objects.filter(
        member=current_user, subject=subject, curriculum__isnull=True).exclude(subject__isnull=True)
    
    if request.method == 'GET':
        
        for curriculum_obj in sorted_curriculums:
            # TODO: here instead of the names, i need the actual objects
            u_obj = Subscription.objects.filter(member=current_user, curriculum=curriculum_obj[0]).first()
            curriculum_obj[0].user_subscription = u_obj

        context = {
            'subject': subject,
            'sorted_curriculums': sorted_curriculums,
            'user_subscription': user_subscription.first(),
            'contributors': contributors,
        }
        return render(request, 'subject/show.html', context)

def subject_index(request):
    fields = Field.objects.all()

    context = {"fields": fields, }
    return render(request, 'explore.html', context)

