from django.contrib import admin
from .models import Account,Image,Reservation,Clinic,Holiday,TimeSlot



class InLineImage(admin.StackedInline):
    model=Image
    
class InLineTimeSlot(admin.StackedInline):
    model=TimeSlot



class AccountAdmin(admin.ModelAdmin):
    inlines=[InLineImage,InLineTimeSlot]
    list_display=("username",'email',"first_name","last_name","last_login","phone")
    list_filter=('is_admin',"is_doctor","date_joined","last_login")
    search_fields = ("username",'email',"first_name","last_name","last_login","phone")

admin.site.register(Account,AccountAdmin)
admin.site.register(Reservation)
admin.site.register(Clinic)

admin.site.register(Holiday)