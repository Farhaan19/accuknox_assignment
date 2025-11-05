# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def slow_signal(sender, instance, **kwargs):
    print("Signal started...")
    time.sleep(3)
    print("Signal finished!")

# test.py
from django.contrib.auth.models import User
import time

start = time.time()
User.objects.create(username="signal_test")
end = time.time()

print(f"Execution time: {end - start:.2f} seconds")