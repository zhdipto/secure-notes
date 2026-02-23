from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User, SecureNote
from .utils import decryptData, encryptData


def home(request):
    if request.method == "POST":
        fullName = request.POST.get('fullName')
        username = request.POST.get('userName')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return render(request, 'registration.html')

        newUser = User.objects.create_user(
            username=username,
            fullName=fullName,
        )
        newUser.set_password(password)
        newUser.save()

        messages.success(request, "Account created with encrypted data!")
        return redirect('login')

    return render(request, 'registration.html')

def loginCheck(request):
    if request.user.is_authenticated:
        return redirect('dashboard') 
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')
@login_required
def dashboard(request):
    notes = SecureNote.objects.filter(user=request.user).order_by('-created_at')

    decrypted_notes = []
    for note in notes:
        decrypted_notes.append({
            'id': note.id,
            'title': decryptData(note.title),
            'content': decryptData(note.encrypted_content),
            'created_at': note.created_at
        })

    return render(request, 'dashboard.html', {'notes': decrypted_notes})
    # return render(request, 'dashboard.html')


@login_required
def createNote(request):
    if request.method == "POST":
        title = encryptData(request.POST.get('title'))
        content = request.POST.get('content')

        if title and content:
            encrypted_content = encryptData(content)

            SecureNote.objects.create(
                user=request.user,
                title=title,
                encrypted_content=encrypted_content
            )

            messages.success(request, "Note saved securely!")
            return redirect('dashboard')

    return render(request, 'createNote.html')

def logoutView(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('home')

@login_required
def delete_note(request, pk):
    note = get_object_or_404(SecureNote, id=pk, user=request.user)
    note.delete()
    return redirect('dashboard')