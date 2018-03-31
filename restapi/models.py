from django.db import models


class Invitation(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    sent = models.BooleanField(blank=True, default=False)
    address = models.CharField(max_length=256, blank=True)
    access_code = models.CharField(max_length=10, blank=True)
    ty_sent = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return 'id: {}, sent: {}, code: {}'.format(self.id, self.sent, self.access_code)


class Slider(models.Model):
    name = models.CharField(max_length=256, blank=False)
    description = models.CharField(max_length=1024, blank=False)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return 'id: {}, name: {}'.format(self.id, self.name)


class Guest(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    invitation = models.ForeignKey(Invitation, related_name='guests',
                                   on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    offered_plus_one = models.BooleanField(blank=True, default=False)
    bringing_plus_one = models.BooleanField(blank=True, default=False)
    attending = models.NullBooleanField(blank=True, default=None)
    invited_by = models.OneToOneField('self', on_delete=models.CASCADE, blank=True, null=True)
    sliders = models.ManyToManyField(Slider, related_name='guests')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return 'id: {}, {}, attending: {}'.format(self.id, self.name, self.attending)


class Gift(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    giver = models.ForeignKey(Invitation, related_name='gifts', on_delete=models.CASCADE)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return 'id: {}, {}, thank you: {}'.format(self.id, self.name, self.ty_sent)
