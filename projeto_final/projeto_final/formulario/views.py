from django.shortcuts import render
from .forms import PedidoForm
import requests

def pedido_view(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            cpf = form.cleaned_data['cpf']
            endereco = form.cleaned_data['endereco']
            pedido = form.cleaned_data['pedido']
            celular = form.cleaned_data['celular']

            mensagem = f"******* Novo Pedido *******\n\nNome: {nome}\nCelular: {celular}\nCPF: {cpf}\nEndereço: {endereco}\n\nPedido: \n{pedido}"  

            token = '7137561963:AAGhr6Ya8MvzhjUoJQJX1HrOw0jEaYn_P68'
            chat_id = '694107029'  
            url = f'https://api.telegram.org/bot{token}/sendMessage'

            response = requests.post(url, data={'chat_id': chat_id, 'text': mensagem})

            if response.status_code == 200:
                return render(request, 'formulario/success.html', {'form': form, 'enviado': True})
            else:
                error_message = response.json().get('description', 'Não foi possível enviar a mensagem ao bot do Telegram.')
                return render(request, 'formulario/error.html', {'error': error_message})
    else:
        form = PedidoForm()

    return render(request, 'formulario/pedido.html', {'form': form})
