from django.db import models
from django.utils.text import slugify


# Create your models here.
TERM_CHOICES = [
    ('one', 'one'),
    ('two', 'two'),
    ('three', 'three')
]

LEVEL_CHOICES = [
    ('primary', 'primary'),
    ('secondary', 'secondary')
]


class Notes(models.Model):
    subject = models.CharField(max_length=225, blank=False)
    topic = models.CharField(max_length=225, blank=False)
    level = models.CharField(
        max_length=9, choices=LEVEL_CHOICES, blank=False, default='')
    level_number = models.PositiveIntegerField(
        null=False, default=1, verbose_name='class')
    notes = models.FileField(upload_to='work/%Y/%m/%d/', null=False)
    term = models.CharField(max_length=5, choices=TERM_CHOICES)
    slug = models.SlugField(null=False, unique=True, default="")

    def __str__(self):
        return self.subject + self.topic + ' Class: ' + str(self.level) + str(self.level_number)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.subject)

        return super().save(*args, **kwargs)
