from django.db import models


class Mail(models.Model):
    message = models.TextField(max_length=1000)
    author = models.ForeignKey('account.Account')
    head = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, null=True)
    recipient = models.CharField(max_length=100)
