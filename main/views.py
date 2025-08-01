from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm 

def chat(request):
    
    messages = Message.objects.all()
    messageForm = MessageForm()
    
    if request.method == 'POST':
        messageForm = MessageForm(request.POST)
        if messageForm.is_valid():
            messageForm.save()
            return redirect('Chat')
    
    context = {
        'messages': messages,
        'form': messageForm,
    }
    
    return render(request, 'main/index.html', context)


# adminkan el kanes