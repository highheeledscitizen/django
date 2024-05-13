from django.shortcuts import render, redirect
from .models import Message
# Create your views here.


def home_page(request):
    return render(request, 'home_page.html')


def input_page(request):
    if request.method == 'POST':
        # save to session
        text = request.POST.get('text')
        if 'messages' not in request.session:
            messages = []
        else:
            messages = request.session['messages']
        messages.append(text)
        request.session['messages'] = messages

        # save to database
        message = Message(message_text=text)
        message.save()
        return redirect('input_list')

    return render(request, 'input_page.html')


def input_list(request):
    session_messages = request.session.get('messages', [])
    db_messages = Message.objects.all()
    return render(request, 'input_list.html', {'messages': session_messages, 'db_messages': db_messages})


