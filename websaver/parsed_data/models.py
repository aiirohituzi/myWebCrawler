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

    solokd = models.CharField(max_length=5, null=True)
    duokd = models.CharField(max_length=5, null=True)
    squadkd = models.CharField(max_length=5, null=True)

    solofppkd = models.CharField(max_length=5, null=True)
    duofppkd = models.CharField(max_length=5, null=True)
    squadfppkd = models.CharField(max_length=5, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.userName