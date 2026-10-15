from django.apps import AppConfig


class CatalogoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' #1agregamos 1
    name = 'apps.catalogo'
    verbose_name = 'Catalogo de figuras' #|agregamos este  2 al igual que los otros apps
