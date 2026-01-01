from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def note_list(request):
    """
    I use this view to display all sticky notes.
    """
    notes = Note.objects.all()

    context = {
        "notes": notes,
        "page_title": "My Sticky Notes",
    }

    return render(request, "notes/note_list.html", context)


def note_detail(request, pk):
    """
    I use this view to display the details of a single note.
    """
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


def note_create(request):
    """
    I use this view to create a new sticky note.
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm()

    return render(request, "notes/note_form.html", {"form": form})


def note_update(request, pk):
    """
    I use this view to update an existing sticky note.
    """
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm(instance=note)

    return render(request, "notes/note_form.html", {"form": form})


def note_delete(request, pk):
    """
    I use this view to delete a sticky note.
    """
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect("note_list")
