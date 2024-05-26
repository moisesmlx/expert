from django.shortcuts import render
from class_expert_cifras import Cifras
import class_expert_cifras
from django.http import HttpResponse
from random import randint
import trans_A
import trans_Am 
import trans_Astm 
import trans_Ast 
import trans_B 
import trans_Bm 
import trans_C 
import trans_Cm 
import trans_Cst 
import trans_Cstm 
import trans_D 
import trans_Dm 
import trans_Dst 
import trans_Dstm 
import trans_E 
import trans_Em 
import trans_F 
import trans_Fm 
import trans_Fst 
import trans_Fstm 
import trans_G 
import trans_Gm 
import trans_Gst 
import trans_Gstm 
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
    tom_new = ''

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

                # visualizar no html
                if tom_original == 'A':

                    for l in trans_A.nova_cifra:
                        tom_new += l
                if tom_original == 'Am':
                    for l in trans_Am.nova_cifra:
                        tom_new += l
                if tom_original == 'A#':
                    for l in trans_Ast.nova_cifra:
                        tom_new += l
                if tom_original == 'A#m':
                    for l in trans_Astm.nova_cifra:
                        tom_new += l
                if tom_original == 'B':
                    for l in trans_B.nova_cifra:
                        tom_new += l
                if tom_original == 'Bm':
                    for l in trans_Bm.nova_cifra:
                        tom_new += l
                if tom_original == 'C':
                    for l in trans_C.nova_cifra:
                        tom_new += l
                if tom_original == 'Cm':
                    for l in trans_Cm.nova_cifra:
                        tom_new += l
                if tom_original == 'C#':
                    for l in trans_Cst.nova_cifra:
                        tom_new += l
                if tom_original == 'C#m':
                    for l in trans_Cstm.nova_cifra:
                        tom_new += l
                if tom_original == 'D':
                    for l in trans_D.nova_cifra:
                        tom_new += l
                if tom_original == 'Dm':
                    for l in trans_Dm.nova_cifra:
                        tom_new += l
                if tom_original == 'D#':
                    for l in trans_Dst.nova_cifra:
                        tom_new += l
                if tom_original == 'D#m':
                    for l in trans_Dstm.nova_cifra:
                        tom_new += l
                if tom_original == 'E':
                    for l in trans_E.nova_cifra:
                        tom_new += l
                if tom_original == 'Em':
                    for l in trans_Em.nova_cifra:
                        tom_new += l
                if tom_original == 'F':
                    for l in trans_F.nova_cifra:
                        tom_new += l
                if tom_original == 'Fm':
                    for l in trans_Fm.nova_cifra:
                        tom_new += l
                if tom_original == 'F#':
                    for l in trans_Fst.nova_cifra:
                        tom_new += l
                if tom_original == 'F#m':
                    for l in trans_Fstm.nova_cifra:
                        tom_new += l
                if tom_original == 'G':
                    for l in trans_G.nova_cifra:
                        tom_new += l
                if tom_original == 'Gm':
                    for l in trans_Gm.nova_cifra:
                        tom_new += l
                if tom_original == 'G#':
                    for l in trans_Gst.nova_cifra:
                        tom_new += l
                if tom_original == 'G#m':
                    for l in trans_Gstm.nova_cifra:
                        tom_new += l
                # fim visualisação html

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
                lista_cifra['new_cifra'] = ''
                lista_cifra['new_cifra'] = str(tom_new)
                
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
