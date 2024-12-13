from django.apps import AppConfig


class FsmtestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fsmtest'

    def ready(self):
        import fsmtest.receivers
