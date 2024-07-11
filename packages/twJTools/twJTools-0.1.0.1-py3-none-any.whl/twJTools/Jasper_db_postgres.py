# pip install psycopg2-binary

import json
import time
import psycopg2
from datetime import date


class DBConnect:

    def __init__(self, printlog=False, host=None, port=None, dbname=None, user=None, password=None):
        self.conn = None
        self.printlog = printlog

        if host:
            self.host = host
        if port:
            self.port = port
        if dbname:
            self.dbname = dbname
        if user:
            self.user = user
        if password:
            self.password = password

        self.connect()

    def check_type(self, value):
        if isinstance(value, date):
            # 將日期轉換為字符串格式
            value = value.strftime('%Y-%m-%d')
        elif isinstance(value, str):
            # 確保字串是 UTF-8 編碼
            value = value.encode('utf-8').decode('utf-8')
        return value

    def check_connect(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT 1")
                print(f"Connection SUEECSS")
        except (psycopg2.DatabaseError, psycopg2.OperationalError) as e:
            print(f"Connection error: {e}")
            self.close(commit=False)
            self.connect()

    def connect(self):
        if self.conn is None or self.conn.closed != 0:
            try:
                conn_string = f"host={self.host} port={self.port} dbname={self.dbname} user={self.user} password={self.password}"
                self.conn = psycopg2.connect(conn_string)
                print(f"Connected to {self.host}")
            except (psycopg2.DatabaseError, psycopg2.OperationalError) as e:
                print(f"Connection error: {e}")
                time.sleep(2)
                self.connect()

    def execute(self, sql, params=None):
        try:
            if self.printlog:
                print(f"Executing SQL: {sql}")
                if params:
                    print(f"Params: {params}")

            with self.conn.cursor() as cur:
                cur.execute(sql, params)
            self.commit()
        except psycopg2.DatabaseError as e:
            print(f"Execute error: {e}")

    import json
    from datetime import date

    # 在 DBConnect 類中的 query 方法後加入以下代碼
    def query(self, sql, params=None):
        try:
            if self.printlog:
                print(f"Executing SQL: {sql}")
                if params:
                    print(f"Params: {params}")

            with self.conn.cursor() as cur:
                cur.execute(sql, params)
                # 取得所有行的數據
                rows = cur.fetchall()

                # 取得列名稱列表
                columns = [desc[0] for desc in cur.description]

                # 將每行數據轉換為字典
                results = []
                for row in rows:
                    row_dict = {}
                    for col, value in zip(columns, row):
                        row_dict[col] = self.check_type(value)
                    results.append(row_dict)

                # 將結果轉換為 JSON 格式
                json_array = json.dumps(results, ensure_ascii=False)
                return json_array

        except psycopg2.DatabaseError as e:
            print(f"Query error: {e}")
            return "[]"

    def commit(self):
        self.conn.commit()

    def close(self, commit=True):
        if self.conn is not None:
            if commit:
                self.commit()

            try:
                self.conn.close()
                print(f"Connection to {self.host} closed")
            except psycopg2.DatabaseError as e:
                print(f"Error closing connection: {e}")
            finally:
                self.conn = None
