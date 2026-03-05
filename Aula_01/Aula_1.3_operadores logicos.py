#usando AND na verificação de idade e altura
idade = 25
altura = 1.75


resultado = (idade >= 18) and (altura >= 1.70) 
msg = 'Pode participar do evento?' + str(resultado)
print(msg)


#Programa de disparo de alarme usando OR

porta = 'a'
janela = 'f'

alarme = (porta == 'a') or (janela == 'a')
msg = "Alarme disparado? " + str(alarme)
print(msg)

#usando o NOT na verficação se tem ou nao dinheiro para comprar
#operador NOT inverte o estado logico

tem_dinheiro = False
tem_dinheiro = not tem_dinheiro
msg = 'Tem dinheiro? ' + str(tem_dinheiro)
print(msg)

