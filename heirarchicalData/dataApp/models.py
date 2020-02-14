from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User

class File(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    folder = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name