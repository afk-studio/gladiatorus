from django.contrib import admin

from .models import Match, StandaloneMatch
# Register your models here.
admin.site.register(Match)
admin.site.register(StandaloneMatch)