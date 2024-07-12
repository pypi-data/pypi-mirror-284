from django.apps import AppConfig


class AccessTimerMiddlewareConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'access_timer_middleware'

    def ready(self):
        import access_timer_middleware.signals
