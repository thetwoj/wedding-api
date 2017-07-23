from django.db import models


class Invitation(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    sent = models.BooleanField(blank=True, default=False)
    address = models.CharField(max_length=256, blank=True)
    access_code = models.CharField(max_length=10, blank=False)


class Guest(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    invitation = models.ForeignKey(Invitation, related_name='guests',
                                   on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    offered_plus_one = models.BooleanField(blank=True, default=False)
    bringing_plus_one = models.BooleanField(blank=True, default=False)
    attending = models.NullBooleanField(blank=True, default=None)
    food_choice = models.IntegerField(null=True, blank=True, default=None)

    class Meta:
        ordering = ('name',)
