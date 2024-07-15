from django.db import models
import string
import random


def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Chat.objects.filter(code=code).count() == 0:
            break

    return code

# Create your models here.


class Chat(models.Model):
    chatId = models.TextField(default="", null=False)
    content = models.TextField(default="", null=False)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)