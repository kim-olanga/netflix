from django.contrib import admin
from .models import User,Profile,Movie,Video

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Movie)
admin.site.register(Video)
