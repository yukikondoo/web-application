from django.contrib import admin
from first_app.models import AccesRecord, Topic, Webpage, NewAdmin, UserProfileInfor

# Register your models here.
admin.site.register(AccesRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(NewAdmin)
admin.site.register(UserProfileInfor)
