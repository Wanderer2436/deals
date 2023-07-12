from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache

from core import models


@receiver(post_save, sender=models.Deal)
def deal_post_save_handler(sender, instance, **kwargs):  # noqa
    cache.clear()
