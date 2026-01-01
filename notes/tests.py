"""Tests for the Sticky Notes application."""

from django.test import TestCase
from django.urls import reverse

from .models import Note


class NoteModelTest(TestCase):
    """Tests for the Note model fields and data integrity."""

    def setUp(self):
        """Create a sample note for model testing."""
        Note.objects.create(title="Test Note", content="This is a test note.")

    def test_note_has_title(self):
        """Ensure the note title is saved correctly."""
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, "Test Note")

    def test_note_has_content(self):
        """Ensure the note content is saved correctly."""
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, "This is a test note.")


class NoteViewTest(TestCase):
    """Tests for note list and detail views."""

    def setUp(self):
        """Create a sample note for view testing."""
        self.note = Note.objects.create(
            title="Test Note", content="This is a test note."
        )

    def test_note_list_view(self):
        """Ensure the note list view loads successfully and displays notes."""
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_note_detail_view(self):
        """Ensure the note detail view displays the correct note information."""
        response = self.client.get(reverse("note_detail", args=[str(self.note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")
        self.assertContains(response, "This is a test note.")
