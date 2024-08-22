from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from users.models import Subscription
from courses.models import Course, Group

@receiver(post_save, sender=Subscription)
def post_save_subscription(sender, instance: Subscription, created, **kwargs):
    """
    Распределение нового студента в группу курса.

    """

    if created:
        pass
        # TODO

@receiver(post_save, sender=Course)
def create_group(sender, instance, created, **kwargs):
    if created:
        for i in range(10):
            Group.objects.create(course=instance)
