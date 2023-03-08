import sqlite3 as sl

class datahandler:
    def dit_str(self, d:dict):
        g = ''
        for i in d:
            g = g + f"\n{i} {d.get(i)},"
        return g

    def __init__(self, file: str, **kwargs):
        '''
        This class is used to handle data with SQLite. 
        Initializing an object with a `.db` file name and 
            directory will create a new database file in that directory. 
        By passing a `Table_name` and `columns`: dirt where the 
            columns are the keys and the data types are the values, 
            a new table will be created in the database. 
        An `id` column will always be added automatically to the table.
        '''
        self.Tables = {}
        self.file = file
        self.con = sl.connect(file)
        if 'Table_name' in kwargs:
            if ('columns' not in kwargs) or (self.table_exist(kwargs['Table_name'])):
                if self.table_exist(kwargs['Table_name']):
                    self.Tables[kwargs['Table_name']] = {item[1]: item[2] for item in self.get_columns(kwargs['Table_name'])[1:]}
            elif 'columns' in kwargs:
                if not self.table_exist(kwargs['Table_name']):
                    self.Tables[kwargs['Table_name']] =  kwargs['columns']
                    self.create_table(kwargs['Table_name'], kwargs['columns'])

    def create_table(self, Table_name: str, columns: dict):
        '''
        It uses to create and new Table under main `.db` file
        By passing a `Table_name` and `columns`: dirt where the 
            columns are the keys and the data types are the values,
            option for data type are `INTEGER`, `TEXT` 
            or more at https://docs.python.org/3/library/sqlite3.html#sqlite-and-python-types
        '''
        self.Tables[Table_name] = columns
        if not self.table_exist(Table_name):
            with self.con:
                self.con.execute(f"CREATE TABLE {Table_name} (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,{self.dit_str(columns)[:-1]});")
        
    def add_data(self, to_table: str, *args):
        '''
        Adds data to a table.
        '''
        with self.con:
            cursor = self.con.cursor()
            query = f"INSERT INTO {to_table} ({', '.join(self.Tables[to_table])}) VALUES (?, ?)"
            cursor.executemany(query, args)

    def get(self, from_table:str):
        '''
        Returns all data from a table.
        '''
        with self.con:
            data = self.con.execute(f"SELECT* FROM {from_table}")
        return list(data)
    
    def table_exist(self, name: str):
        '''
        Checks whether a table with the given name exists in the database.
        '''
        cursor = self.con.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{name}'")
        table_exists = cursor.fetchone()
        return table_exists
    
    def get_columns(self, Table:str):
        '''
        Returns a list of column data for a given table.
        '''
        cur = self.con.cursor()
        cur.execute(f"PRAGMA table_info({Table});")
        columns = cur.fetchall()
        return columns


if __name__ == '__main__':
    dh = datahandler

    temp = dh('Temp.db', Table_name='Temp', columns={'name': 'TEXT', 'age': 'INTEGER'})
    temp.add_data('Temp',('Kreem', 22))
    temp.get(from_table='Temp')
    temp.table_exist('Temp')
    temp.get_columns(Table='Temp')
    temp.create_table('dir', {'fig':'TEXT', 'start':'INTEGER'})
    temp.add_data('dir', ('c/windows/scripts', 3.265), ('d/softwer/win32', 1.29))
    temp.get(from_table='dir')
    temp.get_columns('dir')
    temp.con.close()