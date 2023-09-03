from django import forms
from store.models import BookShopeModel



class ItemSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='Search Items')
    

class BookShopeForm(forms.ModelForm):
    class Meta:
        model = BookShopeModel
        fields = ['id','book_name','author','category']
        