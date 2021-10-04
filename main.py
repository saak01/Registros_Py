from logging import ERROR
from os import error
from funcs import *
from time import sleep

#main
titulo("Cadastros Py")
#
while True:
  print("""
  1- Cadastras Pessoas
  2- Mostrar Pessoas
  3- Excluir Pessoas
  4- Encerrar Programa""")
  escolha = input(str("\nEscolha a opção desejada: "))

  if escolha == "1":
   try:
     print('---'*20)
     adicao_usuarios()
     print('---'*20)
     print('Adicionado com sucesso')
     sleep(1)
     print('---'*20)
   except:
      print(f'Error, algo deu errado.3')
      

  if escolha == "2":
    print('X Inc.            Funcionarios')
    print('-'*120)
    print(f'{"N°" :<5}|{"Nome" :<50}|{"Email" :<50}|{"Senha" :<50} \n')
    print('-'*120)
    mostrartabela()
    sleep(3)

  if escolha == "3":
    excluircadastros()
    print('---'*20)
  if escolha == "4":
    break