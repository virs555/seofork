import requests
import xml.etree.cElementTree as ET

import config

XML_PROXY = 'https://xmlproxy.ru/search/xml'

class XmlParser:

    def __init__(self):
        self.params = config.params
        self.xml_proxy = XML_PROXY 

    def _get_xml(self, query, domain, region):
        params = self.params
        params['query'] = query
        params['lr'] = region
        params['domain'] = domain
        try:
            response = requests.get(self.xml_proxy, params=params)
            response.raise_for_status()
            return ET.fromstring(response.content)
        except(requests.RequestException):
            print('Ошибка соединения с сервером данных')
            return False


    def get_position(self, query, domain, region='213'):
        query = str(query)
        xml_doc = self._get_xml(query, domain, region)
        if xml_doc:
            if xml_doc[0][0].tag == 'error':
                print (f"{xml_doc[0][0].attrib['code']} {xml_doc[0][0].text}")
            else:    
                result_dic = {}
                counter = 0
                domain = domain
                result_dic['response_date'] = xml_doc.find('response').attrib['date']
                result_dic['query'] = query
                for docs in xml_doc.iter('doc'):
                    counter += 1
                    result_dic['region'] = region
                    result_dic['domain'] = domain
                    if domain in docs.find('domain').text:
                        result_dic['url_page'] = docs.find('url').text
                        result_dic['position'] = counter
                        break
                    else:
                        result_dic['url_page'] = None
                        result_dic['position'] = None
                return result_dic
        return False

classXML = XmlParser()
print(classXML.get_position('купить молоко', 'lenta.com'))
