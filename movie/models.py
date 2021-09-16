import uuid
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Character(BaseModel):
    _id = models.CharField(max_length=100, db_index=True, unique=True)
    height = models.CharField(max_length=100, null=True, blank=True)
    race = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    birth = models.CharField(max_length=100, null=True, blank=True)
    spouse = models.CharField(max_length=100, null=True, blank=True)
    death = models.CharField(max_length=100, null=True, blank=True)
    realm = models.CharField(max_length=100, null=True, blank=True)
    hair = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, db_index=True)
    wikiUrl = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ("created", )

    def __str__(self):
        return self.name


class Quote(BaseModel):
    _id = models.CharField(max_length=100, db_index=True, unique=True)
    dialog = models.CharField(max_length=100)
    character = models.ForeignKey(Character, related_name='quote', on_delete=models.CASCADE)
    movie = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ("created", )

    def __str__(self):
        return self.dialog
