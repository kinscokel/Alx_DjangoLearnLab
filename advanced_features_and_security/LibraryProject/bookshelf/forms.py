from django import forms
from .models import Book

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)


from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    """
    ExampleForm securely handles user input for the Book model.
    It uses Django's built-in validation to help prevent malicious input.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        # Additional sanitization or checks can be added here
        return title
