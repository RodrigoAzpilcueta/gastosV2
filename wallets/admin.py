from django.contrib import admin
from .models import Wallet

class WalletAdmin(admin.ModelAdmin):
    list_display = ('description',)
    fields = (('owner', 'name'),)
admin.site.register(Wallet, WalletAdmin)
