from django.db import models

class User(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

class Account(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=19, decimal_places=2)
    open_date = models.DateField

    def __str__(self):
        return f"Account from User: {self.user_id}"

class Card(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    cvv = models.CharField(max_length=3)

    def  __str__(self):
        return f"Card {self.name} from Account: {self.account_id}"