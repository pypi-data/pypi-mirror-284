from django.db import models


# Create your models here.

class Singleton(models.Model):
    class Meta:
        abstract = True

    @classmethod
    def load(cls):
        instance, created = cls.objects.get_or_create(pk=1)
        return instance

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    def __str__(self):
        return self.__class__.__name__
