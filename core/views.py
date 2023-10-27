from django.shortcuts import render

from django.contrib import messages

from .models import Contato

from .forms import ContatoForm

def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None)
    
    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            
            data = Contato(nome=nome, email=email, assunto=assunto, mensagem=mensagem)
            
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
    return render(request, 'produto.html')