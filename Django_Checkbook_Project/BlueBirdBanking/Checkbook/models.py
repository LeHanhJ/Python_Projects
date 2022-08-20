from django.db import models

# Creates Account model
class Account(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2)

    #creates model manager
    Accounts = models.Manager()

    # Allows references  to a specific account be returned as the owner's name not the primary key
    def __str__(self):
        return self.first_name + ' ' + self.last_name

#Choices for a transaction
TransactionType = [('Deposit', 'Deposit'), ('Withdrawl', 'Withdrawl')]

# Creates the Transaction model
class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=10, choices=TransactionType)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    #Defines the model Manager for Transactions
    Transactions = models.Manager()






