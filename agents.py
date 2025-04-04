from crewai import Agent
from config import get_llm
from tools import get_scraper_tool

def create_analista_web():
    return Agent(
        role="Analista de Conteúdo Web",
        goal="Extrair e estruturar informações de páginas da web em português",
        backstory="Especialista em web scraping e análise semântica com foco em tecnologia.",
        tools=[get_scraper_tool()],
        verbose=True,
        llm=get_llm(),
        max_iter=5
    )

def create_redator_tech():
    return Agent(
        role="Redator de Tecnologia",
        goal="Escrever resumos claros em português sobre tendências de IA",
        backstory="Jornalista tech brasileiro com foco em inteligência artificial.",
        verbose=True,
        llm=get_llm(),
        max_iter=5
    )