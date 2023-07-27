from django.db import models
from django.db.models import Q

   


class ModelQuerySet(models.QuerySet):
    def search(self, query=None, **kwargs):
        if query is None or query == "":
            return self.none()
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups)


class ModelManager(models.Manager):
    def get_queryset(self, query):
        return ModelManager(self.model, using=self._db)
    
    def search(self, query):
        return self.get_queryset().search(query=query)