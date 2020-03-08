from django.shortcuts import render, redirect, get_object_or_404
from .forms import CurriculumForm, BitForm
from app.models import Field, Subject, Topic, Curriculum, Member, Bit, ChangeLog, Subscription, Teach


def createcurriculum(request):

    # dropdown list to choose
    fields = Field.objects.all()
    topics = Topic.objects.all()
    subjects = Subject.objects.all()

    form_type = 'Create'

    if request.method == 'POST':
        data = request.POST
        c_obj = Curriculum(
            title=data['title'],
            subject=Subject(id=data['subjects']),
            description=data['description'],
            posted_by=Member(id=request.user.id)
        )

        c_obj.save()

        # Automatic subscribing to own made curriculum
        sub_obj = Subscription(
            member=Member(id=request.user.id),
            subject=None,
            curriculum=Curriculum(id=c_obj.id)
        )
        sub_obj.save()

        log_obj = ChangeLog(
            member=Member(id=request.user.id),
            description='New Curriculum Created + more details ',
            curriculum=Curriculum(id=c_obj.id),
            operation='create'
        )
        log_obj.save()

        # TODO Redirect with message - need to package
        context = {'success': 'Curriculum created!'}
        return redirect('curriculum_show', c_id=c_obj.id)
    else:
        form = CurriculumForm()
        context = {
            'form': form,
            'type': form_type,
            'fields': fields,
            'topics': topics,
            'subjects': subjects
        }
        return render(request, 'curriculum/create.html', context)


def indexcurriculum(request):

    curriculums = Curriculum.objects.filter(posted_by=request.user.id)
    if request.method == 'GET':
        context = {'curriculums': curriculums}
        return render(request, 'curriculum/index.html', context)


def showcurriculum(request, c_id):
    """
    Here we define all functionalities
    for each curriculum page.

    """

    # Current user
    current_user = Member(id=request.user.id)

    # Shitty solution for now
    if not Curriculum.objects.filter(id=c_id):
        return render(request, 'registration/login.html', {})

    # Fetch all records for curriculum with id=c_id
    curriculum = get_object_or_404(Curriculum, id=c_id)

    # Check if user is subscribed to the curriculum with id=c_id
    user_subscription = Subscription.objects.filter(
        member=request.user.id, curriculum=curriculum, subject__isnull=True).exclude(curriculum__isnull=True)

    # Fetch all curriculums taught by user for the subject of
    # current curriculum. (Shouldn't be more than 1)
    user_teach = Teach.objects.filter(
        member=request.user.id, subject=curriculum.subject)

    if request.method == 'POST' and '_subscribe' in request.POST:
        """
        Filtering user subscription by only
        allowing records with curriculums not
        being NULL and subjects being NULL

        """
         # Teach button
        if user_teach:
            if user_teach.first().curriculum.id == c_id:
                teach_button_status = 'UnTeach'
            else:
                teach_button_status = 'Teach'
        else:
            teach_button_status = 'Teach'

        context = {'curriculum': curriculum,
                   'sub_status': sub_status,
                   'subscribe_button_status': subscribe_button_status,
                   'teach_button_status': teach_button_status,}
        return render(request, 'curriculum/show.html', context)

    elif request.method == 'POST' and '_teach' in request.POST:
        """
        """
        if user_teach:
            if user_teach.first().curriculum.id == c_id:
                user_teach.delete()

                # Updating Change Log for the change
                reason = str(current_user) + 'is not teaching' + \
                    str(curriculum.title) + ' at their university - ' + \
                    str(current_user.institution) + 'anymore'

                log_obj = ChangeLog(
                    member=current_user,
                    description=reason,
                    curriculum=None,
                    bit=None,
                    subject=None,
                    operation=None,
                )
                log_obj.save()

                teach_status = 'Not Teaching Anymore!'
                teach_button_status = 'Teach'

            else:
                user_teach.delete()

                # Adding the curriculum for teaching
                teach_obj = Teach(
                    member=current_user,
                    curriculum=curriculum,
                    subject = curriculum.subject
                )
                teach_obj.save()

                # Updating Change Log for the change
                reason = str(current_user) + 'is teaching' + \
                    str(curriculum.title) + ' at their university - ' + \
                    str(current_user.institution)

                log_obj = ChangeLog(
                    member=current_user,
                    description=reason,
                    curriculum=None,
                    bit=None,
                    subject=None,
                    operation=None,
                )
                log_obj.save()

                teach_status = 'Teaching!'
                teach_button_status = 'UnTeach'

        else:
            # Adding the curriculum for teaching
            teach_obj = Teach(
                member=current_user,
                curriculum=curriculum,
                subject = curriculum.subject
            )
            teach_obj.save()

            # Updating Change Log for the change
            reason = str(current_user) + 'is teaching' + \
                str(curriculum.title) + ' at their university - ' + \
                str(current_user.institution)

            log_obj = ChangeLog(
                member=current_user,
                description=reason,
                curriculum=None,
                bit=None,
                subject=None,
                operation=None,
            )
            log_obj.save()

            teach_status = 'Teaching!'
            teach_button_status = 'UnTeach'

        # Subscribe button
        if user_subscription:
            subscribe_button_status = 'Unsubscribe'
        else:
            subscribe_button_status = 'Subscribe'

        context = {'curriculum': curriculum,
                'teach_status': teach_status,
                'teach_button_status': teach_button_status,
                'subscribe_button_status': subscribe_button_status,}
        return render(request, 'curriculum/show.html', context)

    else:
        """
        Assuming the other request would be
        GET request to load the page, placeholder
        text for button can be set

        """

        # Teach button
        if user_teach:
            if user_teach.first().curriculum.id == c_id:
                teach_button_status = 'UnTeach'
            else:
                teach_button_status = 'Teach'
        else:
            teach_button_status = 'Teach'

        context = {'curriculum': curriculum,
                   'user_subscription': user_subscription.first(),
                   'teach_button_status': teach_button_status,}
        return render(request, 'curriculum/show.html', context)


def updatecurriculum(request, c_id):
    # dropdown list menu to choose
    fields = Field.objects.all()
    topics = Topic.objects.all()
    subjects = Subject.objects.all()

    curriculum = get_object_or_404(Curriculum, id=c_id)
    form_type = 'Update'

    if request.method == 'POST':
        data = request.POST

        curriculum.title = data["title"]
        curriculum.subject = Subject(id=data['subjects'])
        curriculum.description = data['description']

        curriculum.save()
        log_obj = ChangeLog(
            member=Member(id=request.user.id),
            description='Curriculum Updated + more details ',
            curriculum=Curriculum(id=curriculum.id),
            operation='update'
        )
        log_obj.save()

        context = {'success': 'Curriculum !'}
        # TODO Redirect with message - need to package
        context = {'success': 'Curriculum updated!'}
        return redirect('curriculum_show', c_id=curriculum.id)
    else:

        form = CurriculumForm(data=curriculum.__dict__)
        context = {
            'form': form,
            "curriculum": curriculum,
            'type': form_type,
            'fields': fields,
            'topics': topics,
            'subjects': subjects
        }
        return render(request, 'curriculum/update.html', context)

# def file_upload(request):
#     save_path = os.path.join(settings.MEDIA_ROOT, request.FILES['file'])
#     path = default_storage.save(save_path, request.FILES['file'])
#     return default_storage.path(path)


def createbit(request, c_id):
    curriculum = get_object_or_404(Curriculum, id=c_id)
    form_type = 'Create'
    if request.method == 'POST':
        data = request.POST
        # TODO: fileupload
        # file_upload(request)
        b_obj = Bit(
            title=data["title"],
            bit_type=data["bit_type"],
            description=data["description"],
            text=data["text"],
            curriculum=Curriculum(id=c_id),
            file=data["file"]
        )
        b_obj.save()
        log_obj = ChangeLog(
            member=Member(id=request.user.id),
            description='Bit Added + more details ',
            bit=Bit(id=b_obj.id),
            operation='create'
        )
        log_obj.save()
        context = {
            'success': 'Bit Added!'
        }
        return render(request, 'bit-form.html', context)
    else:
        form = BitForm()
        context = {
            'curriculum': curriculum,
            'form': form,
            'type': form_type
        }
        return render(request, 'bit-form.html', context)


def updatebit(request, c_id, b_id):
    curriculum = get_object_or_404(Curriculum, id=c_id)
    bit = get_object_or_404(Bit, id=b_id)
    form_type = 'Update'
    if request.method == 'POST':
        data = request.POST
        # TODO: fileupload
        # file_upload(request)

        bit.title = data["title"],
        bit.bit_type = data["bit_type"],
        bit.description = data["description"],
        bit.text = data["text"],
        bit.curriculum = Curriculum(id=c_id)
        bit.file = data["file"]

        bit.save()

        log_obj = ChangeLog(
            member=Member(id=request.user.id),
            description='Bit Updated + more details ',
            bit=Bit(id=bit.id),
            operation='update'
        )
        log_obj.save()

        context = {
            'success': 'Bit Updated!'
        }
        return render(request, 'bit-form.html', context)
    else:
        form = BitForm(data=bit.__dict__)
        context = {
            'curriculum': curriculum,
            'form': form,
            'type': form_type
        }
        return render(request, 'bit-form.html', context)
