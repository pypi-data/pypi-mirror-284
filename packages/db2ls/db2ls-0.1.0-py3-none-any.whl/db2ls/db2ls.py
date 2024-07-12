import sqlite3
import pandas as pd
import json
from datetime import datetime
# import logging
from typing import Optional, List, Union, Tuple

class db2ls:
    def __init__(self, db_path: str):
        self.db_path = db_path
        # # self.logger = logging.getLogger(__name__)
        self.connection: Optional[sqlite3.Connection] = None
    
    def __enter__(self) -> 'db2ls':
        """
        Establishes a context for the db2ls object, opening a connection to the database.
        This method is automatically called when entering a 'with' statement.
        """
        self.connection = sqlite3.connect(self.db_path)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        # Closes the database connection when exiting a 'with' statement.
        if self.connection:
            self.connection.close()
            print("Connection closed")

    @classmethod
    def connect(cls, db_path: str) -> 'db2ls':
        instance = cls(db_path)
        instance.connection = sqlite3.connect(db_path)
        return instance 
    
    def execute(self, query: str, params: Optional[Tuple] = None) -> None:
        # Execute a SQL query with optional parameters.
        try:
            with self.connection as conn:
                cursor = conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                conn.commit()
                self.log_change('EXECUTE', query, params)
                # print("Query executed successfully.")
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            pass

    def fetchall(self, query: str, params: Optional[Tuple] = None) -> Optional[List[Tuple]]:
        # Execute a SQL query and return all results.
        try:
            with self.connection as conn:
                cursor = conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                rows = cursor.fetchall()
                return rows
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            return None

    def fetchmany(self, query: str, params: Optional[Tuple] = None,n:int=5) -> Optional[List[Tuple]]:
        # Execute a SQL query and return all results.
        try:
            with self.connection as conn:
                cursor = conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                rows = cursor.fetchmany(n)
                return rows
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            return None

    def create(self, table: str,columns:Union[str, List[str]],exist_ok:bool=True) -> None:
        # Create a table in the database. 
        if isinstance(columns, list):
            columns_=', '.join(columns)
        else:
            columns_=columns
        if exist_ok:
            query = f"CREATE TABLE IF NOT EXISTS {table} ({columns_})"
        else:
            query = f"CREATE TABLE {table} ({columns_})"
        self.execute(query)
        print(f"Table created with definition: {query}")
    
    def insert(self, table: str, columns: List[str], data: List[Union[str, int, float]]) -> None:
        # Insert data into a table.
        placeholders = ', '.join(['?' for _ in data])
        query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})"
        self.execute(query, data)
        print(f"Data inserted into {table}: {data}")

    def select(self, table: str, columns: Union[str, List[str]] = '*', where: Optional[str] = None, where_params: Optional[Tuple] = None, verbose: bool=False) -> Optional[List[Tuple]]:
        # Select data from a table.        
        if isinstance(columns, list):
            columns_=', '.join(columns)
        else:
            columns_=columns
        query = f"SELECT {columns_} FROM {table}"
        if where:
            query += f" WHERE {where}"
        rows = self.fetchall(query, where_params)
        if verbose:
            for row in rows:
                print(row)
        return rows
    
    def print(self, table: str, columns: Union[str, List[str]] = ['*'], where: Optional[str] = None, where_params: Optional[Tuple] = None, n:int=5) -> Optional[List[Tuple]]:
        rows = self.select(table=table,columns=columns,where=where,where_params=where_params)
        if rows:
            if len(rows) <= n:
                rows_=rows
            else:
                rows_=rows[:n]
            for row in rows_:
                print(row)
    def update(self, table: str, set_clause: Union[str, List[str]], where: Union[str, List[str]], where_params: Tuple=None) -> None:
            """
            Update data in a table.
            Usage:
                option1: 
                    with db2ls(db_path) as db:
                        db.update(table, "postcode = '72076'", "postcode = '69181'")
                option2: 
                db2ls.connect(db_path).execute("update germany set city='Tübingen' where city = 'Leimen'")
            """
            if isinstance(set_clause, list):
                set_clause = ', '.join([f"{col} = ?" for col in set_clause])
            
            if isinstance(where, list):
                where_clause = ' AND '.join(where)
            else:
                where_clause = where
            
            query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
            print(query)
            if where_params is None:
                self.execute(query)
                # print(f"Data updated in {table} where {where_clause}")
            else:
                self.execute(query, where_params)
                # print(f"Data updated in {table} where {where_clause}: {where_params}")

    def drop(self, table:str):
        self.execute("DROP TABLE {table}")
        print(f"Warning: {table} got removed from DataBase")
    def remove(self, table:str):
        self.drop(self, table)
        
    def delete(self, table: str, where: str, where_params: Tuple) -> None:
        # Delete data from a table. 
        query = f"DELETE FROM {table} WHERE {where}"
        self.execute(query, where_params)
        print(f"Data deleted from {table} where {where}")

    def begin(self) -> None:
        """
        Begin a transaction.
        """
        try:
            self.connection.execute('BEGIN')
            print("Transaction started")
        except sqlite3.Error as e:
            print(f"Error starting transaction: {e}")
            pass

    def commit(self) -> None:
        """
        Commit the current transaction.
        """
        try:
            self.connection.commit()
            print("Transaction committed")
        except sqlite3.Error as e:
            print(f"Error committing transaction: {e}")
            pass

    def rollback(self) -> None:
        """
        Rolls back the current transaction to undo changes.
        """
        try:
            self.connection.rollback()
            print("Transaction rolled back")
        except sqlite3.Error as e:
            pass
            print(f"Error rolling back transaction: {e}")
    def undo(self) -> None:
        """
        Rolls back the current transaction to undo changes.
        """
        try:
            self.connection.rollback()
            print("Transaction rolled back")
        except sqlite3.Error as e:
            pass
            print(f"Error rolling back transaction: {e}")

    def columns(self, table: str) -> List[str]:
        """
        Retrieve column names of a table.
        usage: db.connect(db_path).columns('germany')
        """
        query = f"PRAGMA table_info({table})"
        rows = self.fetchall(query)
        if rows:
            return [row[1] for row in rows]
        else:
            return []

    def vacuum(self) -> None:
        """
        Run the VACUUM command to rebuild the database file.
        - Executes the VACUUM command to optimize the database file.
        """
        self.execute("VACUUM")
        print("Database vacuumed")

    def to_df(self, table: str, query: Optional[str] = None) -> pd.DataFrame:
        if query is None:
            query = f"SELECT * FROM {table}"
        try:
            return pd.read_sql_query(query, self.connection)
        except pd.DatabaseError as e:
            print(f"Error converting query result to DataFrame: {e}")
            return pd.DataFrame()

    # +++++++++ to add redo() function +++++++++ 
    def log_change(self, operation: str, query: str, params: Optional[Tuple] = None):
            """
            Log the database operation to the change_log table.
            
            Args:
            - operation (str): The type of operation (e.g., 'INSERT', 'UPDATE', 'DELETE').
            - query (str): The SQL query executed.
            - params (tuple, optional): Parameters used in the query.
            """
            log_query = "INSERT INTO change_log (operation, query, params) VALUES (?, ?, ?)"
            params_str = json.dumps(params) if params else None
            self.execute(log_query, (operation, query, params_str))

    def redo(self):
        """
        Reapply the changes from the change_log.
        """
        logs = self.fetchall("SELECT operation, query, params FROM change_log ORDER BY timestamp")
        for log in logs:
            operation, query, params_str = log
            params = json.loads(params_str) if params_str else None
            self.execute(query, params)
    # +++++++++ to add redo() function +++++++++ 

# Example usage:
if __name__ == "__main__":
    # Example usage
    db_path = 'example.db'
    with db2ls(db_path) as db:
        db.create("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        db.insert("users", ["name", "age"], ["Alice", 30])
        db.insert("users", ["name", "age"], ["Bob", 25])
        
        rows = db.select("users", columns="id, name", where="age > ?", where_params=[26])
        if rows:
            for row in rows:
                print(row)
        db.print("users",columns="*")
        db.update("users", {"age": 31}, "name = ?", ["Alice"])
        
        db.delete("users", "name = ?", ["Bob"])
