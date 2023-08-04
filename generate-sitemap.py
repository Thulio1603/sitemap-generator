import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime


def create_site_map(urls: []):
    root = ET.Element(
        "urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    for url in urls:
        url_element = ET.SubElement(root, "url")
        loc = ET.SubElement(url_element, "loc")
        loc.text = url
        lastmod = ET.SubElement(url_element, "lastmod")
        data_atual = datetime.now()
        lastmod.text = data_atual.strftime('%Y-%m-%d')
        priority = ET.SubElement(url_element, "priority")
        priority.text = '0.9'

    tree = ET.ElementTree(root)
    tree.write("sitemap.xml", encoding="utf-8", xml_declaration=True)


def get_urls(file_path):
    url = []

    try:
        # Carregar o arquivo XLS
        df = pd.read_excel(file_path)

        # Iterar sobre as colunas e imprimir os dados
        for col in df.columns:
            for data in df[col]:
                url.append(data)
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

    return url


if __name__ == "__main__":
    arquivo_xls = "planilha.xlsx"
    urls = get_urls(arquivo_xls)
    create_site_map(urls)
