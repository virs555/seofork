from datetime import datetime
import psycopg2
import psycopg2.errors
import psycopg2.extras

import config
from xmlproxy import classXML

query_data_list = [
            ["мороженое", "https://lenta.com/catalog/zamorozhennaya-produkciya/morozhenoe/1"],
            ["минеральный вода", "https://lenta.com/catalog/bezalkogolnye-napitki/voda/mineralnaya-voda_NEW-PAGE"],
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
            ["памперсы для взрослых", "https://lenta.com/catalog/krasota-i-zdorove/universalnye-gigienicheskie-sredstva/podguzniki-urologicheskie/"],
            ["котлета", "https://lenta.com/myaso-ptica-kolbasa/polufabrikaty/kotlety_new-page"],
            ["икра кета", "https://lenta.com/catalog/ryba-i-moreprodukty/ikra/ikra-keta_NEW-PAGE"],
            ["цикорий", "https://lenta.com/catalog/chajj-kofe-kakao/kofe/cikorijj/"],
            ["холодцы", "https://lenta.com/myaso-ptica-kolbasa/delikatesy/kholodets_new-page"],
            ["холодц", "https://lecnta.com/myaso-ptica-kolbasa/delikatesy/kholodets_new-page"]
        ]

class DB:
    
    def __init__(self):
        self.conn = None
        try:
            self.conn = psycopg2.connect(dbname=config.DB_NAME, user=config.DB_USER,
                                        password=config.DB_PASS, host=config.DB_HOST)
            self.cursor = self.conn.cursor()                     
            print('Соединение с PostgreSQL установлено!')
        except psycopg2.OperationalError:
            print('Ошибка соединения с PostgreSQL')

    def add_project(self, project):
        try:
            sql = "INSERT INTO projects (project) VALUES (%s)"
            self.cursor.execute(sql, (project,))
            self.conn.commit()
            print('Проект успешно добавлен!')
        except psycopg2.errors.UniqueViolation:
            print('Проект уже существует!')
            self.conn.rollback()

    def del_project(self, project):
        sql = "DELETE FROM projects WHERE project = (%s)"
        self.cursor.execute(sql, (project,))
        self.conn.commit()

    def add_project_values(self, query_data_list, project):
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
            ["арбузы", "https://lenta.com/catalog/frukty-i-ovoshchi/frukty/arbuz/"],
            ["карпаччо", "https://lenta.com/myaso-ptica-kolbasa/polufabrikaty/karpachcho_new-page"],
            ["красная икра цена", "https://lenta.com/catalog/ryba-i-moreprodukty/ikra/ikra-krasnaya_NEW-PAGE"],
            ["соль", "https://lenta.com/catalog/bakaleya/sahar-sol/"],
            ["цыплята табака", "https://lenta.com/myaso-ptica-kolbasa/polufabrikaty/kuritsa/tsyplenok-tabaka_new-page"],
            ["памперсы для взрослых", "https://lenta.com/catalog/krasota-i-zdorovvve/universalnye-gigienicheskie-sredstva/podguzniki-urologicheskie/"],
            ["котлеты", "https://lenta.com/myaso-ptica-kolbasa/polufabrikaty/kotlety_new-page"],
            ["икра кета", "https://lenta.com/cacccctalog/ryba-i-moreprodukty/ikra/ikra-keta_NEW-PAGffE111"],
            ["цикорий", "https://lenta.com/catalog/chajj-kofe-kakao/kofe/cikorijj/"],
            ["холодцы", "https://lddendta.com/myaso-ptica-kolbasa/delikatesy/kholodets_new-page"]
        ]
        #Получаем id проекта из таблицы с проектами
        self.cursor.execute(f"SELECT project_id FROM projects WHERE project='{project}'")
        try:
            project_id = str(self.cursor.fetchone()[0])
        except(TypeError):
            print('Ошибка проекта! Добавьте проект.')
            return False

        #Добавляем запросы в таблицу. Складываем id добавленых и уже существующих в self.query_list, добавляем связку query_id-project_id в таблицу.
        for i in query_data_list:
            query_project = [0,0]
            try:
                self.cursor.execute("INSERT INTO queries (query) VALUES (%s) RETURNING query_id;", [i[0]])
            except:
                self.conn.rollback()
                self.cursor.execute("SELECT query_id FROM queries WHERE query=(%s)", [i[0]])
            query_id = self.cursor.fetchone()
            query_project[0] = query_id
            query_project[1] = (project_id,)
            self.cursor.execute("INSERT INTO project_query (query_id, project_id) VALUES (%s, %s) ON CONFLICT DO NOTHING", query_project)
            project_query_id = query_id, project_id
            self.cursor.execute("SELECT project_query_id FROM project_query WHERE query_id=%s AND project_id = (%s)", project_query_id)
            project_url = [i[1], self.cursor.fetchone()]
            self.cursor.execute("INSERT INTO project_url (url, project_query_id) VALUES (%s, %s) ON CONFLICT DO NOTHING", project_url)
            self.conn.commit()


    def del_project_values(self, query_data_list, project):
        pass

    def add_yandex_data(self, project):
        date = datetime.now().date()
        self.cursor.execute(f"SELECT project_id FROM projects WHERE project='{project}'")
        project_id = self.cursor.fetchone()
        self.cursor.execute("""
                             SELECT queries.query_id, queries.query FROM queries 
                             LEFT JOIN project_query
                             ON queries.query_id = project_query.query_id
                             WHERE project_query.project_id = (%s);
        """, project_id)
        project_queries = self.cursor.fetchall()
        result = []
        report_data = [project_id, date]
        self.cursor.execute("INSERT INTO reports (project_id, report_date) VALUES (%s, %s) RETURNING report_id;", report_data)
        report_id = self.cursor.fetchone()
        for i in project_queries:
           result = classXML.get_position(i[1], project)
           result['report_id'] = report_id[0]
           result['query_id'] = i[0]
           print(result)
           self.cursor.execute("INSERT INTO yandex_results (query, report_id, position, url_page, query_id) VALUES (%(query)s, %(report_id)s ,%(position)s, %(url_page)s, %(query_id)s)", result)
        self.conn.commit()      

    # def get_data_by_project(self, date='2021-01-11', project='lenta.com'):
    #     self.cursor.execute(f"SELECT project_id FROM projects WHERE project='{project}'")
    #     project_id = self.cursor.fetchone()
    #     self.cursor.execute("""
    #                          SELECT queries.query_id FROM queries 
    #                          LEFT JOIN project_query
    #                          ON queries.query_id = project_query.query_id
    #                          WHERE project_query.project_id = (%s)
    #                          LEFT JOIN 
                             
    #     """, project_id)
    #     print(self.cursor.fetchall())

db = DB()
#db.add_project('ozon.ru')
#db.del_project('ozon.ru')
#db.add_project_values(query_data_list, 'lenta.com')
#db.add_yandex_data()
#db.get_data_by_project()

