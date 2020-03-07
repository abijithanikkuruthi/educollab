from django.shortcuts import render, get_object_or_404
from app.models import Member, ChangeLog, Subscription, Subject


def showsubject(request, sid):

    # Shitty solution for now
    if not Subject.objects.filter(id=sid):
        return render(request, 'registration/login.html', {})

    subject = get_object_or_404(Subject, id=sid)

    user_subscription = Subscription.objects.filter(
        member=request.user.id, subject=subject, curriculum__isnull=True).exclude(subject__isnull=True)

    if request.method == 'GET':

        if user_subscription:
            button_status = 'Unsubscribe'
        else:
            button_status = 'Subscribe'

        context = {
            'subject': subject,
            'button_status': button_status,
        }
        return render(request, 'subject.html', context)

    if request.method == 'POST':
        """
        Filtering user subscription by only
        allowing records with subjects not
        being NULL and curriculums being NULL

        """
        if user_subscription:
            user_subscription.delete()

            # Updating Change Log for the change
            reason = 'Unsubscribed from ' + \
                str(subject) + ' + more details'
            log_obj = ChangeLog(
                member=Member(id=request.user.id),
                description=reason,
                curriculum=None,
                bit=None,
                subject=subject,
                operation=None,
            )
            log_obj.save()

            sub_status = 'Unsubscribed!'
            button_status = 'Subscribe'

        else:
            sub_obj = Subscription(
                member=Member(id=request.user.id),
                subject=subject,
                curriculum=None
            )
            sub_obj.save()

            # Updating Change Log for the change
            reason = 'Subscribed to ' + str(subject) + ' + more details'
            log_obj = ChangeLog(
                member=Member(id=request.user.id),
                description=reason,
                curriculum=None,
                bit=None,
                subject=subject,
                operation=None,
            )
            log_obj.save()

            sub_status = 'Subscribed!'
            button_status = 'Unsubscribe'

        context = {'subject': subject,
                   'sub_status': sub_status,
                   'button_status': button_status}
        return render(request, 'subject.html', context)
