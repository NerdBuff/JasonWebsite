from django.db.models import Count
from django.shortcuts import render
from django.views.generic import DetailView, View
from .models import Book, Author


# Create your views here.
def list_books(request):
    """
    List the books that have reviews here
    """

    books = Book.objects.exclude(date_reviewed__isnull=True).prefetch_related('authors') #Note two underscores under referencing

    context={           #creates dictionary of authors to return to render function for template
        'books': books,
    }

    return render(request, "list.html", context) #return HttpResponse("We can put anything here") #This puts a simple HTML text in the page

class AuthorList(View):
    def get(self, request):

        authors = Author.objects.annotate(
            published_books=Count('books')
        ).filter(
            published_books__gt=0
        )

        context = {
            'authors': authors,

        }

        return render(request, "authors.html", context)

class BookDetail(DetailView):
    model = Book
    template_name = "book.html"

class AuthorDetail(DetailView):
    model = Author
    template_name = "author.html"
