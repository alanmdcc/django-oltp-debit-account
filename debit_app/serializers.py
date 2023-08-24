from rest_framework.serializers import ModelSerializer

from debit_app.models import User, Account, Card


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'
