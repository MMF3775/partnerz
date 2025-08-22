from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_core.tools import tool
import os
from dotenv import load_dotenv
load_dotenv()

## static
## its better to use direct queries to DB to get datas
## its better to get url as state variable in invoke
order = {}
@tool()
def read_page(url: str):
    """
    Whit help of this tool you can read content of page
    :param url: url of webpage
    :return: content of webpage
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Authentication": f"bearer {os.getenv('AUTHENTICATION')}"
    }
    return UnstructuredURLLoader(urls=[url],
                          headers=headers,
                          mode='single',
                          encoding='utf-8',
                          strategy='hi_res',
                          extract_image_block_types=["Image", "Table"]).load()


@tool
def set_order(product_name,count):
    """
    add product in order

    :param product_name: name of product
    :param count: count of product
    :return:
    """
    if product_name in order.keys():
        order["product_name"] += count
    else:
        order["product_name"] = count

    return order