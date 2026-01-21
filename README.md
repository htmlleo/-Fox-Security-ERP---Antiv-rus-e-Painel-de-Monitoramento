# -Fox-Security-ERP---Antiv-rus-e-Painel-de-Monitoramento
## Descrição do Projeto O **Fox Security ERP** é um sistema de monitoramento e segurança local desenvolvido em **Python**, com foco em **escaneamento de arquivos**, **quarentena de ameaças**, e **painel ERP** para exibir métricas do sistema em tempo real.   O sistema foi pensado para ser **interativo e visual**,
# 🦊 Fox Security ERP - Antivírus e Painel de Monitoramento

## Descrição do Projeto
O **Fox Security ERP** é um sistema de monitoramento e segurança local desenvolvido em **Python**, com foco em **escaneamento de arquivos**, **quarentena de ameaças**, e **painel ERP** para exibir métricas do sistema em tempo real.  
O sistema foi pensado para ser **interativo e visual**, permitindo ao usuário acompanhar os arquivos escaneados, a saúde do PC e gerenciar possíveis ameaças.

Este projeto inclui funcionalidades inspiradas em antivírus comerciais, com melhorias para **visualização de dados**, **gestão de arquivos suspeitos** e integração de conceitos de **IA para otimização de processos** (assistência do ChatGPT para implementação do código e lógica de monitoramento).

---

## Funcionalidades Implementadas
- 🔍 **Escaneamento completo de diretórios** do usuário, identificando arquivos suspeitos por extensão.
- 📦 **Quarentena de arquivos suspeitos**, permitindo isolá-los do sistema.
- 📊 **Painel ERP** com métricas em tempo real:
  - Uso de CPU
  - Uso de RAM
  - Uso de Disco
  - Quantidade de arquivos escaneados
  - Quantidade de ameaças detectadas
- 🦊 **Indicador visual de saúde do PC** com raposa verde (saudável) ou vermelha (alerta).
- 🖥️ **Visual interativo**, incluindo efeitos visuais estilo "Matrix" durante escaneamento.
- 📜 **Log em tempo real** de arquivos escaneados e ameaças detectadas.
- ✅ **Funcionalidade de limpeza** (opcional, removendo arquivos temporários para otimização do PC).

---

## Tecnologias Utilizadas
- Linguagem: **Python 3.10+**
- Bibliotecas:
  - `psutil` (monitoramento de sistema)
  - `tkinter` (interface gráfica)
  - `pathlib` e `os` (manipulação de arquivos)
  - `shutil` (movimentação de arquivos)
- Conceitos aplicados:
  - Programação orientada a objetos
  - Multithreading para scans em segundo plano
  - Lógica de quarentena e gerenciamento de ameaças
  - Visualização de dados em tempo real

---

## Como Executar
1. Clone o repositório:
```bash
git clone <seu-repositorio>
Crie um ambiente virtual (opcional, recomendado):

python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Mac/Linux


Instale as dependências:

pip install -r requirements.txt


Execute o projeto:

python main.py


O arquivo main.py é o script principal que inicia o Fox Security ERP.

Autor

Leonardo Estevão Alves

Graduando em Sistemas de Informação

Apaixonado por Python e Inteligência Artificial

Implementação assistida pelo ChatGPT para otimização do projeto

Observações

Este projeto é voltado para fins educativos e de portfólio, demonstrando habilidades em:

Desenvolvimento de softwares de monitoramento

GUI avançada com Python

Multithreading e manipulação de arquivos

Aplicação prática de conceitos de IA na programação
