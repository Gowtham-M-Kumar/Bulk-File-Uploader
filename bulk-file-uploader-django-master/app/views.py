from django.shortcuts import render
from .models import Document
from django.contrib import messages

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        documents = request.FILES.getlist("documents")
        documents_list = [ Document(name=name, document=document) for document in documents]
        Document.objects.bulk_create(documents_list)

        messages.success(request, "Documents Uploaded")

    # Get recent documents for display
    recent_documents = Document.objects.all().order_by('-id')[:5]
    return render(request, "index.html", {'recent_documents': recent_documents})

def view_documents(request):
    documents = Document.objects.all().order_by('-id')
    return render(request, "view_documents.html", {'documents': documents})
