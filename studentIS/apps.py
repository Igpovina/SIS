from django.apps import AppConfig


class StudentisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'studentIS'
    def ready(self):
        import studentIS.signals