from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfiles


@receiver(post_save, sender=User)   
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    print(created)
    if created:
        UserProfiles.objects.create(user=instance)
    else:
        try:
            profile = UserProfiles.objects.get(user=instance)
            profile.save()
        except:
            #Create the user profile if not exsits
            UserProfiles.objects.create(user=instance)

@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    pass

# post_save.connect(post_save_create_profile_receiver, sender=User)