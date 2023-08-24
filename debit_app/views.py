from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Account, Card
from .serializers import UserSerializer, AccountSerializer, CardSerializer


@api_view(['GET'])
def endpoints(_):
    data = ['/user', 'user/<int:id>', 'account/', 'account/int:id']
    return Response(data)


class UserView(APIView):

    def get(self, _):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = User.objects.create(
            age=request.data['age'],
            name=request.data['name']
        )
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)


class UserDetailView(APIView):

    def get_user(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def get(self, _, id):
        user = self.get_user(id=id)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    def put(self, request, id):
        user = self.get_user(id=id)
        user.age = request.data['age']
        user.name = request.data['name']
        user.save()
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    def delete(self, _, id):
        user = self.get_user(id=id)
        user.delete()
        return Response('User was deleted')


class AccountView(APIView):

    def validatePositiveBalance(self, balance):
        if float(balance) < 0:
            raise ParseError(detail="Balance must be positive")
        return balance

    def get(self, _):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, request):
        new_balance = self.validatePositiveBalance(request.data['balance'])
        try:
            account = Account.objects.create(
                user_id=User.objects.get(id=request.data['user_id']),
                balance=new_balance,
                open_date=request.data['open_date']
            )
        except User.DoesNotExist:
            raise Http404
        serializer = AccountSerializer(account, many=False)
        return Response(serializer.data)


class AccountDetailView(APIView):

    def validatePositiveBalance(self, balance):
        if (float(balance) < 0):
            raise ParseError(detail="Balance must be positive")
        return balance

    def get_account(self, id):
        try:
            return Account.objects.get(id=id)
        except Account.DoesNotExist:
            raise Http404

    def get_user(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def get(self, _, id):
        account = self.get_account(id=id)
        serializer = AccountSerializer(account, many=False)
        return Response(serializer.data)

    def put(self, request, id):
        new_balance = self.validatePositiveBalance(request.data['balance'])
        account = self.get_account(id=id)
        account.user_id = self.get_user(id=request.data['user_id'])
        account.balance = new_balance
        account.open_date = request.data['open_date']
        account.save()
        serializer = AccountSerializer(account, many=False)
        return Response(serializer.data)

    def delete(self, _, id):
        account = self.get_account(id=id)
        account.delete()
        return Response('Account was deleted')


class CardView(APIView):
    def get(self, _):
        accounts = Card.objects.all()
        serializer = CardSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            card = Card.objects.create(
                account_id=Account.objects.get(id=request.data['account_id']),
                name=request.data['name'],
                cvv=request.data['cvv']
            )
        except Account.DoesNotExist:
            raise Http404
        serializer = CardSerializer(card, many=False)
        return Response(serializer.data)


class CardDetailView(APIView):
    def get_card(self, id):
        try:
            return Card.objects.get(id=id)
        except Card.DoesNotExist:
            raise Http404

    def get_account(self, id):
        try:
            return Account.objects.get(id=id)
        except Account.DoesNotExist:
            raise Http404

    def get(self, _, id):
        account = self.get_card(id=id)
        serializer = CardSerializer(account, many=False)
        return Response(serializer.data)

    def put(self, request, id):
        card = self.get_card(id=id)
        card.account_id = Account.objects.get(id=request.data['account_id'])
        card.name = request.data['name']
        card.cvv = request.data['cvv']
        card.save()
        serializer = CardSerializer(card, many=False)
        return Response(serializer.data)

    def delete(self, _, id):
        card = self.get_card(id=id)
        card.delete()
        return Response('Card was deleted')
