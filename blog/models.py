from django.db import models

# Create your models here.
class BlogModel(models.Model):
    bid = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=40)
    blog_content = models.CharField(max_length = 100 , default = None)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name 