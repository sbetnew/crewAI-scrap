CrewAI + Groq: Web Scraper de Notícias de IA body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: 0 auto; padding: 20px; } h1, h2, h3 { color: #2c3e50; } h1 { border-bottom: 2px solid #3498db; padding-bottom: 10px; } h2 { border-left: 4px solid #3498db; padding-left: 10px; margin-top: 30px; } code { background-color: #f8f9fa; padding: 2px 5px; border-radius: 3px; font-family: 'Courier New', Courier, monospace; } pre { background-color: #f8f9fa; padding: 15px; border-radius: 5px; overflow-x: auto; } .badge { display: inline-block; padding: 3px 7px; border-radius: 3px; font-size: 0.8em; font-weight: bold; margin-right: 5px; } .python { background-color: #3776ab; color: white; } .crewai { background-color: #27ae60; color: white; } .groq { background-color: #e67e22; color: white; } .file-structure { font-family: monospace; white-space: pre; line-height: 1.3; } .toc { background-color: #f0f7ff; padding: 15px; border-radius: 5px; margin-bottom: 20px; }

# 🚀 CrewAI + Groq: Web Scraper de Notícias de IA

Python 3.10+

CrewAI 0.28.8

Groq LLaMA3

## 📋 Sumário

- [Visão Geral](#visao-geral)
- [Pré-requisitos](#pre-requisitos)
- [Instalação](#instalacao)
- [Configuração](#configuracao)
- [Como Usar](#como-usar)
- [Estrutura de Arquivos](#estrutura)
- [Personalização](#personalizacao)
- [Troubleshooting](#troubleshooting)
- [Licença](#licenca)

## 🌐 Visão Geral

Sistema automatizado que:

1.  Coleta notícias sobre IA do TechCrunch
2.  Processa o conteúdo com Groq (LLaMA3-70b)
3.  Gera relatórios em português

**Tecnologias:**

- CrewAI (framework para agentes)
- Groq (inferência ultra-rápida)
- Playwright (scraping web)

## 🛠️ Pré-requisitos

- Python 3.10+
- [Conta na Groq](https://console.groq.com/)

  # Verifique sua versão do Python

  python --version

## 📥 Instalação

### 1\. Clone o repositório

    git clone https://github.com/seu-usuario/crewai-groq-scraper.git

    cd crewai-groq-scraper

### 2\. Configure ambiente virtual

    python -m venv venv

    # Windows:

    venv\Scripts\activate

    # Mac/Linux:

    source venv/bin/activate

### 3\. Instale dependências

    pip install -r requirements.txt

    playwright install chromium

### 4\. Configure sua API key

    echo "GROQ_API_KEY=sua_chave_aqui" > .env

## ⚙️ Configuração

### Arquivo `main.py`:

    # Configuração do LLM

    llm = ChatGroq(
    model="groq/llama3-70b-8192",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.6 # 0 = preciso, 1 = criativo
    )

    # Configuração do Scraper

    scraper = ScrapeWebsiteTool(
    website_url="https://techcrunch.com/category/artificial-intelligence/",
    browser="chromium",
    timeout=60
    )

## 🖥️ Como Usar

Execute o sistema:

    python main.py

**Saídas geradas:**

- `output/scraping_result.md`: Dados brutos
- `output/resumo_ia.md`: Análise consolidada

Exemplo de saída:

    ## 🗞️ Últimas Notícias de IA

    1.  **Novo modelo da OpenAI bate recordes**

        - Data: 15/06/2024
        - [Link](https://exemplo.com/noticia1)

    2.  **Robôs humanoides na Amazon**

        - Data: 10/06/2024
        - [Link](https://exemplo.com/noticia2)

## 📂 Estrutura de Arquivos

. ├── main.py # Código principal ├── requirements.txt # Dependências ├── .env # Chaves API ├── output/ # Resultados │ ├── scraping_result.md │ └── resumo_ia.md └── README.md # Documentação

## 🎛️ Personalização

### Mudar site alvo:

    scraper = ScrapeWebsiteTool(
            website_url="https://novosite.com/ia",
            extract="links"  # Alternativas: text/html

        )

### Usar modelo diferente:

    llm = ChatGroq(
            model="groq/mixtral-8x7b-32768",  # Mais rápido
            temperature=0.4

        )

## 🔧 Troubleshooting

### Erros comuns:

**1\. Timeout no scraping**

    scraper = ScrapeWebsiteTool(..., timeout=120)

**2\. Problemas com Playwright**

    playwright install

**3\. Erros na API Groq**

- Verifique:
  - Chave API no `.env`
  - [Limites de uso](https://console.groq.com/settings/limits)

---

Desenvolvido por **Sabrina Bet** • **2025**  
[LinkedIn](https://linkedin.com/in/seu-perfil)
