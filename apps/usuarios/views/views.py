from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receitas
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if senha == senha2:
            if User.objects.filter(username=nome).exists():
                messages.error(request, "O usuário já existe")
                return redirect('cadastro')
            else:
                User.objects.create_user(username=nome, email=email, password=senha)
                messages.success(request, "Usuário criado com sucesso")
                return redirect('login')   
        else:
            messages.error(request, "As senhas são diferentes")
            return redirect('cadastro')
        return render(request, 'usuarios/cadastro.html')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user:
                auth.login(request, user=user)
                return redirect('dashboard')
            else:
                # messages(Senha incorreta)
                return redirect('login')
        else:
            # messages(Usuário não existe)
            return redirect('login')

    else:
        return render(request, 'usuarios/login.html')

def dashboard(request):
    if request.user.is_authenticated:
        receitas = Receitas.objects.order_by('-data').filter(pessoa=request.user)

        paginator = Paginator(receitas, 1)
        page = request.GET.get('page')
        lista_receitas = paginator.get_page(page)

        dados = {
            'receitas': lista_receitas
        }

        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('login')
    
def logout(request):
    auth.logout(request)
    return redirect('login')