import schedule
import time
import os
from plyer import notification
import winsound
from playsound import playsound

def alerta_medicamento(nome_medicamento):
    notification.notify(
        title='Hora do Medicamento',
        message=f'É hora de tomar o seu medicamento: {nome_medicamento}',
        timeout=10
    )
    winsound.Beep(1000, 1500)
    playsound('som.mp3')
    print(f'Notificação enviada: {nome_medicamento}')


def salvar_medicamentos(medicamentos, arquivo='medicamentos.txt'):
    with open(arquivo, 'a') as f:
        for medicamento, horario in medicamentos.items():
            f.write(f'{medicamento},{horario}\n')

def carregar_medicamentos(arquivo='medicamentos.txt'):
    medicamentos = {}
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            for linha in f:
                medicamento, horario = linha.strip().split(',')
                medicamentos[medicamento] = horario
    return medicamentos


def adicionar_medicamentos():
    medicamentos = {}
    while True:
        medicamento = input('Digite o nome do medicamento: ')
        horario = input('Digite o horário para tomar o medicamento (HH:MM): ')
        medicamentos[medicamento] = horario
        continuar = input('Deseja adicionar mais medicamentos? (s/n): ')
        if continuar.lower() != 's':
            break
    return medicamentos



if not os.path.exists('medicamentos.txt'):
    print('Arquivo de medicamentos não encontrado. Vamos adicionar alguns medicamentos.')
    medicamentos = adicionar_medicamentos()
    salvar_medicamentos(medicamentos)
else:
    medicamentos = carregar_medicamentos()

for medicamento, horario in medicamentos.items():
    schedule.every().day.at(horario).do(alerta_medicamento, nome_medicamento=medicamento)

print('Agendador de medicamentos iniciado...')
while True:
    schedule.run_pending()
    time.sleep(1)




