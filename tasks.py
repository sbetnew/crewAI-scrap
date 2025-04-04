from crewai import Task
from agents import create_analista_web, create_redator_tech

def create_scraping_task():
    return Task(
        description="""Raspe a página fornecida e extraia em português:
        1. Títulos das 5 principais notícias (traduza se necessário)
        2. Links associados
        3. Data de publicação (se disponível)
        Mantenha o resultado em Português do Brasil""",
        expected_output="Lista estruturada em Markdown com os dados coletados em português.",
        agent=create_analista_web(),
        output_file="output/scraping_result.md"
    )

def create_resumo_task():
    return Task(
        description="""Com base nos dados raspados, crie em português:
        1. Um parágrafo com as tendências principais
        2. Destaque 2 inovações relevantes para o mercado brasileiro
        3. Inclua links para as fontes
        Use linguagem natural e acessível em Português do Brasil""",
        expected_output="Relatório em Markdown com análise concisa em português.",
        agent=create_redator_tech(),
        context=[create_scraping_task()],
        output_file="output/resumo_ia.md"
    )