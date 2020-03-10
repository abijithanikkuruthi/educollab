from app.models import Field
from django.shortcuts import render


def showchoices(request):
    fields = Field.objects.all()

    context = {"fields": fields, }
    return render(request, 'explore.html', context)
