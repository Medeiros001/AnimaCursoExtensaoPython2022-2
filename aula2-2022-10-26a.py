# Comando input(): quero permitir que 
# O usuário digite algo...
nome = input("Digite seu nome: ")
# Pedir a idade para o usuário "Digite sua idade?"
idade = int(input("Digite sua idade:"))

# Comando de saída...Exibir na tela
print(f"Boa noite, seu nome é {nome}")
# Exiba "Sua idade é ..."
print(f"Sua idade é {idade}")

# E se eu quisesse mostrar o dobro da idade informada?
dobro = idade * 2
print("O dobro da idade informada é: {}".format(dobro))

# Estrutura condicional - o famoso "SE" (if) 
# Se a pessoa for maior de idade, mostre "Você é maior de idade, ótimo! já pode beber ou dirigir"
if idade >= 18:
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir")
else:
  print("Você é xóven ainda, xóven ainda... ")

# E se eu quiser perguntar o gênero (M = Masculino e F = Feminino)
# Mostre (... e você também precisa/precisou prestar o serviço militar obrigatório)
genero = input("Informe o gênero M = Masculino, F = Feminino, O = Outros: ")
if idade >= 18 and genero == "M":
  print("... e você tambèm precisa/precisou prestar o serviço militar obrigatório")






print("vai ser executada de qualquer jeito")
