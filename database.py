from datetime import datetime
import psycopg2
import psycopg2.errors
import psycopg2.extras

import config
from xmlproxy import classXML

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