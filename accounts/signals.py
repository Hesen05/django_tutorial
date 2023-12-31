from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from accounts.models import Profile


@receiver(post_save, sender = User)
def ProfileSave(sender, instance, created ,*args, **kwargs):
    if created:
        Profile.objects.create(user = instance)
