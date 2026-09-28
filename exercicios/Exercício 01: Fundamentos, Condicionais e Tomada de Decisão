"""
Exercício 01: Fundamentos, Condicionais e Tomada de Decisão
Objetivo: Validar regras operacionais simples baseadas em entrada de dados.
"""

def avaliar_desempenho_operacional(meta_horas, horas_realizadas):
    print(f"Meta definida: {meta_horas}h | Horas realizadas: {horas_realizadas}h")
    
    if horas_realizadas <= meta_horas:
        status = "Dentro do prazo (Meta atingida)"
    elif horas_realizadas <= meta_horas * 1.1:
        status = "Atenção: Margem limite tolerável atingida (10% acima)"
    else:
        status = "Alerta: SLA estourado"
        
    return status

if __name__ == "__main__":
    resultado = avaliar_desempenho_operacional(meta_horas=40, horas_realizadas=42)
    print(f"Status do Atendimento: {resultado}")
