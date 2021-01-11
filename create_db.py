import psycopg2

commands = (
    """
    CREATE TABLE projects(
        project_id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
        project character varying NOT NULL,
        PRIMARY KEY (project_id),
        UNIQUE (project) 
    ) 
    """,

    """
    CREATE TABLE queries(
        query_id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
        query character varying NOT NULL,
        PRIMARY KEY (query_id),
        UNIQUE (query) 
    ) 
    """,

    """
    CREATE TABLE project_query(
        project_query_id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
        query_id integer NOT NULL,
        project_id integer NOT NULL,
        PRIMARY KEY (project_query_id),
        UNIQUE (query_id, project_id),
        FOREIGN KEY (project_id)
            REFERENCES projects (project_id)
            ON UPDATE CASCADE 
            ON DELETE CASCADE,
        FOREIGN KEY (query_id)
            REFERENCES queries (query_id)
            ON UPDATE CASCADE 
            ON DELETE CASCADE
    ) 
    """,
    """
    CREATE TABLE project_url(
        project_url_id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
        url character varying NOT NULL,
        project_query_id integer NOT NULL,
        PRIMARY KEY (project_url_id),
        UNIQUE (project_query_id, url),
        FOREIGN KEY (project_query_id)
            REFERENCES project_query (project_query_id)
            ON UPDATE CASCADE 
            ON DELETE CASCADE
        )
    """,  

    """
    CREATE TABLE reports(
        report_id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
        report_date character varying NOT NULL,
        project_id integer NOT NULL,
        PRIMARY KEY (report_id),
        FOREIGN KEY (project_id)
            REFERENCES projects (project_id)
            ON UPDATE CASCADE 
            ON DELETE CASCADE
        )
    """,

    """
    CREATE TABLE yandex_results(
        yandex_result_id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
        query character varying NOT NULL,
        query_id integer NOT NULL,
        report_id integer NOT NULL,
        position character varying,
        url_page character varying,
        PRIMARY KEY (yandex_result_id),
        FOREIGN KEY (report_id)
            REFERENCES reports (report_id)
            ON UPDATE CASCADE 
            ON DELETE CASCADE
        )
    """
    )


try:
    conn = psycopg2.connect(dbname = "seofork", user = "postgres", password = "12345", host = "localhost", port = "5432")
except:
    print("I am unable to connect to the database") 

cur = conn.cursor()

for command in commands:
    cur.execute(command)

conn.commit() # <--- makes sure the change is shown in the database
conn.close()
cur.close()

