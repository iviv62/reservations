import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from .models import Account,Image,Clinic
from backend.settings import MEDIA_URL

class AccountType(DjangoObjectType):
    class Meta:
        model = Account
        fields = "__all__"
        convert_choices_to_enum = False
        
class ClinicType(DjangoObjectType):
    class Meta:
        model = Clinic
        convert_choices_to_enum = False
       
       

class ImageType(DjangoObjectType):

    class Meta:
        model=Image

    def resolve_image(self,info):
        if self.image:
            self.image = info.context.build_absolute_uri(self.image.url)
        return self.image
    
class Query(graphene.ObjectType):
    all_users=graphene.List(AccountType)
    user=graphene.Field(AccountType, id=graphene.Int())
    

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