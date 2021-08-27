from clickhouse_driver import Client
from clickhouse_driver import errors
import pandas as pd


class ClickHouse:

    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password
        self.client = ''

        self.get_client()

    def get_client(self):
        """Подключение к серверу"""
        self.client = Client(
            host=self.host,
            port=self.port,
            user=self.username,
            password=self.password,
            database=self.database
        )

    def test_connection(self):
        """Проверка соединения. Выводит список таблиц БД"""
        print(self.client.execute('SHOW TABLES'))
        
    def clear_table(self, table_name):
        """Удаляет данные из таблицы"""
        self.client.execute(f'TRUNCATE TABLE {table_name};')
        
    def upload_data(self, query, records = ''):
        """Вставляет данные в таблицу. records - вложенный список с данными"""
        self.client.execute(query, records)
    
    def run_query(self, query):
        """Выполнение запроса на сервере"""
        self.client.execute(query)
        
    def get_clickhouse_data(self, query, connection_timeout = 1500):
        try:
            r = self.client.execute(query, with_column_types=True)
        except errors.ServerException as E:
            print(E)
        
        return r

    def get_clickhouse_df(self, query, connection_timeout = 1500):
        data = self.get_clickhouse_data(query, connection_timeout=connection_timeout) 
        
        column_names = []
        for column in data[1]:
            column_names.append(column[0])
        df = pd.DataFrame(data[0], columns=column_names)
        return df
       
    def insert_data_from_df(self, table_name, data_df):
        self.client.execute(f'''INSERT INTO {table_name} VALUES''', data_df.to_dict('records'))