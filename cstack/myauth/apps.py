import logging

from django.apps import AppConfig

logger = logging.getLogger(__name__)


class MyauthConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "myauth"

    def ready(self):
        logger.info("Signals are connected")
