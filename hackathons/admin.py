from django.contrib import admin
from .models import Hackathon, Judge, Prize, Sponsor, Criteria, Participant

# Register your models here.

admin.site.register([Hackathon, Judge, Prize, Sponsor, Criteria, Participant])
