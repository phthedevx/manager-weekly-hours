# manager-weekly-hours
Com uma rotina de horários flexíveis durante a semana, eu precisava de uma forma precisa para calcular as horas restantes a serem cumpridas aos sábados, sempre respeitando o limite de 4 horas diárias.

Para otimizar esse processo e eliminar cálculos manuais, desenvolvi um script em Python. A ferramenta automatiza a contagem da carga horária semanal e determina exatamente meu horário de saída no sábado.

Funcionalidades Principais

* **✅ Cálculo Automático:** Calcula o total de horas trabalhadas durante a semana.
* **✅ Previsão Precisa:** Informa o horário exato de saída para o sábado.
* **✅ Validação de Dados:** Garante que os horários inseridos estejam em formato correto (`HH:MM`) e que a saída seja posterior à entrada.
* **✅ Alertas Inteligentes:** Notifica o usuário caso o limite de 4 horas diárias seja excedido.
* **✅ Gestão de Excedentes:** Lida com cenários onde a carga horária já foi completada antes do sábado.
* **✅ Interface Interativa:** Guiado por um console limpo e intuitivo.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Módulos Nativos:** `datetime` e `timedelta` para manipulação precisa de data e hora.
