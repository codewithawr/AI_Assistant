import sqlite3 as sl

class datahandler:
    def dit_str(self, d):
        g = ''
        for i in d:
            g = g + f"\n{i} {d.get(i)},"
        return g
    
    def __init__(self, file, **kwargs):
        print(1)
        self.file = file
        self.con = sl.connect(file)
        if 'Table_name' in kwargs:
            self.Table = kwargs['Table_name']

            if ('columns' not in kwargs) or (self.table_exist(kwargs['Table_name'])):
                if self.table_exist(kwargs['Table_name']):
                    self.columns = {item[1]: item[2] for item in self.get_columns(self.Table)[1:]}

            elif 'columns' in kwargs:
                if not self.table_exist(kwargs['Table_name']):
                    self.columns = kwargs['columns']
                    self.create_table(self.Table, self.columns)

    def create_table(self, Table_name, columns):
        self.Table = Table_name
        # self.columns = {item[1]: item[2] for item in self.get_columns()}
        self.columns = columns
        if not self.table_exist(Table_name):
            with self.con:
                print(f"CREATE TABLE {Table_name} (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,{self.dit_str(columns)[:-1]});")
                self.con.execute(f"CREATE TABLE {Table_name} (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,{self.dit_str(columns)[:-1]});")
        
    def add_data(self, args):
        cursor = self.con.cursor()
        with self.con:
            print(f"INSERT INTO {self.Table} ({', '.join(self.columns)}) VALUES (?, ?)", args)
            cursor.executemany(f"INSERT INTO {self.Table} ({', '.join(self.columns)}) VALUES (?, ?)", args)

    def get(self):
        with self.con:
            data = self.con.execute(f"SELECT* FROM {self.Table}")
        return list(data)
    
    def table_exist(self, name):
        cursor = self.con.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{name}'")
        table_exists = cursor.fetchone()
        return table_exists
    
    def get_columns(self, Table):
        cur = self.con.cursor()
        cur.execute(f"PRAGMA table_info({Table});")
        columns = cur.fetchall()
        return columns

if __name__ == '__main__':
    d = datahandler('dp.db', Table_name = 'Temp')
    # d.add_data([
    #     ( None, 'Rana', 'k')
    #     ])
    # print(d.get_columns('Temp'))
    # print(d.get())
    d.con.close()