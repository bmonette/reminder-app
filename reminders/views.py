from django.shortcuts import render

from .models import Reminder

from .forms import ReminderForm


def reminder_list(request):
    reminders = Reminder.objects.all()

    context = {
        "reminders": reminders,
    }

    return render(request, "reminders/reminder_list.html", context)
