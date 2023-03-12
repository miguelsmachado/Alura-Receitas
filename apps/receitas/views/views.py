from django.shortcuts import render, get_object_or_404, redirect
from receitas.models import Receitas
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def index(request):
    receitas = Receitas.objects.order_by('-data').filter(publicada=True)

    paginator = Paginator(receitas, 1)
    page = request.GET.get('page')
    lista_receitas = paginator.get_page(page)


    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'receitas/index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)

    dados = {
        'receita': receita
    }
    return render(request, 'receitas/receita.html', dados)


def busca(request):
    nome_a_buscar = request.GET['search'].strip()
    receitas = Receitas.objects.order_by('-data').filter(publicada=True)
    lista_receitas = []
    if nome_a_buscar:
        lista_receitas = receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': lista_receitas
    }
    return render(request, 'receitas/buscar.html', dados)


def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        pessoa = request.user

        receita = Receitas.objects.create(nome_receita=nome_receita, ingredientes=ingredientes, 
                                          modo_preparo=modo_preparo, tempo_preparo=tempo_preparo, rendimento=rendimento, categoria=categoria, foto_receita=foto_receita, pessoa=pessoa)
        receita.save()
        return redirect('dashboard')
    else:
        return render(request, 'receitas/cria_receita.html')
    

def publica(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)

    if receita.publicada:
        receita.publicada = False
    else:
        receita.publicada = True

    receita.save()
    return redirect('dashboard')


def apaga_receita(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)

    receita.delete()

    return redirect('dashboard')


def edita_receita(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)

    dados = {
        'receita': receita
    }
    return render(request, 'receitas/edita_receita.html', dados)


def atualiza_receita(request):
    if request.method == 'POST':

        receita = get_object_or_404(Receitas, pk=request.POST['receita_id'])

        receita.nome_receita = request.POST['nome_receita']
        receita.ingredientes = request.POST['ingredientes']
        receita.modo_preparo = request.POST['modo_preparo']
        receita.tempo_preparo = request.POST['tempo_preparo']
        receita.rendimento = request.POST['rendimento']
        receita.categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES: 
            receita.foto_receita = request.FILES['foto_receita']
        
        receita.save()

        return redirect('dashboard')
    else:
        return redirect('edita_receita')