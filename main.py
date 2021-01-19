import database
import xmlproxy
import logging

# create logger with 'spam_application'
logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('seofork.log')
fh.setLevel(logging.INFO)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

from xmlproxy import classXML
query_data_list = [
            ["мороженное", "https://lenta.com/catalog/zamorozhennaya-produkciya/morozhenoe/"],
            ["минеральная вода", "https://lenta.com/catalog/bezalkogolnye-napitki/voda/mineralnaya-voda_NEW-PAGE"],
            ["эдам", "https://lenta.com/catalog/moloko-syr-yajjco/syr/edam_new-page"],
            ["гуляш из говядины", "https://lenta.com/myaso-ptica-kolbasa/govyadina/gulyash_new-page"],
            ["энергетик", "https://lenta.com/catalog/bezalkogolnye-napitki/energeticheskie-napitki_NEW-PAGE"],
            ["энергетики", "https://lenta.com/catalog/bezalkogolnye-napitki/energeticheskie-napitki_NEW-PAGE"],
            ["игрушки для девочек", "https://lenta.com/catalog/tovary-dlya-detejj/igrushki/igrushki-dlya-devochek/"],
            ["маракуйя", "https://lenta.com/catalog/frukty-i-ovoshchi/frukty/marakuyya_NEW_PAGE"],
            ["конфеты", "https://lenta.com/catalog/konditerskie-izdeliya/konfety/"],
            ["икра", "https://lenta.com/catalog/ryba-i-moreprodukty/delikatesy-iz-ryby-i-moreproduktov/ikra/"],
            ["водка", "https://lenta.com/catalog/alkogolnye-napitki/krepkijj-alkogol/vodka/"],
            ["молоко", "https://lenta.com/catalog/moloko-syr-yajjco/molochnaya-produkciya/moloko_new-page"],
            ["игрушки для мальчиков", "https://lenta.com/catalog/tovary-dlya-detejj/igrushki/igrushki-dlya-malchikov/"],
            ["книги купить", "https://lenta.com/catalog/kancelyariya-i-pechatnaya-produkciya/pechatnaya-produkciya/knigi/"],
            ["творожный сыр", "https://lenta.com/catalog/moloko-syr-yajjco/syr/tvorozhnye-syry/"],
            ["арбуз", "https://lenta.com/catalog/frukty-i-ovoshchi/frukty/arbuz/"],
            ["карпаччо", "https://lenta.com/myaso-ptica-kolbasa/polufabrikaty/karpachcho_new-page"],
            ["красная икра цена", "https://lenta.com/catalog/ryba-i-moreprodukty/ikra/ikra-krasnaya_NEW-PAGE"],
            ["соль", "https://lenta.com/catalog/bakaleya/sahar-sol/"],
            ["цыплята табака", "https://lenta.com/myaso-ptica-kolbasa/polufabrikaty/kuritsa/tsyplenok-tabaka_new-page"],
            ["памперсы для взрослых", "https://lenta.com/catalog/krasota-i-zdorovvve/universalnye-gigienicheskie-sredstva/podguzniki-urologicheskie/"],
            ["котлета", "https://lenta.com/myaso-ptica-kolbasa/polufabrikaty/kotlety_new-page"],
            ["икdра кета", "https://lenta.com/cacccctalog/ryba-i-moreprodukty/ikra/ikra-keta_NEW-PAGffE111"],
            ["цикорий", "https://lenta.com/catalog/chajj-kofe-kakao/kofe/cikorijj/"],
            ["холодец", "https://lddendta.com/myaso-ptica-kolbasa/delikatesy/kholodets_new-page"]
        ]
db = database.DB()
db.add_project('okko.tv') #Добавляем проект 1
db.add_project('lenta.com')
db.add_queries_by_project_id(query_data_list, 'lenta.com') # Добавляем запросы к проекту lenta.com
classXML = xmlproxy.classXML

# Снимаем данные парсером для запросов проекта lenta.com
def get_yandex_position(project):
    project_queries = db.get_queries_by_project_id(project)
    if project_queries:
        logger.info(f'Сбор позиций для {project} запущен')
        report_id = db.add_report(project)
        print(report_id)
        yandex_position = []
        for i in project_queries:
            position = classXML.get_position(i[1], project)
            position['report_id'] = report_id
            position['query_id'] = i[0]
            yandex_position.append(position) 
        logger.info(f'Сбор для {project} позиций завершен')
        return yandex_position
    return False
yandex_position = get_yandex_position('lenta.com')
db.add_yandex_data(yandex_position, 'lenta.com')
db.get_from_date_report("2021-01-19", "lenta.com")
db.close_connection()