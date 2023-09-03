from django import forms
from store.models import BookShopeModel




    

class BookShopeForm(forms.ModelForm):
    class Meta:
        model = BookShopeModel
        fields = ['id','book_name','author','category']
        