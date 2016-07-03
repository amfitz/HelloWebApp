from django.contrib import admin

from collection.models import Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Review, ReviewAdmin)
