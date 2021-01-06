import psycopg2

import config

class DB:
    
    def __init__(self):
        self.conn = psycopg2.connect(dbname=config.DB_NAME, user=config.DB_USER,
                                     password=config.DB_PASS, host=config.DB_HOST)
        self.cursor = self.conn.cursor()                     

    def add_project(self):
        self.project = input()
        self.sql = "INSERT INTO projects (project) VALUES (%s)"
        self.cursor.execute(self.sql, (self.project,))
        self.conn.commit()
        self.cursor.close()

    def add_project_values(self):
        project_data_list = [
            ("мороженое", "https://lenta.com/catalog/zamorozhennaya-produkciya/morozhenoe/", "lenta.com"),
            ("минеральный вода", "https://lenta.com/catalog/bezalkogolnye-napitki/voda/mineralnaya-voda_NEW-PAGE", "lenta.com"),
            ("эдам", "https://lenta.com/catalog/moloko-syr-yajjco/syr/edam_new-page", "lenta.com"),
            ("гуляш из говядины", "https://lenta.com/myaso-ptica-kolbasa/govyadina/gulyash_new-page", "lenta.com"),
            ("энергетик", "https://lenta.com/catalog/bezalkogolnye-napitki/energeticheskie-napitki_NEW-PAGE", "lenta.com"),
            ("энергетики", "https://lenta.com/catalog/bezalkogolnye-napitki/energeticheskie-napitki_NEW-PAGE", "lenta.com"),
            ("игрушки для девочек", "https://lenta.com/catalog/tovary-dlya-detejj/igrushki/igrushki-dlya-devochek/", "lenta.com"),
            ("маракуйя", "https://lenta.com/catalog/frukty-i-ovoshchi/frukty/marakuyya_NEW_PAGE", "lenta.com"),
            ("конфеты", "https://lenta.com/catalog/konditerskie-izdeliya/konfety/", "lenta.com"),
            ("икра", "https://lenta.com/catalog/ryba-i-moreprodukty/delikatesy-iz-ryby-i-moreproduktov/ikra/", "lenta.com"),
            ("водка", "https://lenta.com/catalog/alkogolnye-napitki/krepkijj-alkogol/vodka/", "lenta.com"),
            ("молоко", "https://lenta.com/catalog/moloko-syr-yajjco/molochnaya-produkciya/moloko_new-page", "lenta.com"),
            ("игрушки для мальчиков", "https://lenta.com/catalog/tovary-dlya-detejj/igrushki/igrushki-dlya-malchikov/", "lenta.com"),
            ("книги купить", "https://lenta.com/catalog/kancelyariya-i-pechatnaya-produkciya/pechatnaya-produkciya/knigi/", "lenta.com"),
            ("творожный сыр", "https://lenta.com/catalog/moloko-syr-yajjco/syr/tvorozhnye-syry/", "lenta.com"),
            ("арбуз", "https://lenta.com/catalog/frukty-i-ovoshchi/frukty/arbuz/", "lenta.com"),
            ("карпаччо", "https://lenta.com/myaso-ptica-kolbasa/polufabrikaty/karpachcho_new-page", "lenta.com"),
            ("красная икра цена", "https://lenta.com/catalog/ryba-i-moreprodukty/ikra/ikra-krasnaya_NEW-PAGE", "lenta.com"),
            ("соль", "https://lenta.com/catalog/bakaleya/sahar-sol/", "lenta.com"),
            ("цыплята табака", "https://lenta.com/myaso-ptica-kolbasa/polufabrikaty/kuritsa/tsyplenok-tabaka_new-page", "lenta.com"),
            ("памперсы для взрослых", "https://lenta.com/catalog/krasota-i-zdorove/universalnye-gigienicheskie-sredstva/podguzniki-urologicheskie/", "lenta.com"),
            ("котлета", "https://lenta.com/myaso-ptica-kolbasa/polufabrikaty/kotlety_new-page", "lenta.com"),
            ("икра кета", "https://lenta.com/catalog/ryba-i-moreprodukty/ikra/ikra-keta_NEW-PAGE", "lenta.com"),
            ("цикорий", "https://lenta.com/catalog/chajj-kofe-kakao/kofe/cikorijj/", "lenta.com"),
            ("холодцы", "https://lenta.com/myaso-ptica-kolbasa/delikatesy/kholodets_new-page", "lenta.com")
        ]

        self.cursor.execute(f"SELECT project_id FROM projects WHERE project='lenta.com'")
        project_id = str(self.cursor.fetchone()[0])
        print(project_id)
        
        user_records = ", ".join(["%s"] * len(project_data_list))
        insert_query = (f"INSERT INTO queries (query, url, project_id) VALUES {user_records}")

        self.cursor.mogrify(insert_query, project_data_list)
        #self.conn.autocommit = True
        #self.conn.close()

db = DB()
db.add_project_values()