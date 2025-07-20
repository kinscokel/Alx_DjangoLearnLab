from django.apps import AppConfig


class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'


    # django-models/apps.py

from django.apps import AppConfig

class DjangoModelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django-models'

    def ready(self):
        import django_models.signals
