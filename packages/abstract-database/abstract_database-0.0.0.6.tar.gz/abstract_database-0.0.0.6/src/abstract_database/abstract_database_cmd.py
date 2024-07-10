import os
import pandas as pd
from sqlalchemy import create_engine, String, BigInteger, JSON, Text, cast, Index, MetaData, Table, text, inspect, Column, Integer, Float
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql import column
from abstract_utilities import *
def get_all_key_values(data, parent_key='', sep='_'):
    items = {}
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.update(get_all_key_values(value, new_key, sep=sep))
        else:
            items[new_key] = value
    return items

  
def get_file_parts(path):
    dirName = os.path.dirname(path)
    baseName = os.path.basename(path)
    fileName, ext = os.path.splitext(baseName)
    return {"dirName": dirName, "baseName": baseName, "fileName": fileName, "ext": ext}
def get_db_url(dbPath):
    dbUrl = f"sqlite:///{dbPath}"
    return dbUrl
def get_db_engine(dbUrl=None,dbPath=None):
  if dbUrl == None:
    if dbPath == None:
      return
    dbUrl=get_db_url(dbPath)
  return create_engine(dbUrl)
def enter_value_text(typ="",action="to filter by",parentObject="selection"):
  return input(f"Enter {typ} value {action} in {parentObject}: ")
def get_type_change_list():
  return ["String","Integer","Float","JSON"]
def capitalize(string):
  return f"{string[0].upper()}{string[1:].lower()}"
def pluralize(string):
  return f"{eatOuter(string,['s'])}s"
def get_integer_input(prompt, min_value, max_value):
    """Get an integer input from the user within a specified range."""
    while True:
        try:
            value = int(input(f"{prompt} ({min_value}-{max_value}): "))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def enumerate_selections(obj_list=[],parentObject="column",childObject=None):
    parent_plural = pluralize(capitalize(parentObject))
    output = f"Available {parent_plural}:" if childObject == None else f"{parent_plural} in {childObject}:" 
    for idx, value in enumerate(obj_list):
        print(f"{idx + 1}. {value}")
    return obj_list
def list_objects(obj_list=None,parentObject=None,object_type='column'):
    if not obj_list:
        print(f"No {pluralize(object_type)} available.")
        return None
    object_choice = get_integer_input(f"Choose a {object_type}", 1, len(obj_list)) - 1
    return obj_list[object_choice]
def get_field_choice(obj_list,parentObject=None,object_type=None):
    enumerate_selections(obj_list=obj_list,parentObject=parentObject)
    return list_objects(obj_list=obj_list,parentObject=None,object_type=object_type)
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

def get_db_name(dbName=None, dbPath=None, dbUrl=None):
    if dbName:
        return dbName
    fileParts_js = get_file_parts(dbPath or dbUrl)
    return fileParts_js.get("fileName")

class sessionManager(metaclass=SingletonMeta):
    def __init__(self, Base=None):
        self.dbTracker = {}
        self.Base = Base or declarative_base()

    def initialize_db(self, dbPath=None, dbUrl=None):
        dbUrl = dbUrl or get_db_url(dbPath)
        dbName = get_db_name(dbPath=dbPath, dbUrl=dbUrl)
        self.checkDatabaseName(dbName=dbName, dbPath=dbPath, dbUrl=dbUrl)
        self.create_session(dbPath=dbPath, dbUrl=dbUrl)
        self.create_tables(dbName)
        return dbName

    def get_dbName(self, dbName=None, dbPath=None, dbUrl=None):
        if dbName is None and dbUrl is None and dbPath is None:
            return dbName
        elif dbName is None and (dbUrl is not None or dbPath is not None):
            dbName = get_db_name(dbPath=dbPath, dbUrl=dbUrl)
        return dbName

    def create_session(self, dbPath=None, dbUrl=None):
        dbName = get_db_name(dbPath=dbPath, dbUrl=dbUrl)
        self.dbTracker[dbName]["engine"] = get_db_engine(dbUrl=dbUrl,dbPath=dbPath)
        self.Base.metadata.bind = self.dbTracker[dbName]["engine"]
        self.solcatcherDBSession = sessionmaker(bind=self.dbTracker[dbName]["engine"])
        self.dbTracker[dbName]["session"] = self.solcatcherDBSession()

    def create_tables(self, dbName):
        self.Base.metadata.create_all(self.dbTracker[dbName]["engine"])

    def checkDatabaseName(self, dbName=None, dbPath=None, dbUrl=None, dbBrowser=None):
        dbName = self.get_dbName(dbName=dbName, dbPath=dbPath, dbUrl=dbUrl)
        if dbName not in self.dbTracker:
            self.dbTracker[dbName] = {"dbUrl": dbUrl, "dbPath": dbPath}

    def close_session(self, dbName=None, dbPath=None, dbUrl=None):
        dbName = self.get_dbName(dbName=dbName, dbPath=dbPath, dbUrl=dbUrl)
        self.dbTracker[dbName]["session"].close()
class DatabaseBrowser:
    def __init__(self, dbPath=None, dbUrl=None):
        self.dbUrl = dbUrl or get_db_url(dbPath)
        self.engine = create_engine(self.dbUrl)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.metadata = MetaData()
        self.inspector = inspect(self.engine)
    def list_tables(self):
        tables = self.inspector.get_table_names()
        return enumerate_selections(obj_list=tables,parentObject="table",childObject=None)

    def table_list(self):
        obj_list = self.list_tables()
        return list_objects(obj_list=obj_list,object_type='table')
    def list_columns(self, table_name):
        try:
            table = Table(table_name, self.metadata, autoload_with=self.engine)
            columns = [column.name for column in table.columns]
            return enumerate_selections(obj_list=columns,parentObject="column",childObject=table)
        except Exception as e:
            print(f"Error loading table {table_name}: {e}")
            return []

    def column_list(self, table_name=None):
        if table_name is None:
            table_name = self.table_list()
        if table_name is None:
            print("No table selected.")
            return None
        obj_list = self.list_columns(table_name)  
        return list_objects(obj_list=obj_list,parentObject=table_name,object_type='column')
    def view_table(self, table_name, start=0, end=5):
        try:
            table = Table(table_name, self.metadata, autoload_with=self.engine)
            query = table.select().offset(start).limit(end - start)
            result = self.session.execute(query)
            rows = result.fetchall()

            if rows:
                df = pd.DataFrame(rows)
                df.columns = result.keys()
                pd.set_option('display.max_rows', None)
                pd.set_option('display.max_columns', None)
                pd.set_option('display.width', None)
                pd.set_option('display.max_colwidth', None)
                print(df)
                pd.reset_option('display.max_rows')
                pd.reset_option('display.max_columns')
                pd.reset_option('display.width')
                pd.reset_option('display.max_colwidth')
            else:
                print(f"No data found in table {table_name} from row {start} to {end}")
        except Exception as e:
            print(f"Error viewing table {table_name}: {e}")
    def alter_column_type(self, table_name, column_name, new_type):
        """Alter the type of a specific column in a table."""
        if new_type not in ['String', 'Integer', 'Float']:
            print("Invalid type. Please choose from 'String', 'Integer', or 'Float'.")
            return
        
        try:
            # Load the table
            table = Table(table_name, self.metadata, autoload_with=self.engine)
            old_column = table.c[column_name]
            
            # Determine the new column type
            if new_type == 'String':
                new_column = Column(column_name, String, nullable=old_column.nullable)
            elif new_type == 'Integer':
                new_column = Column(column_name, Integer, nullable=old_column.nullable)
            elif new_type == 'Float':
                new_column = Column(column_name, Float, nullable=old_column.nullable)
            
            # Perform the column type change
            with self.engine.connect() as connection:
                connection.execute(text(f"ALTER TABLE {table_name} RENAME COLUMN {column_name} TO {column_name}_old"))
                connection.execute(text(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {new_type}"))
                connection.execute(text(f"UPDATE {table_name} SET {column_name} = {column_name}_old"))
                connection.execute(text(f"ALTER TABLE {table_name} DROP COLUMN {column_name}_old"))
                connection.commit()
            
            print(f"Column {column_name} in table {table_name} successfully altered to {new_type}.")
        except Exception as e:
            print(f"Error altering column type: {e}")

    def update_all_entries(self, table_name, column_name, new_value):
        """Update all entries in a specific column with a new value."""
        try:
            table = Table(table_name, self.metadata, autoload_with=self.engine)
            query = table.update().values({column_name: new_value})
            result = self.session.execute(query)
            self.session.commit()
            print(f"All entries in column {column_name} of table {table_name} updated to {new_value}.")
        except Exception as e:
            print(f"Error updating entries: {e}")

    def export_data_by_key_value(self, table_name,value, file_path,key='zipcode' ):
        """Export data from a specific zipcode to an Excel file."""
        try:
            query = text(f"SELECT * FROM {table_name} WHERE {key} = :{key}")
            result = self.session.execute(query, {f"{key}": value})
            rows = result.fetchall()

            if rows:
                df = pd.DataFrame(rows)
                df.columns = result.keys()
                df.to_excel(file_path, index=False)
                print(f"Data for {key} {value} exported to {file_path}")
            else:
                print(f"No data found for {key} {value} in table {table_name}")
        except Exception as e:
            print(f"Error exporting data: {e}")
    def search_table(self, table_name, column_name, search_value):
        try:
            table = Table(table_name, self.metadata, autoload_with=self.engine)
        except Exception as e:
            print(f"Error loading table {table_name}: {e}")
            return
        
        if column_name not in [col.name for col in table.columns]:
            print(f"Column {column_name} does not exist in table {table_name}.")
            return

        try:
            query = text(f"SELECT * FROM {table_name} WHERE {column_name} LIKE :val")
            result = self.session.execute(query, {"val": f"%{search_value}%"})
            rows = result.fetchall()

            if rows:
                df = pd.DataFrame(rows)
                df.columns = result.keys()
                print(df)
            else:
                print(f"No results found for {search_value} in {column_name} of {table_name}")
        except Exception as e:
            print(f"Error executing search query: {e}")
    
    def search_by_json_field(self, table_name, json_field, key, value, file_path=None, case_sensitive=True, partial_match=False, save_to_excel=True):
        try:
            if not case_sensitive:
                value = value.lower()
                query = text(f"SELECT * FROM {table_name} WHERE LOWER(JSON_EXTRACT({json_field}, '$.{key}')) {'LIKE' if partial_match else '='} :val")
            else:
                query = text(f"SELECT * FROM {table_name} WHERE JSON_EXTRACT({json_field}, '$.{key}') {'LIKE' if partial_match else '='} :val")
            
            if partial_match:
                value = f"%{value}%"
            
            result = self.session.execute(query, {"val": value})
            rows = result.fetchall()
            
            if rows:
              input(rows)
                df = pd.DataFrame(rows)
                df.columns = result.keys()
                
                # Flatten the nested JSON fields
                for column in df.columns:
                    if isinstance(df[column].iloc[0], dict):
                        expanded_data = df[column].apply(lambda x: get_all_key_values(x))
                        expanded_df = pd.DataFrame(expanded_data.tolist())
                        expanded_df.columns = [f"{column}.{sub_col}" for sub_col in expanded_df.columns]
                        df = df.drop(columns=[column]).join(expanded_df)
                
                if save_to_excel and file_path:
                    df.to_excel(file_path, index=False)
                    print(f"Data for {key} {value} exported to {file_path}")
                
                return df
            else:
                print(f"No results found for {value} in {key} of {json_field} in {table_name}")
        except Exception as e:
            print(f"Error executing search query: {e}")



    def main(self):
        while True:
            print("\nMenu:")
            print("0. Exit")
            print("1. List tables")
            print("2. Search table")
            print("3. View table contents")
            print("4. List columns in a table")
            print("5. Alter column type")
            print("6. Update all entries in a column")
            print("7. Export data by key")
            
            choice = input("Enter your choice: ")

            if choice == "0":
                print("Exiting...")
                break
            elif choice == "1":
                self.list_tables()
            elif choice == "2":
                table_name = self.table_list()
                column_name = self.column_list(table_name)
                search_value = enter_value_text(typ="",action="to search for",parentObject=column_name)
                self.search_table(table_name, column_name, search_value)
            elif choice == "3":
                table_name = self.table_list()
                table_row_count = self.session.execute(text(f"SELECT COUNT(*) FROM {table_name}")).scalar()
                start = get_integer_input(f"Enter start row (0-{table_row_count - 1})", 0, table_row_count - 1)
                end = get_integer_input(f"Enter end row ({start + 1}-{table_row_count})", start + 1, table_row_count)
                self.view_table(table_name, start, end)
            elif choice == "4":
                self.list_columns()
            elif choice == "5":
                column_name = self.column_list()
                field_choice = get_field_choice(obj_list=get_type_change_list(),parentObject="new type",object_type='type')
                self.alter_column_type(table_name, column_name, field_choice)
            elif choice == "6":
                column_name = self.column_list()
                new_value = enter_value_text(typ="new",action="for all entries",parentObject=column_name)
                self.update_all_entries(table_name, column_name, new_value)
            elif choice == "7":
                table_name = self.table_list()
                obj_list = ["id","baseMint","quoteMint","tokenName","tokenSymbol"]
                field_choice = get_field_choice(obj_list=obj_list,parentObject="JSON search field",object_type='JSON field')
                value = enter_value_text(typ="the",action="to filter by",parentObject=field_choice)
                json_field = 'pool_keys' if field_choice in ['id', 'baseMint', 'quoteMint'] else 'meta_data'
                case_sensitive = input("Case sensitive? (y/n):(n) ").lower() or 'n' =='y'
                partial_match = input("Partial match? (y/n):(y) ").lower() or 'y' == 'y'
                save_to_excel = input("Save to excel? (y/n):(y) ").lower() or 'y' == 'y'
                if save_to_excel:
                  output_dir = os.path.join(os.getcwd(),'output_data')
                  os.makedirs(output_dir,exist_ok=True)
                  fileName = f"{table_name}_{field_choice}"
                  fileName = input(f"please enter a fileName: ({fileName}) ") or fileName
                  file_path = os.path.join(output_dir,f"{fileName}.xlsx")
                self.search_by_json_field(table_name=table_name, json_field=json_field, key=field_choice, value=value,file_path=file_path, case_sensitive=case_sensitive, partial_match=partial_match,save_to_excel=save_to_excel)
                
            else:
                print("Invalid choice. Please try again.")
def manageDb(dbPath):
    db_browser = DatabaseBrowser(dbPath=dbPath)
    db_browser.main()
