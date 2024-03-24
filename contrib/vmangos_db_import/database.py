#!/usr/bin/python3

import mysql.connector

class DbInstance:
    _connection = None
    _cursor = None
    
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
        
    
    def get_rows(self, query, args = None):
        self._cursor.execute(query, args)
        return self._cursor.fetchall()
    
    def get_row(self, query, args = None):
        self._cursor.execute(query, args)
        return self._cursor.fetchone()
    
    def execute(self, query, args = None):
        self._cursor.execute(query, args)
        self._connection.commit()
        
    def execute_many(self, queries, args = None):
        for query in queries:
            self.execute(query, args)
        
    def insert(self, query, args = None):
        self._cursor.execute(query, args)
        self._connection.commit()
        return self._cursor.lastrowid
    
    def chunk(self, query, size, callback):
        has_more = True
        offset = 0
        
        while has_more:
            results = self.get_rows(query, (size, offset,))
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
        

