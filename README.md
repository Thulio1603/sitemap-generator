## Como Usar

- Crie uma planilha no formato XLS com todas as URLs que você deseja incluir no sitemap. Coloque as URLs na primeira coluna (coluna A) da planilha.

- Salve o arquivo da planilha na raiz do repositório com o nome de "planilha.xls".

- Certifique-se de ter o Python instalado em seu sistema. Caso não tenha, você pode fazer o download e instalar a partir do site oficial: https://www.python.org/.

- Instale a biblioteca Pandas executando o seguinte comando em seu terminal:
  `  pip install pandas`

- Execute o seguinte comando no terminal para gerar o sitemap.xml:
  ` python generate-sitemap.py`
- O arquivo "sitemap.xml" será gerado na raiz do repositório, contendo as URLs presentes na planilha.xlsx, ou se preferir no arquivo generate-sitemap.py na linha 42 vc pode alterar o nome do arquivo.
