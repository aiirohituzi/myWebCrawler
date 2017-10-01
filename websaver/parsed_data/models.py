from django.db import models

# Create your models here.
class RatingData(models.Model):
    userName = models.CharField(max_length=30)
    solofpp = models.CharField(max_length=5, null=True)
    duofpp = models.CharField(max_length=5, null=True)
    squadfpp = models.CharField(max_length=5, null=True)
    solo = models.CharField(max_length=5, null=True)
    duo = models.CharField(max_length=5, null=True)
    squad = models.CharField(max_length=5, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.userName