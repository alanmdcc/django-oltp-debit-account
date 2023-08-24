from rest_framework.serializers import ModelSerializer

from debit_app.models import User, Account


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'