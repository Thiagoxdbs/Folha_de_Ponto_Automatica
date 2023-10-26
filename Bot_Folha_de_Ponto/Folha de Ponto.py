import tkinter as tk
from random import randint
import pandas as pd

def gerar_folha_ponto():
    mes = int(entry_mes.get())
    NumMes = int(entry_num_mes.get())
    ano = int(entry_ano.get())
    horario_de_entrada = int(entry_hora_entrada.get())
    horario_de_saida = int(entry_hora_saida.get())

    data_dias = ['DATA'] + [f'{cont+1}/{NumMes}/{ano}' for cont in range(mes)]

    hora_entrada = ['ENTRADA'] + [f'0{randint(horario_de_entrada-1, horario_de_entrada)}:{0 if hora_entrada == horario_de_entrada else 5}{randint(0, 5) if hora_entrada == horario_de_entrada else randint(0, 9)}' for hora_entrada in range(mes)]
    intervalo_entrada_hora = [randint(horario_de_entrada + 4, horario_de_entrada + 6) for _ in range(mes)]
    intervalo_entrada_minutos = [randint(10, 59) for _ in range(mes)]
    intervalo_final_hora = [hora + 1 for hora in intervalo_entrada_hora]
    intervalo_final_minutos = intervalo_entrada_minutos

    horario_intervalo_inicio = ['INTERVALO SAIDA'] + [f'{hora}:{minuto}' for hora, minuto in zip(intervalo_entrada_hora, intervalo_entrada_minutos)]
    horario_intervalo_final = ['INTERVALO ENTRADA'] + [f'{hora}:{minuto}' for hora, minuto in zip(intervalo_final_hora, intervalo_final_minutos)]

    horario_saida = ['SAIDA'] + [f'{horario_de_saida}:{0}{randint(0, 9)}' for _ in range(mes)]

    tabela = pd.DataFrame(
        data=zip(data_dias, hora_entrada, horario_intervalo_inicio, horario_intervalo_final, horario_saida),
        columns=["data_dias", "horario_inicio", "horario_intervalo_inicio", "horario_intervalo_final", "horario_saida"]
    )

    tabela.to_csv("folha_de_ponto.csv")

    result_label.configure(text="Folha de ponto gerada com sucesso!")


# Criar janela principal
root = tk.Tk()
root.title("Gerador de Folha de Ponto")

# Criar rótulos e campos de entrada
label_mes = tk.Label(root, text="Quantos dias tem no mês:")
label_mes.pack()
entry_mes = tk.Entry(root)
entry_mes.pack()

label_num_mes = tk.Label(root, text="Qual mês:")
label_num_mes.pack()
entry_num_mes = tk.Entry(root)
entry_num_mes.pack()

label_ano = tk.Label(root, text="Qual ano:")
label_ano.pack()
entry_ano = tk.Entry(root)
entry_ano.pack()

label_hora_entrada = tk.Label(root, text="Digite seu horário de entrada:")
label_hora_entrada.pack()
entry_hora_entrada = tk.Entry(root)
entry_hora_entrada.pack()

label_hora_saida = tk.Label(root, text="Digite seu horário de saída:")
label_hora_saida.pack()
entry_hora_saida = tk.Entry(root)
entry_hora_saida.pack()

generate_button = tk.Button(root, text="Gerar Folha de Ponto", command=gerar_folha_ponto)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Executar janela principal
root.mainloop()