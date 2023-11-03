from django.contrib import admin
from .models import *
@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'blood_group', 'phone_number', 'email', 'age', 'gender')
    list_filter = ('blood_group', 'gender')
    search_fields = ('name', 'email', 'phone_number')

@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'blood_group', 'location', 'age')
    list_filter = ('blood_group',)
    search_fields = ('patient_name', 'location')

