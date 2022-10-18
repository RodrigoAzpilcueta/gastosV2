from django.db import models
from profiles.models import Profile
from django.contrib import admin

class Wallet(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='wallets')

    @admin.display(description="description")
    def description(self):
        return f'{self.owner} -> {self.name}'

    def __str__(self):
        return  self.name
