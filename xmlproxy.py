import requests
import xml.etree.cElementTree as ET

import config


class XmlParser:

    def __init__(self, params=config.params_yandex):
        pass


    def __get_xml_yandex(self, query, domain, region):
        params = config.params_yandex
        params['query'] = query
        params['lr'] = region
        params['domain'] = domain
        response = requests.get(config.XML_PROXY, params=params)
        return ET.fromstring(response.content)




    def get_position_yandex(self, query, domain, region='213'):
        query = str(query)
        xml_doc = self.__get_xml_yandex(query, domain, region)
        result_dic = {}
        counter = 0
        domain = domain
        result_dic['response_date'] = xml_doc.find('response').attrib['date']
        result_dic['query'] = query
        for docs in xml_doc.iter('doc'):
            counter += 1
            if domain in docs.find('domain').text:
                result_dic['url_page'] = docs.find('url').text
                result_dic['position'] = counter
                result_dic['region'] = region
                result_dic['domain'] = domain
                break
            else:
                result_dic['url_page'] = None
                result_dic['position'] = None
        return result_dic
        
classP = XmlParser()
print(classP.get_position_yandex('купить молоко', 'lenta.com'))