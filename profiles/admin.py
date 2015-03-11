from django.contrib import admin
from profiles.models import Politician, UserProfile

# Register your models here.
admin.site.register(Politician)
admin.site.register(UserProfile)