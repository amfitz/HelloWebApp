from django.forms import ModelForm
from collection.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'description',)
