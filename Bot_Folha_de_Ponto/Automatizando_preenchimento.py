from random import randint
import pandas as pd


data_dias = [] 


hora_entrada = [] 
minuto_dezena = [] 
minuto_unidade = [] 
horario_inicio = []


intervalo_entrada_hora = [] 
intervalo_entrada_minutos = [] 
horario_intervalo_inicio = []


intervalo_final_hora = [] 
intervalo_final_minutos = [] 
horario_intervalo_final = []


hora_final = [] 
minuto_dezena_final = [] 
minuto_unidade_final = [] 
horario_saida = []

mes = int(input('Quantos dias tem no mês: '))
NumMes = int(input('Qual mês: '))
ano =  int(input('Qual ano: '))
horario_de_entrada = int(input('Digite seu horario de entrada:'))
horario_de_entrada_variado = horario_de_entrada - 1
horario_de_saida = int(input('Digite seu horario de saida:'))
horario_de_saida_variado = horario_de_saida - 1


#Sorteio do horario de entrada
def coluna9(horafinal):
  horario_saida.append('SAIDA')
  for cont in range(0,mes):
    hora_final.append(horario_de_saida)
    minuto_dezena_final.append(0)
    minuto_unidade_final.append(randint(0,9))
    if hora_final[cont] < 10:
      horario_saida.append(f'0{hora_final[cont]}:{minuto_dezena_final[cont]}{minuto_unidade_final[cont]}')
    else:
      horario_saida.append(f'{hora_final[cont]}:{minuto_dezena_final[cont]}{minuto_unidade_final[cont]}')


#Sorteio do intervalo final
def coluna7(intervaloentrada):
  horario_intervalo_final.append('INTERVALO ENTRADA')
  for cont in range(0,mes):
    intervalo_final_hora.append(intervalo_entrada_hora[cont]+1)
    intervalo_final_minutos.append(intervalo_entrada_minutos[cont])
    horario_intervalo_final.append(f'{intervalo_final_hora[cont]}:{intervalo_final_minutos[cont]}')

#Sorteio do intervalo inicio
def coluna4(intervaloentrada):
  horario_intervalo_inicio.append('INTERVALO SAIDA')
  for cont in range(0,mes):
    intervalo_entrada_hora.append(randint(horario_de_entrada + 4,horario_de_entrada + 6))
    intervalo_entrada_minutos.append(randint(10,59))
    horario_intervalo_inicio.append(f'{intervalo_entrada_hora[cont]}:{intervalo_entrada_minutos[cont]}')



#Sorteio do horario de entrada
def coluna2(horaentrada):
  horario_inicio.append('ENTRADA')
  for cont in range(0,mes):
    hora_entrada.append(randint(horario_de_entrada_variado,horario_de_entrada))
    if hora_entrada[cont] == horario_de_entrada:
      minuto_dezena.append(0)
      minuto_unidade.append(randint(0,5))
      horario_inicio.append(f'0{hora_entrada[cont]}:{minuto_dezena[cont]}{minuto_unidade[cont]}')
    else:
      minuto_dezena.append(5)
      minuto_unidade.append(randint(0,9))
      horario_inicio.append(f'0{hora_entrada[cont]}:{minuto_dezena[cont]}{minuto_unidade[cont]}')
    

#Dias do mês
def coluna1(numeros):
  data_dias.append('DATA')
  for cont in range(0,mes):
    data_dias.append(f'{cont+1}/{NumMes}/{ano}')


coluna1(data_dias)
coluna2(hora_entrada)
coluna4(intervalo_entrada_hora)
coluna7(intervalo_final_hora)
coluna9(hora_final)


tabela = pd.DataFrame(
    data = zip(data_dias,horario_inicio,horario_intervalo_inicio,horario_intervalo_final,
        horario_saida), 
    columns=["data_dias","horario_inicio","horario_intervalo_inicio",
              "horario_intervalo_final","horario_saida"])


tabela.to_csv("folha_de_ponto.csv")



#print(data)
#print(hora_entrada)
#print(minuto_dezena)
#print(minuto_unidade)
#print(intervalo_entrada_hora)
#print(intervalo_entrada_minutos)
#print(intervalo_final_hora)
#print(intervalo_final_minutos)
#print(hora_final)
#print(minuto_dezena_final)
#print(minuto_unidade_final)
#print(horario_inicio)
#print(horario_intervalo_inicio)
#print(horario_intervalo_final)
#print(horario_saida)


#print(len(intervalo_final_hora))
#print(len(intervalo_final_minutos))
#print(len(intervalo_entrada_minutos))
#print(len(intervalo_entrada_hora))
#print(len(minuto_unidade))
#print(len(minuto_dezena))
#print(len(data))
#print(len(hora_entrada))
#print(len(horario_inicio))
#print(len(horario_intervalo_inicio))
#print(len(horario_intervalo_final))
#print(len(horario_saida))

print(tabela)