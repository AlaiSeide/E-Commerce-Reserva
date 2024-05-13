from django.shortcuts import render

# Create your views here.
# Aqui definimos o que que acontece se uma usuario entrar numa pagina, o que que vai aparecer naquela pagina


# No contexto dessa função, request é um objeto que contém informações sobre a solicitação HTTP, como parâmetros GET ou POST, cookies, cabeçalhos, etc. 'homepage.html' é o nome do template que será renderizado e exibido para o usuário.
def homepage(request):
    return render(request, 'homepage.html')