from django.db import models
from django.contrib.auth.models import User

print(User)


# Create your models here.
def upload_update_image():
    # return True
    return "images/"


class Update(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image())
    sys_update_on = models.DateTimeField(auto_now=True)
    sys_created_on = models.DateTimeField(auto_now_add=True)
    parent_update = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    # def __str__(self):
    #     return self.content

