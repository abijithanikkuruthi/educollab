from django.shortcuts import render, redirect, get_object_or_404
from .forms import CurriculumForm, BitForm
from app.models import Field, Subject, Topic, Curriculum, Member, Bit, ChangeLog, Subscription, Teach
from .utils import check_user_id
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist


def subscription_index(request):
    current_user = get_object_or_404(Member, u_id=request.user.id)

    subs = Subscription.objects.filter(member=current_user)

    if request.method == 'GET':
        context = {'subscriptions': subs}
        return render(request, 'subscriptions/index.html', context)


def curriculum_subscription_create(request, cid):
    # commenting out for now for easier implementation
    # if request.method != 'POST':
    #     raise Http404("Invalid routing.")

    current_user = get_object_or_404(Member, u_id=request.user.id)
    curriculum = get_object_or_404(Curriculum, id=cid)

    try:
        subscription = Subscription.objects.get(
            member=current_user, curriculum=curriculum)
    except ObjectDoesNotExist:
        subscription = None

    if subscription != None:
        raise Http404("Subscription Already Exists.")

    sub_obj = Subscription(
        member=current_user,
        subject=None,
        curriculum=curriculum)
    sub_obj.save()

    # Updating Change Log for the change TODO: not sure about this
    reason = 'Subscribed to Curriculum ' + \
        str(curriculum.title) + ' + more details'
    # TODO Add stuff decoartate the objects curriculum + title
    # and all other stuff
    log_obj = ChangeLog(
        member=current_user,
        description=reason,
        curriculum=Curriculum(id=curriculum.id),
        bit=None,
        subject=None,
        operation=None,
    )
    log_obj.save()

    return redirect(request.headers['Referer'])


def subject_subscription_create(request, sid):
    if request.method != 'POST':
        raise Http404("Invalid routing.")

    current_user = get_object_or_404(Member, u_id=request.user.id)
    subject = get_object_or_404(Subject, id=sid)

    try:
        subscription = Subscription.objects.get(
            member=current_user, subject=subject)
    except ObjectDoesNotExist:
        subscription = None

    if subscription is not None:
        raise Http404("Subscription Already Exists.")

    subscription = Subscription(
        member=current_user,
        subject=subject,
        curriculum=None)
    subscription.save()

    # Updating Change Log for the change
    reason = 'Subscribed to ' + str(subject) + ' + more details'
    # TODO Add stuff decoartate the objects curriculum + title
    # and all other stuff
    log_obj = ChangeLog(
        member=current_user,
        description=reason,
        curriculum=None,
        bit=None,
        subject=subject,
        operation=None,
    )
    log_obj.save()

    return redirect(request.headers['Referer'])


def subscription_delete(request, sid):
    if request.method != 'POST':
        raise Http404("Invalid routing.")

    current_user = get_object_or_404(Member, u_id=request.user.id)
    subscription = get_object_or_404(Subscription, id=sid)

    if subscription.member != current_user:
        raise Http404("Invalid access.")

    if subscription.curriculum is not None:
        subObject = subscription.curriculum
    else:
        subObject = subscription.subject

    # Updating Change Log for the change
    reason = 'Unsubscribed from ' + \
        str(subObject) + ' + more details'
    # TODO Add stuff decoartate the objects curriculum + title
    # and all other stuff
    log_obj = ChangeLog(
        member=current_user,
        description=reason,
        curriculum=subscription.curriculum,
        bit=None,
        subject=subscription.subject,
        operation=None,
    )
    log_obj.save()

    subscription.delete()
    return redirect(request.headers['Referer'])
