import os
import psycopg2
from psycopg2 import Error
from http.server import BaseHTTPRequestHandler, HTTPServer

def run(server_class = HTTPServer, handler_class = BaseHTTPRequestHandler):
    server_address = ('', 80)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()

            connection = psycopg2.connect (user = "user", password = "password", host = os.environ['DB_HOST'], port = os.environ['DB_PORT'], database = "db_ps")
            curs = connection.cursor()

            # Создание таблицы User
            #create_table_query = '''CREATE TABLE usr (ID INT PRIMARY KEY   NOT NULL, NAME VARCHAR, EMAIL VARCHAR); '''
            #curs.execute(create_table_query)
            #connection.commit()

            #insert_query = """ INSERT INTO usr (ID, NAME, EMAIL) VALUES (1, 'Роман', 'Роман@mail.ru'),
                                                                     #(2, 'Данил', 'Данил@mail.ru')"""
            #curs.execute(insert_query)
            #connection.commit()

            # Получить результат
            curs.execute("SELECT * from usr")
            record = curs.fetchall()
            if self.path == '/GET/users':
                for row in record:
                    self.wfile.write(f'ID = {row[0]}, NAME = {row[1]}, EMAIL = {row[2]}\n'.encode())

            for row in record:   
                if self.path == f'/GET/users/{row[0]}':
                    postgresql_select_query = "SELECT * FROM usr WHERE ID = %s"
                    curs.execute(postgresql_select_query, (row[0],))
                    mobile_records = curs.fetchall()  
                    self.wfile.write(f'ID = {row[0]}, NAME = {row[1]}, EMAIL = {row[2]}\n'.encode()) 
            
        except (Exception, Error) as error:
            self.wfile.write("DDDDDDDDDDDD")
            print("Ошибка при работе с PostgreSQL", error)


run(handler_class=myHandler)