import requests
import xml.etree.cElementTree as ET

import config

def get_xml_yandex(query):
    params = config.params
    params['query'] = query
    response = requests.get('https://xmlproxy.ru/search/xml',params=params)
    return ET.fromstring(response.content)


def get_position_yandex(query):
    query = str(query)
    xml_doc = get_xml_yandex(query)
    table_1 = {}
    counter = 0
    project_url = config.PROJECT_URL
    table_1['response_date'] = xml_doc.find('response').attrib['date']
    table_1['query'] = query
    for docs in xml_doc.iter('doc'):
        counter += 1
        if project_url in docs.find('domain').text:
            table_1['url_page'] = docs.find('url').text
            table_1['position'] = counter
            break
        else:
            table_1['url_page'] = None
            table_1['position'] = None
    return table_1

print(get_position_yandex('купить молоко'))