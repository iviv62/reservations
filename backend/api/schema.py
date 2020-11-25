import graphene
from graphene_django import DjangoObjectType
from .models import Account,Image

class AccountType(DjangoObjectType):
    class Meta:
        model = Account
        fields = "__all__"
        #continue adding 