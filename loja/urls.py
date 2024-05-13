from django.urls import path
from .views import *


urlpatterns = [
    # '': Esta é a rota ou o caminho. Quando está vazio '', significa que é a página inicial do seu site. Por exemplo, se o seu site for www.meusite.com, essa rota corresponderia a www.meusite.com.

    # homepage: Esta é a função de visualização que será chamada quando alguém acessar essa rota. Essa função é responsável por decidir o que o usuário verá quando acessar essa rota. Por exemplo, pode ser uma página inicial com boas-vindas ao usuário.

    # name='homepage': Este é o nome que você dá para essa rota. Isso é útil para referenciar essa rota em outras partes do seu código. Por exemplo, se você quiser criar um link para essa rota, você pode usar o nome ‘homepage’ em vez de escrever a rota completa.
    path('', homepage, name='homepage')
]
