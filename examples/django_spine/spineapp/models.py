from django.db import models
from django.utils.timezone import now
from bpmappers.djangomodel import ModelMapper


class Example(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    message = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )

#    @models.permalink
#    def get_absolute_url(self):
#        return ('tester_example_detail', (), {'pk': self.pk})


class ExampleMapper(ModelMapper):
    class Meta:
        model = Example