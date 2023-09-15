from django.contrib import admin
from .models import LynkLocal, Contact_Form_Submission
# Register your models here.
admin.site.register(LynkLocal)
admin.site.register(Contact_Form_Submission)

admin.site.site_header = 'LynkLocal Admin'
admin.site.site_title = 'LynkLocal Admin Panel'
admin.site.index_title = 'Welcome to LynkLocal Admin'

