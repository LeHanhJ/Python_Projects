from django.forms import ModelForm
from .models import Account, Transaction


# Creates Account Form based on Account model
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


# Creates Transaction Form based on Transaction model
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
