from datetime import datetime, timedelta

CARGA_HORARIA_SEMANAL_TOTAL = timedelta(hours=20)
LIMITE_DIARIO = timedelta(hours=4)
HORA_INICIO_SABADO = datetime.strptime("08:00", "%H:%M")
DIAS_DA_SEMANA = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"]

def obter_horario_valido(mensagem_prompt):
    while True:
        try:
            horario_str = input(mensagem_prompt)
            return datetime.strptime(horario_str, "%H:%M")
        except ValueError:
            print("Formato de hora inválido. Por favor, use HH:MM (ex: 13:30).")

def formatar_timedelta(td):
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    return f"{hours} horas e {minutes} minutos"

def main():
    pass

if __name__ == "__main__":
    main()