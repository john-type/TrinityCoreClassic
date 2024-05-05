#!/usr/bin/python3

import mysql.connector

class DbInstance:    
    def open(self, db_name):
        self._connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database=db_name
        )
        self._cursor = self._connection.cursor(buffered=True)
    
    def close(self):
        self._cursor.close()
    
    # query builder methods.
    
    def select_all(self, builder):
        built = builder.build_sql()
        self._cursor.execute(built['sql'], built['args'])
        columns = self._cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in self._cursor.fetchall()]
        return result
    
    def select_one(self, builder):
        built = builder.build_sql()
        self._cursor.execute(built['sql'], built['args'])
        columns = self._cursor.description
        row = self._cursor.fetchone()
        if row != None:
            result = [{columns[index][0]: column for index, column in enumerate(row)}]
            return result[0]

        return None
    
    def select_chunked(self, builder, size):
        has_more = True
        offset = 0
        
        while has_more:
            builder.limit(size, offset)
            rows = self.select_all(builder)
            
            for row in rows:
                yield row
            
            offset += size
            has_more = len(rows) > 0
            
    
    def upsert(self, builder):
        built = builder.build_sql()
        self._cursor.execute(built['sql'], built['args'])
        self._connection.commit()
        return self._cursor.lastrowid
    
    def delete(self, builder):
        built = builder.build_sql()
        self._cursor.execute(built['sql'], built['args'])
        self._connection.commit()
    
    # old style methods
        
    def get_rows_raw(self, query, args = None):
        self._cursor.execute(query, args)
        return self._cursor.fetchall()
    
    def get_row_raw(self, query, args = None):
        self._cursor.execute(query, args)
        return self._cursor.fetchone()
    
    def execute_raw(self, query, args = None):
        self._cursor.execute(query, args)
        self._connection.commit()
        
    def execute_many_raw(self, queries, args = None):
        for query in queries:
            self.execute_raw(query, args)
        
    def insert_raw(self, query, args = None):
        self._cursor.execute(query, args)
        self._connection.commit()
        return self._cursor.lastrowid
    
    def chunk_raw(self, query, size, callback):
        has_more = True
        offset = 0
        
        while has_more:
            results = self.get_rows_raw(query, (size, offset,))
            delta = 0

            for result in results:
                delta += callback(result)
                
            offset += delta
            offset += size
            has_more = len(results) > 0
            
    
tri_world = DbInstance()
tri_hotfix = DbInstance()
vm_world = DbInstance()

def OpenAll():
    tri_world.open('trinity_world')
    tri_hotfix.open('trinity_hotfixes')
    vm_world.open('vmangos_mangos')

    
def CloseAll():
    tri_world.close()
    tri_hotfix.close()
    vm_world.close()
        

class SelectQuery:   
    def __init__(self, table_name):
        self._table = table_name
        self._select = '*'
        self._condition = None
        self._limit = None
        self._offset = None
        self._orders = []
        self._groups = []
    
    def select(self, select_str):
        self._select = select_str
        return self
    
    def where(self, *args):
        if(len(args) == 1):
            self._condition = args[0]
        else:
            self._condition = Condition(*args)
        return self
    
    def order_by(self, orders):
        if type(orders) == str:
            orders = [orders]
        self._orders = orders
        return self
    
    def group_by(self, groups):
        if type(groups) == str:
            groups = [groups]
        self._groups = groups
        return self
    
    def limit(self, limit, offset = None):
        self._limit = limit
        self._offset = offset
        return self
    
    def build_sql(self):
        args = []
        sql = "SELECT " + self._select + " FROM " + self._table
        
        if self._condition != None:
            inner = self._condition.build_sql()
            sql += " WHERE " + inner['sql']
            args += inner['args']
            
        if len(self._groups) > 0:
            sql += " GROUP BY " + ', '.join(self._groups)
            
        if len(self._orders) > 0:
            sql += " ORDER BY " + ', '.join(self._orders)
            
        if self._limit != None:
            sql += " LIMIT " + str(self._limit)
            
        if self._offset != None:
            sql += " OFFSET " + str(self._offset)
        
        return {
            'sql': sql,
            'args': args
        }
        
class DeleteQuery:
    def __init__(self, table_name):
        self._table = table_name
        self._condition = None
        
    def where(self, *args):
        if(len(args) == 1):
            self._condition = args[0]
        else:
            self._condition = Condition(*args)
        return self
    
    def build_sql(self):
        args = []
        sql = "DELETE FROM " + self._table
        
        if self._condition != None:
            inner = self._condition.build_sql()
            sql += " WHERE " + inner['sql']
            args += inner['args']
        
        return {
            'sql': sql,
            'args': args
        }
        
class UpsertQuery:
    def __init__(self, table_name):
        self._table = table_name
        self._values = {}
        self._condition = None
    
    def values(self, values):
        self._values = self._values | values
        return self
    
    def where(self, *args):
        if(len(args) == 1):
            self._condition = args[0]
        else:
            self._condition = Condition(*args)
        return self
    
    def build_sql(self):
        args = []
        sql = ""
        
        if self._condition != None:
            sql = "UPDATE " + self._table + " SET "            
            sql += ', '.join(
                map(lambda key: key + " = %s", self._values.keys())
            )
            
            args += self._values.values()
            inner = self._condition.build_sql()
            sql += " WHERE " + inner['sql']
            args += inner['args']
        else:
            sql = "INSERT INTO " + self._table + " ("
            sql += ', '.join(self._values.keys())
            sql += ") VALUES ("
            sql += ', '.join(['%s'] * len(self._values))
            sql += ")"
            
            args += self._values.values()
        
        return {
            'sql': sql,
            'args': args
        }

class GroupCondition:
    def __init__(self, op):
        self._op = op
        self._conds = []
        
    def condition(self, *args):
        if(len(args) == 1):
            self._conds.append(args[0])
        else:
            self._conds.append(Condition(*args))
        return self
        
    def build_sql(self):
        str = ""
        args = []
        first = True
        
        for child in self._conds:
            tmp = child.build_sql()
            if not first:
                str += " " + self._op + " "
                
            str += tmp['sql']
            args += tmp['args']
            first = False

        return {
            'sql': "(" + str + ")",
            'args': args
        }

class RawCondition:
    def __init__(self, raw, args = []):
        self._raw = raw
        self._args = args
        
    def build_sql(self):
        return {
            'sql': "(" + self._raw + ")",
            'args': self._args
        }
        
class Condition:    
    def __init__(self, field, op, value):
        self._field = field
        self._op = op
        self._value = value
        
    def build_sql(self):
        
        if (self._op == "IN" or self._op == "NOT IN") and isinstance(self._value, list):
            placeholder = ', '.join(['%s'] * len(self._value))
            return {
                'sql': "(" + self._field + " " + self._op + " (" + placeholder +"))",
                'args': self._value
            } 
        
        
        return {
            'sql': "(" + self._field + " " + self._op + " %s)",
            'args': [self._value]
        }
        