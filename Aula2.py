' Permitir que o usuário digite algo '

#comando de entrada

nome = input("Digite seu nome: ")

idade = int(input("Digite a sua idade: "))

genero = input("Informe o gênero. M para Masculino; F para Feminino e O para Outros: ")

#outras variáveis

dobro = idade * 2

feminino = "F"

masculino = "M"

outro = "O"

#comando de saída

print("Seu nome é {}" .format(nome))

print("Sua idade é {}" .format(idade))

print("O dobro de sua idade é {}".format(dobro))

#condicional

if idade >= 18:
  
  print("Opa! você já é maior de idade!")

else: 
  print("Est xóven demais.")


if idade >= 18 and genero == "M":
  print("Você precisa prestar serviço militar obrigatório.")

elif idade >=18 and genero == "F":
  print("Sua prestação de serviço militar não é obrigatória.")
          

  


  
