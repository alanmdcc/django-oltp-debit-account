from django.contrib import admin

from debit_app.models import User, Account, Card, Transaction

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Card)
admin.site.register(Transaction)
