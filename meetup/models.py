from django.db import models


class Talk(models.Model):
    title = models.CharField(max_length=255)
    talker = models.ForeignKey('Talker')
    slides = models.FileField(upload_to='media/slides/', null=True, blank=True)

    def __unicode__(self):
        return self.title


class Talker(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Meetup(models.Model):
    talks = models.ManyToManyField('Talk')
    place = models.ForeignKey('Place')
    datetime = models.DateTimeField()

    def __unicode__(self):
        return str(self.datetime) + ' @ ' + str(self.place)
