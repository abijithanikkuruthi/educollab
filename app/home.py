from django.shortcuts import render, get_object_or_404
from app.models import Member, ChangeLog, Subscription, Subject, Upvote
from .utils import check_user_id

def feed(request):
    current_user = request.user
    if current_user.id:
        check_user_id(current_user)

        member = Member.objects.filter(u_id=current_user).first()

        # TODO: filter only based on subscriptiuos of user
        changelogs = ChangeLog.objects.filter(member=member)
        
        for c_log in changelogs:
            u_obj = Upvote.objects.filter(member=Member(id=request.user.id), changelog=c_log, bit=None, curriculum=None)
            c_log.is_upvoted = len(u_obj) > 0

        #print(changelogs)
        context = {
            "changelogs": changelogs,
            "current_user": current_user
        }
        return render(request, 'feeds/index.html', context)
    else:
        return render(request, 'index.html', {})