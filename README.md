Sitemap Generator

  Descrição
  O Sitemap Generator é uma ferramenta desenvolvida em Python que permite a criação de um arquivo sitemap.xml a partir de uma lista de URLs fornecida. Esse sitemap.xml é uma valiosa ferramenta para otimizar a indexação do seu site pelos mecanismos de busca, melhorando assim sua visibilidade nos resultados de pesquisa.
  
  Como Usar
  Para utilizar o Sitemap Generator, siga os passos abaixo:
  
  Crie uma planilha no formato XLS com todas as URLs que você deseja incluir no sitemap. Coloque as URLs na primeira coluna (coluna A) da planilha.
  
  Salve o arquivo da planilha na raiz do repositório com o nome de "planilha.xls".
  
  Certifique-se de ter o Python instalado em seu sistema. Caso não tenha, você pode fazer o download e instalar a partir do site oficial: https://www.python.org/.
  
  Instale a biblioteca Pandas executando o seguinte comando em seu terminal: 
    pip install pandas
    
  Execute o seguinte comando no terminal para gerar o sitemap.xml:
    python generate-sitemap.py
  
  O arquivo "sitemap.xml" será gerado na raiz do repositório, contendo as URLs presentes na planilha XLS.
