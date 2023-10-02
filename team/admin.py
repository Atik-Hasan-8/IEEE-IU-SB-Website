from django.contrib import admin

# Register your models here.
from .models import Event,Team,Upcomming_event,Contact,ExCom

# admin.site.register(TeamMember)
admin.site.register(Event)
admin.site.register(Team)
admin.site.register(Upcomming_event)
admin.site.register(Contact)
admin.site.register(ExCom)