from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """
    I use this form to create and update sticky notes.
    """

    class Meta:
        model = Note
        fields = ["title", "content"]
