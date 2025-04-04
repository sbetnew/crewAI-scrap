from crewai import Crew
from agents import create_analista_web, create_redator_tech
from tasks import create_scraping_task, create_resumo_task

def main():
    # Criar equipe
    equipe = Crew(
        agents=[create_analista_web(), create_redator_tech()],
        tasks=[create_scraping_task(), create_resumo_task()],
        verbose=True
    )

    print("🔎 Iniciando scraping e análise...")
    try:
        resultado = equipe.kickoff()
        print("✅ Resultado final:\n", resultado)
    except Exception as e:
        print(f"❌ Erro durante a execução: {e}")

if __name__ == "__main__":
    main()


# project/
# ├── main.py          # Ponto de entrada principal
# ├── agents.py        # Definição dos agentes
# ├── tasks.py         # Definição das tarefas
# ├── tools.py         # Configuração das ferramentas
# └── config.py        # Configurações globais



# ATIVIDADE

# Atividade Prática: Implementando um Revisor Técnico Automatizado

# Contexto
#   Seu sistema já possui dois agentes:
#    - Analista Web (coleta notícias)
#    - Redator Técnico (gera resumos em português)

#   Agora, você deve criar um Revisor Técnico que:
#    - Verifica se o resumo está dentro do padrão de qualidade
#    - Calcula métricas simples (número de palavras, termos técnicos)
#    - Sugere melhorias

# Objetivo
# - Adicionar um terceiro agente "Revisor Técnico" ao sistema de análise de notícias, utilizando as 
#   ferramentas FileReadTool e CalculatorTool para validar a qualidade do resumo gerado.