from django.shortcuts import render
from django.http import HttpResponse

from .models import Reminder


def reminder_list(request):
    reminders = Reminder.objects.all()

    return HttpResponse("Reminder App")
