<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CrewAI + Groq: Web Scraper de Notícias de IA</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        h1 {
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        h2 {
            border-left: 4px solid #3498db;
            padding-left: 10px;
            margin-top: 30px;
        }
        code {
            background-color: #f8f9fa;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: 'Courier New', Courier, monospace;
        }
        pre {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
        .badge {
            display: inline-block;
            padding: 3px 7px;
            border-radius: 3px;
            font-size: 0.8em;
            font-weight: bold;
            margin-right: 5px;
        }
        .python {
            background-color: #3776ab;
            color: white;
        }
        .crewai {
            background-color: #27ae60;
            color: white;
        }
        .groq {
            background-color: #e67e22;
            color: white;
        }
        .file-structure {
            font-family: monospace;
            white-space: pre;
            line-height: 1.3;
        }
        .toc {
            background-color: #f0f7ff;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <h1>🚀 CrewAI + Groq: Web Scraper de Notícias de IA</h1>
    
    <div class="badge python">Python 3.10+</div>
    <div class="badge crewai">CrewAI 0.28.8</div>
    <div class="badge groq">Groq LLaMA3</div>

    <div class="toc">
        <h2>📋 Sumário</h2>
        <ul>
            <li><a href="#visao-geral">Visão Geral</a></li>
            <li><a href="#pre-requisitos">Pré-requisitos</a></li>
            <li><a href="#instalacao">Instalação</a></li>
            <li><a href="#configuracao">Configuração</a></li>
            <li><a href="#como-usar">Como Usar</a></li>
            <li><a href="#estrutura">Estrutura de Arquivos</a></li>
            <li><a href="#personalizacao">Personalização</a></li>
            <li><a href="#troubleshooting">Troubleshooting</a></li>
            <li><a href="#licenca">Licença</a></li>
        </ul>
    </div>

    <h2 id="visao-geral">🌐 Visão Geral</h2>
    <p>Sistema automatizado que:</p>
    <ol>
        <li>Coleta notícias sobre IA do TechCrunch</li>
        <li>Processa o conteúdo com Groq (LLaMA3-70b)</li>
        <li>Gera relatórios em português</li>
    </ol>

    <p><strong>Tecnologias:</strong></p>
    <ul>
        <li>CrewAI (framework para agentes)</li>
        <li>Groq (inferência ultra-rápida)</li>
        <li>Playwright (scraping web)</li>
    </ul>

    <h2 id="pre-requisitos">🛠️ Pré-requisitos</h2>
    <ul>
        <li>Python 3.10+</li>
        <li><a href="https://console.groq.com/" target="_blank">Conta na Groq</a></li>
    </ul>

    <pre><code># Verifique sua versão do Python

python --version</code></pre>

    <h2 id="instalacao">📥 Instalação</h2>

    <h3>1. Clone o repositório</h3>
    <pre><code>git clone https://github.com/seu-usuario/crewai-groq-scraper.git

cd crewai-groq-scraper</code></pre>

    <h3>2. Configure ambiente virtual</h3>
    <pre><code>python -m venv venv

# Windows:

venv\Scripts\activate

# Mac/Linux:

source venv/bin/activate</code></pre>

    <h3>3. Instale dependências</h3>
    <pre><code>pip install -r requirements.txt

playwright install chromium</code></pre>

    <h3>4. Configure sua API key</h3>
    <pre><code>echo "GROQ_API_KEY=sua_chave_aqui" > .env</code></pre>

    <h2 id="configuracao">⚙️ Configuração</h2>

    <h3>Arquivo <code>main.py</code>:</h3>
    <pre><code># Configuração do LLM

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
)</code></pre>

    <h2 id="como-usar">🖥️ Como Usar</h2>
    <p>Execute o sistema:</p>
    <pre><code>python main.py</code></pre>

    <p><strong>Saídas geradas:</strong></p>
    <ul>
        <li><code>output/scraping_result.md</code>: Dados brutos</li>
        <li><code>output/resumo_ia.md</code>: Análise consolidada</li>
    </ul>

    <p>Exemplo de saída:</p>
    <pre><code>## 🗞️ Últimas Notícias de IA

1.  **Novo modelo da OpenAI bate recordes**

    - Data: 15/06/2024
    - [Link](https://exemplo.com/noticia1)

2.  **Robôs humanoides na Amazon**

    - Data: 10/06/2024
    - [Link](https://exemplo.com/noticia2)</code></pre>


        <h2 id="estrutura">📂 Estrutura de Arquivos</h2>
        <div class="file-structure">

    .
    ├── main.py # Código principal
    ├── requirements.txt # Dependências
    ├── .env # Chaves API
    ├── output/ # Resultados
    │ ├── scraping_result.md
    │ └── resumo_ia.md
    └── README.md # Documentação
    </div>

        <h2 id="personalizacao">🎛️ Personalização</h2>

        <h3>Mudar site alvo:</h3>
        <pre><code>scraper = ScrapeWebsiteTool(
        website_url="https://novosite.com/ia",
        extract="links"  # Alternativas: text/html

    )</code></pre>

        <h3>Usar modelo diferente:</h3>
        <pre><code>llm = ChatGroq(
        model="groq/mixtral-8x7b-32768",  # Mais rápido
        temperature=0.4

    )</code></pre>

        <h2 id="troubleshooting">🔧 Troubleshooting</h2>

        <h3>Erros comuns:</h3>

        <p><strong>1. Timeout no scraping</strong></p>
        <pre><code>scraper = ScrapeWebsiteTool(..., timeout=120)</code></pre>

        <p><strong>2. Problemas com Playwright</strong></p>
        <pre><code>playwright install</code></pre>

        <p><strong>3. Erros na API Groq</strong></p>
        <ul>
            <li>Verifique:
                <ul>
                    <li>Chave API no <code>.env</code></li>
                    <li><a href="https://console.groq.com/settings/limits" target="_blank">Limites de uso</a></li>
                </ul>
            </li>
        </ul>

        <hr>

        <p>Desenvolvido por <strong>Sabrina Bet</strong> • <strong>2025</strong><br>
        <a href="https://linkedin.com/in/seu-perfil" target="_blank">LinkedIn</a></p>

    </body>
    </html>
