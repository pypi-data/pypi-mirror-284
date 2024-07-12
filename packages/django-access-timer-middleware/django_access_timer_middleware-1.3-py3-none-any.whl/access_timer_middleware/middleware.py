import re

from django.conf import settings
from django.utils import timezone
from django.http import JsonResponse
from .models import AccessTime
from .exceptions import FiltersConflictException


class AccessTimerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if hasattr(settings, 'RESTRICTED_PATHS') and hasattr(settings, 'EXCLUDED_PATHS'):
            raise FiltersConflictException(
                'Simultaneous existence of filters `EXCLUDED_PATHS` and `RESTRICTED_PATHS` is not allowed'
            )

        filter_path = None
        if settings.EXCLUDED_PATHS:
            filter_path = not any([pattern in request.path for pattern in settings.EXCLUDED_PATHS])
        elif settings.RESTRICTED_PATHS:
            filter_path = any([pattern in request.path for pattern in settings.RESTRICTED_PATHS])

        if filter_path:
            current_time = timezone.now()
            if request.session.get('last_access_time'):
                duration = settings.DEFAULT_DURATION \
                    if hasattr(settings, 'DEFAULT_DURATION') else AccessTime.load().duration.total_seconds()
                last_access_time = timezone.datetime.fromisoformat(request.session.get('last_access_time'))
                delta = (current_time - last_access_time).total_seconds()
                if delta > duration:
                    return JsonResponse({
                        'error': 'Access time expired'
                    }, status=403)

            request.session['last_access_time'] = current_time.isoformat()

        response = self.get_response(request)
        return response
