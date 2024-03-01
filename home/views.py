from django.shortcuts import render
from pathlib import Path
from django.http import HttpResponse, FileResponse
from django.urls import reverse
import os
# Create your views here.


def index(request):
    print('procurou no banco')
    return render(request,'base/home.html')

def filmes(request):
    base_dir = Path(__file__).resolve().parent.parent
    caminhofilmes = os.path.join(base_dir,'static/filmes/')
    filmes = os.listdir(caminhofilmes)
    links = []
    filmes_files = []
    imagens = []
    caminho_imagens = []
    cont = 0
    cont2 = 0
    for filme in filmes:
        conc = filme + ".png"
        imagens = imagens + [conc]

    for filme in filmes:
        conc = filme + ".mp4"
        filmes_files = filmes_files + [conc]

    for filme in filmes:
        conc = filme
        conc = conc + "/" + imagens[cont]
        caminho_imagens = caminho_imagens + [conc]
        cont += 1
    for filme in filmes:
        caminho = "/filme/" + filme
        conc1 = caminho + "/"
        conc2 = conc1 + filmes_files[cont2]
        links = links + [conc2]
        cont2 += 1
    context = {
        'filmes_imagens_links': zip(filmes, caminho_imagens, links)
    }
    return render(request,'base/filmes.html', context)

def episodios(request, nome_serie):
    #vai pesquisar o diretorio da serie e listar as temporadas
    base_dir = Path(__file__).resolve().parent.parent
    caminhoseries = os.path.join(base_dir,'static/series/',nome_serie,'episodios/')
    episodios = os.listdir(caminhoseries)
    links = []
    for episodio in episodios:
        caminho = "/serie/" + nome_serie
        conc1 = caminho + "/"
        conc2 = conc1 + episodio
        links = links + [conc2]
    
    context = {
        'episodios_links': zip(episodios,links)
    }
    return render(request, 'base/episodios.html',context)

def series(request):
    base_dir = Path(__file__).resolve().parent.parent
    caminhoseries = os.path.join(base_dir,'static/series/')
    series = os.listdir(caminhoseries)
    imagens = []
    caminho_imagens = []
    links = []
    cont = 0
    #coloca a extesão no arquivo de imagen
    for serie in series:
        junta = serie + ".png"
        imagens = imagens + [junta]
    #concatena nome da pasta com o arquivo para usar com 'static/series/'
    for serie in series:
        conc = serie
        conc = conc + "/" + imagens[cont]
        caminho_imagens = caminho_imagens + [conc]
        cont += 1

    for serie in series:
        episodios = "/episodios/"
        conc = episodios + serie
        links = links + [conc]

    context = {
        'series_imagens_links': zip(series, caminho_imagens, links)
    }

    return render(request,'base/series.html', context)

def transmitir_serie(request, nome_serie, nome_episodio):
    base_dir = Path(__file__).resolve().parent.parent
    filename = os.path.join(base_dir,'static/series/', nome_serie, 'episodios/', nome_episodio)
    video_file = open(filename, 'rb')
    return FileResponse(video_file, content_type='video/mp4')

def transmitir_filme(request, nome_pasta, nome_filme):
    base_dir = Path(__file__).resolve().parent.parent
    filename = os.path.join(base_dir,'static/filmes/', nome_pasta, nome_filme)
    video_file = open(filename, 'rb')
    return FileResponse(video_file, content_type='video/mp4')

    
