#Chatbot com parte de perguntas A B C D não há uma resposta correta, apenas uma resposta de seleção
#Durante o código eu fui testando formas diferentes, no começo coloquei para "printar" e depois eu coloquei apenas "resposta'
# Esqueci de colocar o /n para melhorar a visualização para a quebra de linha
# Eu estou vendo uma melhor forma para fazer a lista ocorrer para no final de todo o formulário imprimir um resumo do que foi selecionado
# esse foi apenas o que deu pra fazer de cabeça, durante o processo pensei em formas para usar o match case e o while. 
# mas não quis cortar o raciocínio e preferi fazer tudo e depois adicionar as melhorias. o match case vai ser para selecionar melhor
# o começo, porque antes de saber se tem um bin adicionado na estação  (LINHA 51) precisa saber se estamos em período pordutivo
# ou podemos estar em período de limpeza de final da campanha, nesse caso é necessário o match case para selecionar um caminho totalmente diferente

print("Houve ocorrencia de EHS?")
print("1 - Sim")
print("2 - Não")
resposta = input("Digite o número da sua resposta: ")
if resposta == "1":
    print("Qual foi a ocorrência?")
    resposta = input("Digite a ocorrência:")

print("Houve ocorrencia de Qualidade?")
print("1 - Sim")
print("2 - Não")
resposta = input("Digite o número da sua resposta: ")
if resposta == "1":
    print("Qual foi a ocorrência?")
    resposta = input("Digite a ocorrência:")

print("Foi realizado o Checklist de Safety Startup?")
print("1 - Sim")
print("2 - Não")
resposta = input("Digite o número da sua resposta: ")
if resposta == "1":
    print("Alguma falha durante o teste?")
    resposta = input("Escreva de forma breve:")
elif resposta == "2":
    print("Porque não foi realizado o Checklist de Safety Startup?")
    resposta = input("Escreva de forma breve:")

print("Foi realizado o Checklist nas Empilhadeiras?")
print("1 - Sim")
print("2 - Não")
resposta = input("Digite o número da sua resposta: ")
if resposta == "1":
    resposta= input("Necessário carregar ou resisão/manutenção?")
elif resposta == "2":
    resposta= input("Porque não foi realizado o Checklist nas Empilhadeiras?")

print("Houve quebra ou ajuste significativo em equipamento?")
print("1 - Sim")
print("2 - Não")
resposta = input("Digite o número da sua resposta: ")
if resposta == "1":
    resposta= input("Conte de forma direta o que ocorreu e quais as medidas tomadas, adicione também o tempo estimado em cada atividade e se foi necessário abertura de ACR:")

print("Bulk alocado na Estação 1?")
print("1 - Sim")
print("2 - Não")
print("3 - Não aplicavel")
resposta = input("Digite o número da sua resposta: ")
if resposta == "1":
    resposta = input("Qual o número do bulk?")
elif resposta == "2":
    resposta = input("Porque não temos bulk alocado na Estação 1?")


print("Bulk alocado na Estação 2?")
print("1 - Sim")
print("2 - Não")
print("3 - Não aplicavel")
resposta = input("Digite o número da sua resposta: ")
if resposta == "1":
    resposta = input("Qual o número do bulk?")
elif resposta == "2":
    resposta = input("Porque não temos bulk alocado na Estação 2?")

print("Processos em andamento durante a passagem de turno?")
print("1 - Sim")
print("2 - Não")
resposta = input("Digite o número da sua resposta: ")
if resposta == "1":
    resposta = input("Quais processos estão em andamento?")


print("Quantos bulks fabricados?")
resposta = input("Digite os números dos bulk:")

print("Necessário pedir Bulk?")
print("1 - Sim")
print("2 - Não")
resposta = input("Digite o número da sua resposta: ")
if resposta == "1":
    resposta = input("Foi solicitado com previsão para que horas ou ainda será necessário solicitar?")
    
print("Quantos carbonatos fabricados e quantos aprovados?")
resposta = input("Digite os números dos carbonatos fabricados e quantos aprovados:")

print("Necessário pedir Carbonato?")
print("1 - Sim")
print("2 - Não")
resposta = input("Digite o número da sua resposta:")
if resposta == "1":
    resposta = input("Foi solicitado com previsão para que horas ou ainda será necessário solicitar?")

print("Pendências no SAP?")
print("1 - Sim")
print("2 - Não")
resposta = input("Digite o número da sua resposta:")
if resposta == "1":
    resposta = input("Quais pendências no SAP?")

print("Pendências no sistema de PASX?")
print("1 - Sim")
print("2 - Não")
resposta = input("Digite o número da sua resposta:")
if resposta == "1":
    resposta = input("Quais pendências no sistema de PASX?")









    #atualizar para lista, para no final dar o print de tudo o que foi respondido em formato de relatório
