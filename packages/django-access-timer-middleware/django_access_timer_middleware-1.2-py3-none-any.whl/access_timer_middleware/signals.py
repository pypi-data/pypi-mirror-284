from django.conf import settings
from django.dispatch import receiver, Signal
from django.utils import timezone
from loguru import logger

user_logged_in_api = Signal()


@receiver(user_logged_in_api)
def update_last_access_time(sender, request, **kwargs):
    if settings.DEBUG:
        logger.debug('update_last_access_time')
        logger.debug(timezone.now().isoformat())
    current_time = timezone.now()
    request.session['last_access_time'] = current_time.isoformat()
