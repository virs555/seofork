import database

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
db.add_project('lenta.com') #Добавляем проект 1
db.add_project('perekrestok.com') #Добавляем проект 2
db.del_project('perekrestok.com') # Удаляем проект 2
db.add_project_values(query_data_list, 'lenta.com') # Добавляем запросы к проекту lenta.com
db.add_yandex_data('lenta.com') # Снимаем данные парсером для запросов проекта lenta.com