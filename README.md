# Projeto MLOps com Classificador de Íris

Este projeto demonstra uma pipeline MLOps completa usando um classificador de íris como exemplo. Ele integra várias ferramentas e práticas modernas de MLOps, incluindo controle de versão de dados, experimentação, empacotamento de modelos e implantação contínua.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal
- **scikit-learn**: Para o modelo de classificação
- **MLflow**: Para rastreamento de experimentos e registro de modelos
- **BentoML**: Para empacotamento e servir o modelo
- **DVC (Data Version Control)**: Para versionamento de dados
- **GitHub Actions**: Para CI/CD

## Estrutura do Projeto

```
.
├── .github
│   └── workflows
│       └── mlops_pipeline.yml
├── data
│   └── iris.csv
├── models
│   └── model.pkl
├── src
│   ├── train.py
│   └── serve.py
├── .dvc
├── .gitignore
├── bentofile.yaml
├── requirements.txt
└── README.md
```

## Configuração

1. Clone o repositório:
   ```
   git clone https://github.com/ntsation/project-mlops.git
   cd project-mlops
   ```

2. Crie e ative um ambiente virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Configure o DVC:
   ```
   dvc init
   dvc add data/iris.csv
   ```

   Para uso local:
   ```
   dvc remote add -d localremote /caminho/para/armazenamento/local
   ```

   Para uso com Google Drive (recomendado para CI/CD):
   ```
   dvc remote add -d myremote gdrive://your-drive-id
   ```

   Depois de configurar o remote:
   ```
   dvc push
   ```

## Uso

### Treinamento do Modelo

Para treinar o modelo:

```
python src/train.py
```

Isso treinará o modelo, registrará métricas no MLflow e salvará o modelo usando BentoML.

### Servindo o Modelo

Para servir o modelo localmente:

```
bentoml serve src/serve.py:svc
```

### Construindo o BentoML Bundle

Para construir um bundle BentoML:

```
bentoml build
```

## Pipeline CI/CD

O arquivo `.github/workflows/mlops_pipeline.yml` define um pipeline CI/CD que é acionado em pushes para a branch main. 

**Nota Importante sobre DVC e CI/CD:**
Se você estiver usando o DVC com armazenamento local, o pipeline CI/CD no GitHub Actions falhará ao tentar acessar os dados no DVC. Isso ocorre porque o armazenamento local não está acessível no ambiente de CI/CD remoto. 

Para resolver esse problema, você tem algumas opções:

1. Use um armazenamento remoto para o DVC, como Google Drive, AWS S3, ou similar. Isso permitirá que o pipeline CI/CD acesse os dados.

2. Se você precisa manter o armazenamento local, considere adicionar os dados ao repositório Git para fins de CI/CD. Neste caso, você pode criar um branch separado para CI/CD que inclui os dados.

3. Modifique o pipeline CI/CD para pular a etapa de pull do DVC quando estiver usando armazenamento local.

Para execução local, o uso de armazenamento local do DVC funcionará sem problemas.

O pipeline inclui:

- Instalação de dependências
- Configuração do DVC e pull dos dados (pode falhar com armazenamento local)
- Treinamento do modelo
- Construção do bundle BentoML
- Testes (simulados)
- Deploy (simulado)

## Execução Local vs. CI/CD

- **Execução Local**: Todos os passos, incluindo o DVC com armazenamento local, funcionarão conforme esperado.
- **CI/CD**: Se estiver usando DVC com armazenamento local, o passo de pull dos dados falhará. Considere as opções mencionadas acima para resolver isso.

## Monitoramento e Iteração

Use o MLflow UI para visualizar métricas e parâmetros:

```
mlflow ui
```