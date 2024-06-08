from django import forms

class PedidoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    cpf = forms.CharField(label='CPF', max_length=15)
    endereco = forms.CharField(label='Endereço', max_length=200)
    pedido = forms.CharField(label='Pedido', widget=forms.Textarea)
    celular = forms.CharField(label='Celular', max_length=20)

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if any(char.isdigit() for char in nome):
            raise forms.ValidationError("O nome não pode conter números.")
        return nome

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if not cpf.isdigit() or len(cpf) != 11:
            raise forms.ValidationError("O CPF deve conter exatamente 11 dígitos.")
        return cpf

    def clean_celular(self):
        celular = self.cleaned_data['celular']
        if not celular.isdigit() or not (10 <= len(celular) <= 15):
            raise forms.ValidationError("O celular deve conter entre 10 e 15 dígitos.")
        return celular

