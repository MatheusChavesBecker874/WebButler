from django.apps import AppConfig


class ProjetoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projeto'

class ProjetoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projeto'

    def ready(self):
        import projeto.signals