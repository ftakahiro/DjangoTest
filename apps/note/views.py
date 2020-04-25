from django.shortcuts import render
from django.http      import HttpResponse
from . models         import Note

# Create your views here.

def index(request):
    notes=Note.objects.all()
    context={
        'notes':notes,
    }
    return render(request,'note/note_list.html',context)

def detail(request,note_id):
    try:
        note=Note.objects.get(id=note_id)
    except Note.DeosNoteExist:
        note=None
    
    context={
        'note':note
    }
    return render(request,'note/note_detail.html',context)

def create(request):
    if request.method=='POST':
        note=Note()
        note.title=request.POST['title']
        note.content=request.POST['content']
        note.save()
        return index(request)
    elif request.method=='GET':
        return render(request,'note/note_create.html')


def edit(request,note_id):
    if request.method == 'POST':
        note=Note.objects.get(id=note_id)
        note.title=request.POST['title']
        note.content=request.POST['content']
        note.save()
        return index(request)
    elif request.method == 'GET':
        note=Note.objects.get(id=note_id)
        context={
            'note':note
        }
        return render(request,'note/note_edit.html',context)

def delete(request,note_id):
     note=Note.objects.filter(id=note_id).delete()
     return index(request)
