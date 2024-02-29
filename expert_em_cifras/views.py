from django.shortcuts import render
from class_expert_cifras import Cifras
import class_expert_cifras
from django.http import HttpResponse
from random import randint
import os

id = ''
confirme_download = False
def index(request):
    return render(request, 'main/index.html')


def expertEmCifras(request):
    global id, confirme_download
    decode = randint(1, 1000)
    id = f'{request.POST.get('id')}{int(decode) + int(randint(100, 600))}'
    tom_original = request.POST.get('original')
    novo_tom = request.POST.get('novo')
    nome_cifra = request.POST.get('nome_cifra')
    cifra = request.POST.get('cifra')
    tom_new = 'vazio'

    if tom_original == 'A' or tom_original == 'A#' or tom_original == 'B' or tom_original == 'C' or \
        tom_original == 'C#' or tom_original == 'D' or tom_original == 'D#' or tom_original =='E' or\
        tom_original == 'F' or tom_original == 'F#' or tom_original == 'G' or tom_original == 'G#':
        pass
    
    if novo_tom == 'A' or novo_tom == 'A#' or novo_tom == 'B' or novo_tom == 'C' or novo_tom == 'C#' or \
     novo_tom == 'D' or novo_tom == 'D#' or novo_tom == 'E' or novo_tom == 'F' or novo_tom == 'F#' or \
     novo_tom == 'G' or novo_tom == 'G#' and nome_cifra != '':
        
        if tom_original != '' and novo_tom != '' and cifra != '':
            try:
                Cifras(nome_cifra, tom_original, novo_tom, cifra, id)
                tom_new = class_expert_cifras.new
                try:
                    os.system(rf'del /s /q temporarios\{id}.txt')
                except:
                    os.system(f'del /s /q temporarios/{id}.txt')
                confirme_download = True
                    
                lista_cifra = {
                'new_tom': novo_tom,
                'new_cifra': str(tom_new.strip()),
                'nome': request.POST.get('id'),
                'confirme_download': confirme_download,
                'link': f'Minhas_cifras/{request.POST.get('new_tom')}.txt',
                }
                return render(request, 'info/cifra.html', lista_cifra)
                
            except Exception as erro:
                return HttpResponse('''<center><h1>
                                Não pode deixar os campos vazios por favor volte e tente novamente<br>
                                </h1>
                                <a href="javascript: history.go(-1)">Voltar</a>
                                </center>''')
        else:
            return HttpResponse('''<center><h1>
                                Não pode deixar os campos vazios por favor volte e tente novamente<br>
                                </h1>
                                <a href="javascript: history.go(-1)">Voltar</a>
                                </center>''')
    else:    
        return render(request, 'info/info.html')
