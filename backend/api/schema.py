import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from .models import Account,Image,Clinic,AccountInfoField,Holiday,Reservation
from backend.settings import MEDIA_URL
from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField

class AccountType(DjangoObjectType):
    class Meta:
        model = Account
        interfaces = (Node,)
        filter_fields = {
            'specialty': ['exact', 'icontains', 'istartswith'],
            'city': ['icontains'],
        }
        convert_choices_to_enum = False
        
    
        
class ClinicType(DjangoObjectType):
    class Meta:
        model = Clinic
        convert_choices_to_enum = False
        
class InfoFieldType(DjangoObjectType):
    class Meta:
        model = AccountInfoField
        
class HolidayType(DjangoObjectType):
    class Meta:
        model = Holiday
        
class ReservationType(DjangoObjectType):
    class Meta:
        model = Reservation

class ImageType(DjangoObjectType):

    class Meta:
        model=Image

    def resolve_image(self,info):
        if self.image:
            self.image = info.context.build_absolute_uri(self.image.url)
        return self.image
    
class Query(graphene.ObjectType):
    all_users=graphene.List(AccountType)
    #user=graphene.Field(AccountType, id=graphene.Int())
    all_users=DjangoFilterConnectionField(AccountType)
    user = Node.Field(AccountType)
    

    def resolve_all_users(self,info,**kwargs):
        return Account.objects.all()
    
    def resolve_all_user_images(self,info,**kwargs):
        return Image.objects.all()
    
    def resolve_all_clinics(self,info,**kwargs):
        return Clinic.objects.all()
    

    def resolve_user(self,info,**kwargs):
        id=kwargs.get("id")
        if id is not None:
            return Account.objects.get(id=id)