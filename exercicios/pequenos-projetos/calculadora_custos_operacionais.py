"""
Projeto: Calculadora de Custos Operacionais de Transporte e Rota
Objetivo: Calcular custos fixos e variáveis de uma operação logística/frota.
"""

def calcular_custo_viagem(distancia_km, consumo_km_litro, preco_combustivel, pedagio, custo_hora_motorista, tempo_horas):
    # Custo com combustível
    litros_necessarios = distancia_km / consumo_km_litro
    custo_combustivel = litros_necessarios * preco_combustivel
    
    # Custo com equipe/mão de obra
    custo_mao_obra = tempo_horas * custo_hora_motorista
    
    # Custo total e métrica por KM rodado
    custo_total = custo_combustivel + pedagio + custo_mao_obra
    custo_por_km = custo_total / distancia_km if distancia_km > 0 else 0
    
    return {
        "distancia_km": distancia_km,
        "custo_combustivel": round(custo_combustivel, 2),
        "custo_mao_obra": round(custo_mao_obra, 2),
        "pedagio": round(pedagio, 2),
        "custo_total": round(custo_total, 2),
        "custo_por_km": round(custo_por_km, 2)
    }

if __name__ == "__main__":
    relatorio = calcular_custo_viagem(
        distancia_km=250.0,
        consumo_km_litro=2.5,
        preco_combustivel=5.80,
        pedagio=48.50,
        custo_hora_motorista=35.0,
        tempo_horas=4.5
    )
    
    print("=" * 45)
    print("       RELATÓRIO DE CUSTO DA OPERAÇÃO")
    print("=" * 45)
    for chave, valor in relatorio.items():
        rotulo = chave.replace('_', ' ').capitalize()
        unidade = "km" if "distancia" in chave else "R$"
        print(f"{rotulo}: {unidade} {valor}")
    print("=" * 45)
