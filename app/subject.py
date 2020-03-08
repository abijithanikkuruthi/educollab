from django.shortcuts import render, get_object_or_404
from app.models import Member, ChangeLog, Subscription, Subject


def showsubject(request, sid):

    current_user = get_object_or_404(Member, u_id=request.user)

    # Shitty solution for now
    if not Subject.objects.filter(id=sid):
        return render(request, 'registration/login.html', {})

    subject = get_object_or_404(Subject, id=sid)

    user_subscription = Subscription.objects.filter(
        member=current_user, subject=subject, curriculum__isnull=True).exclude(subject__isnull=True)

    if request.method == 'GET':
        context = {
            'subject': subject,
            "user_subscription": user_subscription.first(),
        }
        return render(request, 'subject.html', context)
