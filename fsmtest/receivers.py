from django_fsm import post_transition, pre_transition
from django.dispatch import receiver
from .models import Post, Transition_Logger
from rest_framework.exceptions import ValidationError


@receiver(sender=Post, signal=post_transition)
def status_transition_logger(**kwargs):
    try:
        log = Transition_Logger(post=kwargs['instance'],source=kwargs['source'],target=kwargs['target'])
        log.save()
    except:
        ValidationError('bad request')
   