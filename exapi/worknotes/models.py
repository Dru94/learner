from distutils.command.upload import upload
from django.db import models
from django.utils.text import slugify


# Create your models here.
TERM_CHOICES = [
    ('All', 'All'),
    ('One', 'One'),
    ('Two', 'Two'),
    ('Three', 'Three')
]

LEVEL_CHOICES = [
    ('Primary', 'Primary'),
    ('Senior', 'Senior')
]


class Notes(models.Model):
    subject = models.CharField(max_length=225, blank=False)
    topic = models.CharField(max_length=225, blank=False)
    level = models.CharField(
        max_length=9, choices=LEVEL_CHOICES, blank=False, default='')
    level_number = models.PositiveIntegerField(
        null=False, default=1, verbose_name='class')
    notes = models.FileField(upload_to='work/%Y/%m/%d/', null=False)
    subject_image = models.ImageField(
        upload_to='notes_image/%Y/%m/%d/', null=True)
    term = models.CharField(max_length=5, choices=TERM_CHOICES)
    slug = models.SlugField(null=False, unique=True, default="")

    def __str__(self):
        return self.subject + self.topic + ' Class: ' + str(self.level) + str(self.level_number)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.subject)

        return super().save(*args, **kwargs)

class Subjects(models.Model):
    title = models.CharField(max_length=225, blank=False, default='')
    level = models.CharField(max_length=225, default='', blank=False)
    class_number = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title