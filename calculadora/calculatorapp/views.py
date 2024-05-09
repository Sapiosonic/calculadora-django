from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def resultado(request):
    numero_1 = int(request.GET.get('numero_1'))
    numero_2 = int(request.GET.get('numero_2'))
    
    if request.GET.get('add') == "":
        resposta = numero_1 + numero_2
    elif request.GET.get('subtract') == "":
        resposta = numero_1 - numero_2 
    elif request.GET.get('multiply') == "":
        resposta = numero_1 * numero_2
    else:
        resposta = numero_1 / numero_2
        
    return render(request, 'resultado.html', {'resposta': resposta})
        