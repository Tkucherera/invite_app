from django.shortcuts import render


# Create your views here.
def home(request):
    if request.method == 'GET':
        color = request.GET.get('color')
        backcolor = request.GET.get('backcolor')
        return render(request, 'home.html', {'color': color, 'backcolor': backcolor})

    return render(request, 'home.html')
