from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import Library

# Create your views here.
# Function based view
from django.shortcuts import render
from .models import Book, Library
from django.views.generic.detail import DetailView

def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})



# Class based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'


    from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


    from django.shortcuts import render, get_object_or_404
from .models import Library

def library_detail(request, pk):
    library = get_object_or_404(Library, pk=pk)
    return render(request, "relationship_app/library_detail.html", {"library": library})

    # relationship_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})



   # django-models/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def check_role(user, role_name):
    return hasattr(user, 'userprofile') and user.userprofile.role == role_name

def admin_check(user):
    return check_role(user, 'Admin')

def librarian_check(user):
    return check_role(user, 'Librarian')

def member_check(user):
    return check_role(user, 'Member')

@login_required
@user_passes_test(admin_check)
def admin_view(request):
    return render(request, 'admin_view.html')

@login_required
@user_passes_test(librarian_check)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@login_required
@user_passes_test(member_check)
def member_view(request):
    return render(request, 'member_view.html') 


    from django.shortcuts import render

def register(request):
    return render(request, 'register.html')  # Adjust template name as needed

from django.http import HttpResponse  

def home(request):
    message = "Welcome to the Library Project!"
    return HttpResponse(message)


from django.http import HttpResponse  

def home(request):
    message = "Welcome to the Library Project!"
    return HttpResponse(message)


from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def check_role(role):
    def check(user):
        return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role
    return check

@login_required
@user_passes_test(check_role('Admin'))
def admin_view(request):
    return render(request, 'admin_view.html')

@login_required
@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    return render(request, 'librarian_view.html')

@login_required
@user_passes_test(check_role('Member'))
def member_view(request):
    return render(request, 'member_view.html')


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})
