from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, Book
from .forms import AuthorForm, BookForm
from .decorators import login_required_message

# Create your views here.
def home(request):
    return render(request,'books/index.html')



def bookstore(response):
    return HttpResponse("Hello, Bookstore")

def test_view(request):
    return HttpResponse("Hello, this is a test view to check Heroku deployment!")



def author_list(request):
    query = request.GET.get('q')
    if query:
        authors = Author.objects.filter(Q(name__icontains=query) | Q(biography__icontains=query)).order_by('name')
    else:
        authors = Author.objects.all().order_by('name')
    
    return render(request, 'books/author_list.html', {'authors': authors, 'query': query})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'books/author_detail.html', {'author': author})

@login_required_message
def author_create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Author created successfully')
            return redirect('author_list')
        else:
            messages.error(request, 'Failed to create author')
    else:
        form = AuthorForm()
    return render(request, 'books/author_form.html', {'form': form})

@login_required_message
def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, 'Author updated successfully')
            return redirect('author_list')
        else:
            messages.error(request, 'Failed to update author')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'books/author_form.html', {'form': form})

@login_required_message
def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        author.delete()
        messages.success(request, 'Author deleted successfully')
        return redirect('author_list')
    return render(request, 'books/author_confirm_delete.html', {'author': author})

def book_list(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query)).order_by('title')
    else:
        books = Book.objects.all().order_by('title')
    
    return render(request, 'books/book_list.html', {'books': books, 'query': query})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

@login_required_message
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book created successfully')
            return redirect('book_list')
        else:
            messages.error(request, 'Failed to create book')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

@login_required_message
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully')
            return redirect('book_list')
        else:
            messages.error(request, 'Failed to update book')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})

@login_required_message
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        messages.success(request, 'Book deleted successfully')
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})

