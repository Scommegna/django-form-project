from django.shortcuts import render

from django.contrib import messages

from django.shortcuts import redirect

from .models import Contato, Produto

from .forms import ContatoForm, ProdutoModelForm

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    
    return render(request, 'index.html', context)

def contato(request):
    form = ContatoForm(request.POST or None)
    
    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            
            data = Contato(nome=nome, email=email, assunto=assunto, mensagem=mensagem)
            
            form.send_mail()
            
            data.save()
            
            messages.success(request, 'Enviado com sucesso!')
            
            form = ContatoForm()
            
        else:
            messages.error(request, 'Erro ao enviar o email.')
    
    context = {
        'form': form
    }
    
    return render(request, 'contato.html', context)
    

def produto(request):
    if str(request.user != 'AnonymousUser'):
        
        if request.method == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
        
            if form.is_valid():
                form.save()
            
                messages.success(request, 'Produto salvo com sucesso.')
            
            
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar o produto.')
            
        else:
            form = ProdutoModelForm()
    
        context = {
            'form': form
        }
    
        return render(request, 'produto.html', context)
    
    else:
        return redirect('index')