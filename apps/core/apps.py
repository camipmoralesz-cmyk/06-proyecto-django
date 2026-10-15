from django.apps import AppConfig


class CatalogoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' #1agregamos 1
    name = 'apps.core'
    verbose_name = 'Nucleo de sitio' #|agregamos este  2 al igual que los otros apps

