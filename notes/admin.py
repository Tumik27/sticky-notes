from django.contrib import admin
from .models import Note

# I register the Note model so I can manage notes via the admin panel.
admin.site.register(Note)
