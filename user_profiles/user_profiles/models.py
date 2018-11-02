from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# from user_profiles.models import User
# from user_profiles.models import Profile
#python manage.py migrate --run-syncdb

class Profile(models.Model):
    name =  models.TextField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(name="officer",user=instance)
        Profile.objects.create(name="admin",user=instance)