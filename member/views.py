from django.shortcuts import render


def index(request):
    """List all members
    """
    return render(request, 'member/index.html')
