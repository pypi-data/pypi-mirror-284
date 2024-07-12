from django.db import models
from django.utils import timezone

from singleton.models import Singleton


# Create your models here.

class AccessTime(Singleton):
    ONE_HOUR = timezone.timedelta(hours=1)
    THREE_HOURS = timezone.timedelta(hours=3)
    TWELVE_HOURS = timezone.timedelta(hours=12)
    ONE_DAY = timezone.timedelta(days=1)
    TWO_WEEKS = timezone.timedelta(weeks=2)

    DURATION_CHOICES = (
        (ONE_HOUR, '1 hour'),
        (THREE_HOURS, '3 hours'),
        (TWELVE_HOURS, '6 hours'),
        (ONE_DAY, '1 day'),
        (TWO_WEEKS, '2 weeks'),
    )

    duration = models.DurationField(choices=DURATION_CHOICES, default=ONE_HOUR)

    def __str__(self):
        return f'{self.get_duration_display()} {self.duration}'
