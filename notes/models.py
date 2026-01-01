from django.db import models


class Note(models.Model):
    """
    Model representing a sticky note.

    Fields:
    - title: Short title for the note
    - content: Main text of the note
    - created_at: Date and time when the note was created
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
