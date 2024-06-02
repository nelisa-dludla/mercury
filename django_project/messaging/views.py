from django.shortcuts import render

messages = [
        {
            'sender': 'Nelisa Dludla',
            'content': 'Hello, World!',
            'date_sent': 'June 1, 2024'
        },
        {
            'sender': 'Jane Doe',
            'content': 'Learning Django',
            'date_sent': 'May 30, 2024'
        }
]

def home(request):
    context = {
            'messages': messages
    }

    return render(request, 'messaging/home.html', context)

def about(request):
    return render(request, 'messaging/about.html', {'title': 'About'})
