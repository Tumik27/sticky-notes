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
    """Tests for all note views and core CRUD use cases."""

    def setUp(self):
        """Create a sample note for view testing."""
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test note.",
        )

    def test_note_list_view(self):
        """Ensure the note list view loads successfully and displays notes."""
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_note_detail_view(self):
        """Ensure the note detail view displays the correct note information."""
        response = self.client.get(reverse("note_detail", args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")
        self.assertContains(response, "This is a test note.")

    def test_note_create_view_get(self):
        """Ensure the create view page loads (GET)."""
        response = self.client.get(reverse("note_create"))
        self.assertEqual(response.status_code, 200)

    def test_note_create_view_post_creates_note(self):
        """Ensure posting to create view creates a new note (POST)."""
        response = self.client.post(
            reverse("note_create"),
            data={"title": "New Note", "content": "New content"},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Note.objects.filter(title="New Note").exists())

    def test_note_update_view_get(self):
        """Ensure the update view page loads (GET)."""
        response = self.client.get(reverse("note_update", args=[self.note.id]))
        self.assertEqual(response.status_code, 200)

    def test_note_update_view_post_updates_note(self):
        """Ensure posting to update view updates the note (POST)."""
        response = self.client.post(
            reverse("note_update", args=[self.note.id]),
            data={"title": "Updated Title", "content": "Updated content"},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated Title")
        self.assertEqual(self.note.content, "Updated content")

    def test_note_delete_view_get_redirects(self):
        """Ensure the delete view redirects on GET (no confirmation page)."""
        response = self.client.get(reverse("note_delete", args=[self.note.id]))
        self.assertEqual(response.status_code, 302)

    def test_note_delete_view_post_deletes_note(self):
        """Ensure posting to delete view deletes the note (POST)."""
        note_id = self.note.id
        response = self.client.post(
            reverse("note_delete", args=[note_id]),
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Note.objects.filter(id=note_id).exists())
