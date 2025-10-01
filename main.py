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

def processar_jornada_diaria(dia):
    print(f"--- {dia} ---")
    while True:
        entrada = obter_horario_valido("Digite o horário de entrada (HH:MM): ")
        saida = obter_horario_valido("Digite o horário de saída (HH:MM):   ")

        if saida > entrada:
            break
        else:
            print("\nErro: O horário de saída deve ser depois do horário de entrada. Tente novamente.\n")

    horas_no_dia = saida - entrada
    
    if horas_no_dia > LIMITE_DIARIO:
        print(f"Atenção: Você trabalhou {formatar_timedelta(horas_no_dia)}, excedendo o limite de 4 horas.")
    else:
        print(f"Horas trabalhadas no dia: {formatar_timedelta(horas_no_dia)}")
    
    print("-" * 25 + "\n")
    return horas_no_dia

def registrar_horas_semana():
    total_horas_trabalhadas = timedelta()
    for dia in DIAS_DA_SEMANA:
        total_horas_trabalhadas += processar_jornada_diaria(dia)
    
    print("\n--- Resumo da Semana ---")
    print(f"Total de horas trabalhadas de Segunda a Sexta: {formatar_timedelta(total_horas_trabalhadas)}")
    return total_horas_trabalhadas

def main():
    print("--- Calculadora de Carga Horária Semanal ---")
    print(f"Objetivo: Completar {CARGA_HORARIA_SEMANAL_TOTAL.total_seconds() / 3600:.0f} horas semanais.\n")
    registrar_horas_semana()

if __name__ == "__main__":
    main()