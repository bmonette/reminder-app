from django.db import models


class Reminder(models.Model):
    """A model representing a reminder with a text, due date, and a sent status."""

    reminder_text = models.TextField()
    due_date = models.DateField()
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return self.reminder_text
