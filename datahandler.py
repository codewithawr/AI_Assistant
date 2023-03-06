import sqlite3 as sl

class datahandler:
    def dit_str(self, d):
        g = ''
        for i in d:
            g = g + f"\n{i} {d.get(i)},"
        return g
    
    def __init__(self, file, Table_name, columns=dict):
        self.file = file
        self.Table = Table_name
        self.columns = ', '.join(columns)
        self.con = sl.connect(file)
        if not self.table_exist(Table_name):
            with self.con:
                self.con.execute(f"CREATE TABLE {Table_name} (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,{self.dit_str(columns)[:-1]});")

    def add_data(self, args):
        cursor = self.con.cursor()
        with self.con:
            cursor.executemany(f"INSERT INTO {self.Table} (id, {self.columns}) VALUES (?, ?, ?)", args)

    def get(self):
        with self.con:
            data = self.con.execute(f"SELECT* FROM {self.Table}")
        print(list(data))
    
    def table_exist(self, name):
        cursor = self.con.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{name}'")
        table_exists = cursor.fetchone()
        return table_exists


d = datahandler('chat.db', 'Temp', {'name' : "TEXT", 'age':"INTEGER"})
d.add_data([
    ( None, 'Rana', 'k')
    ])
d.get()
