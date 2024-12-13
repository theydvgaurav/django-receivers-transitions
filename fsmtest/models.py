from django.db import models
from django_fsm import FSMField, transition


class Post(models.Model):
    name = models.CharField(max_length=50)
    status = FSMField(default='unverified', protected=True)

    @transition(field=status, source="unverified", target="verified")
    def verified_status_transition(self):
        print("Transition happened from unverified state to verified state")

    @transition(field=status, source="verified", target="unverified")
    def unverified_status_transition(self):
        print("Transition happened from verified state to unverified state")


class Transition_Logger(models.Model):
    source = models.CharField(max_length=50)
    target = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
