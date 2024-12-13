from django.dispatch import receiver
from django_fsm import post_transition
from rest_framework.exceptions import ValidationError

from .models import Post, Transition_Logger


@receiver(sender=Post, signal=post_transition)
def status_transition_logger(**kwargs):
    try:
        log = Transition_Logger(post=kwargs['instance'], source=kwargs['source'], target=kwargs['target'])
        log.save()
    except:
        ValidationError('bad request')
