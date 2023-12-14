from apps.helpers.models import TimeStamp
from apps.location.models import Division, District, UpazilaOrThana, UnionOrWard
from django.db import models

# Create your models here.
class Projects(TimeStamp):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    room = models.FloatField(default=0)
    area = models.PositiveIntegerField(default=0)
    floor = models.PositiveIntegerField(default=0, verbose_name='Total Floor')
    parking = models.BooleanField(default=True)
    lift = models.BooleanField(default=True)
    stair = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to='thumbnail', null=True, blank=True)

    
    # present address
    division = models.ForeignKey(Division, on_delete=SET_NULL, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=SET_NULL, null=True, blank=True)
    thana = models.ForeignKey(UpazilaOrThana, on_delete=SET_NULL, null=True, blank=True)
    union = models.ForeignKey(UnionOrWard, on_delete=SET_NULL, null=True, blank=True)

    address = models.TextField(blank=True, default='#')

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.title