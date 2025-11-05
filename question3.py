# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction

@receiver(post_save, sender=User)
def check_transaction(sender, instance, **kwargs):
    print("Inside atomic block:", transaction.get_connection().in_atomic_block)
    
# test.py
from django.db import transaction
from django.contrib.auth.models import User

with transaction.atomic():
    User.objects.create(username="txn_check")

