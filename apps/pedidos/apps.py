from django.apps import AppConfig


class CatalogoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.pedidos'
    verbose_name = 'Pedidos del sitio' #|agregamos este  2 al igual que los otros apps
