# signals.py
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def check_thread(sender, instance, **kwargs):
    print("Signal thread ID:", threading.get_ident())

# test.py
import threading
from django.contrib.auth.models import User

print("Caller thread ID:", threading.get_ident())
User.objects.create(username="thread_check")
