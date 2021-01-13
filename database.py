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

        
    def get_project_id(self, project):
        self.cursor.execute(f"SELECT project_id FROM projects WHERE project='{project}'")
        try:
            project_id = str(self.cursor.fetchone()[0])
            return project_id
        except(TypeError):
            print('Ошибка проекта! Добавьте проект.')
            return False

    def add_queries_by_project_id(self, query_data_list, project):
        project_id = self.get_project_id(project)
        if project_id:
            #Добавляем запросы в таблицу. Складываем id добавленых и уже существующих в query_list, добавляем связку query_id-project_id в таблицу.
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
                url = i[1]
                project_url = project_id, query_id, url
                self.cursor.execute("INSERT INTO project_url (project_id, query_id, url) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING", project_url)
                self.conn.commit()
        return False

    def get_queries_by_project_id(self, project):
        project_id = self.get_project_id(project)
        if project_id:
            self.cursor.execute("""
                                SELECT queries.query_id, queries.query FROM queries 
                                LEFT JOIN project_url
                                ON queries.query_id = project_url.query_id
                                WHERE project_url.project_id = (%s);
            """, (project_id,))
            project_queries = self.cursor.fetchall()
            return project_queries
        return False

    def add_report(self, project):
        project_id = self.get_project_id(project)
        if project_id:
            date = datetime.now().date()
            report_data = [project_id, date]
            self.cursor.execute("INSERT INTO reports (project_id, report_date) VALUES (%s, %s) RETURNING report_id;", report_data)
            report_id = self.cursor.fetchone()
            return report_id[0]
        return False

    def add_yandex_data(self, yandex_position, project):
        if yandex_position:
            self.add_report(project)
            print(f'---------------------{yandex_position}')
            for i in yandex_position:
                self.cursor.execute("INSERT INTO yandex_results (query, report_id, position, url_page, query_id) VALUES (%(query)s, %(report_id)s ,%(position)s, %(url_page)s, %(query_id)s)", i)
            self.conn.commit()
        return False