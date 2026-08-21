# Coletor de Proxies com Playwright e OpenPyXL

Automação desenvolvida em Python para acessar uma página web, extrair informações de servidores proxy e salvar os dados automaticamente em uma planilha Excel.

## Sobre o projeto

Este projeto utiliza o Playwright para controlar um navegador Chromium, acessar uma página contendo uma tabela de proxies e extrair informações como endereço IP, porta e protocolo.

Após a coleta, os dados são armazenados em uma lista e exportados para uma planilha chamada `proxies.xlsx` por meio da biblioteca OpenPyXL.

A primeira linha da tabela é ignorada porque representa o cabeçalho da página. Cada uma das demais linhas é processada individualmente para obter os dados necessários.

## Objetivo

Automatizar a coleta de informações de proxies disponíveis em uma página web e organizar os resultados em uma planilha Excel.

O projeto busca substituir a cópia manual dos dados, reduzir erros de digitação e facilitar a organização das informações coletadas.

## Funcionalidades

- Inicialização automática do navegador Chromium;
- Acesso automático à página de proxies;
- Localização de todas as linhas da tabela;
- Exclusão do cabeçalho durante a leitura;
- Extração do endereço IP;
- Extração da porta;
- Extração do protocolo;
- Armazenamento temporário dos dados em uma lista;
- Criação automática de uma planilha Excel;
- Criação do cabeçalho da planilha;
- Inserção de todos os proxies coletados;
- Salvamento automático do arquivo `proxies.xlsx`;
- Encerramento do navegador após a coleta.

## Tecnologias utilizadas

- Python
- Playwright
- OpenPyXL
- Chromium
- Microsoft Excel ou outro programa compatível com arquivos `.xlsx`

## Formato da planilha

A automação gera um arquivo chamado:

```text
proxies.xlsx
```

A planilha contém as seguintes colunas:

| IP | Porta | Protocolo |
|---|---|---|
| Endereço do servidor | Porta utilizada | Tipo de protocolo |

Exemplo:

| IP | Porta | Protocolo |
|---|---:|---|
| 192.168.1.10 | 8080 | HTTP |
| 192.168.1.20 | 3128 | HTTPS |
| 192.168.1.30 | 1080 | SOCKS5 |

Os dados presentes na planilha dependem das informações disponíveis no site no momento da execução.

## Estrutura do projeto

```text
BotVarreduraDePlanilha/
├── BotVarreduraPlanilha.py
├── proxies.xlsx
├── README.md
├── COPYRIGHT.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

### Arquivos do projeto

- `BotVarreduraPlanilha.py`: arquivo principal que realiza a coleta e cria a planilha;
- `proxies.xlsx`: arquivo gerado automaticamente após a execução;
- `README.md`: documentação do projeto;
- `COPYRIGHT.md`: informações relacionadas à autoria e aos direitos autorais;
- `LICENSE`: condições de utilização do projeto;
- `requirements.txt`: bibliotecas externas necessárias;
- `.gitignore`: arquivos e pastas que não devem ser enviados ao GitHub.

## Pré-requisitos

Antes de executar o projeto, tenha instalado:

- Python;
- Git;
- Visual Studio Code ou outro editor;
- As bibliotecas presentes no arquivo `requirements.txt`;
- O navegador Chromium utilizado pelo Playwright;
- Acesso à internet;
- Um programa compatível com arquivos Excel.

## Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/coletor-de-proxies.git
```

Entre na pasta:

```bash
cd coletor-de-proxies
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Instale o navegador Chromium do Playwright:

```bash
python -m playwright install chromium
```

## Como executar

Execute o arquivo principal:

```bash
python ColetorProxies.py
```

Durante a execução, o programa irá:

1. Acessar a página de proxies;
2. Localizar a tabela;
3. Extrair IP, porta e protocolo;
4. Criar uma nova planilha;
5. Inserir os dados coletados;
6. Salvar o arquivo `proxies.xlsx`.

Ao concluir, a planilha será criada na mesma pasta do código.

## Fluxo da automação

1. O Playwright é inicializado.
2. O navegador Chromium é aberto em modo invisível.
3. A página de proxies é acessada.
4. Todas as linhas da tabela são localizadas.
5. A primeira linha é ignorada por representar o cabeçalho.
6. Cada linha restante é processada.
7. As células da linha são localizadas.
8. O endereço IP é extraído.
9. A porta é extraída.
10. O protocolo é extraído.
11. Os dados são adicionados à lista `proxies`.
12. O navegador é fechado.
13. Uma nova planilha Excel é criada.
14. O cabeçalho é inserido.
15. Os proxies coletados são adicionados à planilha.
16. O arquivo é salvo como `proxies.xlsx`.

## Limitações atuais

- O projeto depende da disponibilidade da página utilizada;
- Alterações na estrutura da tabela podem exigir atualização do código;
- A automação considera que IP, porta e protocolo estão nas posições esperadas;
- O arquivo `proxies.xlsx` é substituído quando o programa é executado novamente;
- O projeto não verifica se os dados coletados estão duplicados;
- Não existe tratamento específico para falhas de conexão;
- Não existe validação das linhas antes da extração;
- O projeto não testa se os proxies estão funcionando;
- O navegador é executado de forma invisível;
- Não existe interface gráfica nesta versão.

## Autor

Desenvolvido por **Fabio** como projeto de estudo em Python, automação web, Playwright, extração de dados e criação de planilhas com OpenPyXL.

## Direitos autorais

Copyright © 2026 FabioDevPTch. Todos os direitos reservados.

Este projeto e seu código-fonte são de autoria de FabioDevPTch.

O repositório está disponível publicamente para fins de estudo, demonstração técnica e apresentação de portfólio.

A disponibilização pública não concede automaticamente permissão para reprodução, modificação, distribuição ou comercialização do projeto.

Consulte o arquivo [`COPYRIGHT.md`](COPYRIGHT.md) para conhecer as informações completas sobre os direitos autorais.

## Licença

Este projeto possui uma licença proprietária e não é distribuído sob uma licença de código aberto.

Não é permitida a reprodução, modificação, distribuição, comercialização, sublicenciamento ou utilização total ou parcial do projeto sem autorização prévia e expressa do autor.

Consulte o arquivo [`LICENSE`](LICENSE) para conhecer os termos completos.

Copyright © 2026 Fabio. Todos os direitos reservados.
