from django.contrib import admin
from api.models import CreditCardUser, Advantage, Rewiew, Faq, CreditRequest,CreditRequestStatus

# Register your models here.
admin.site.register(CreditCardUser) 
admin.site.register(Advantage) 
admin.site.register(Rewiew) 
admin.site.register(Faq) 
#admin.site.register(CreditRequestStatus) 

@admin.register(CreditRequest)
class CreditRequestAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CreditRequest._meta.get_fields()]