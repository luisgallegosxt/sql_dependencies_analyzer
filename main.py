import re
import sqlparse
import io

class Table:
    def __init__(self, name):
        self.name = name
        self.dependencies = []

    def add_dependencies(self, dependence):
        self.dependencies.append(dependence)

def get_table(name):
    if name not in tables:
        tables[name] = Table(name)
    return tables[name]
  
  
from typing import Pattern
def extract_sql_line(table_sentence):
  
  buf = io.StringIO(table_sentence)
  lines = buf.readlines()
  if lines[0].startswith("CREATE OR REPLACE TABLE"):
      pattern = r"CREATE OR REPLACE TABLE (\S+)"
      try:
        table_name = re.search(pattern, lines[0]).group(1)
        table = get_table(table_name)
        for line in lines:
          if "FROM" in line.upper():
            pattern = r"FROM (\S+)"
            try:
              dependence_table_name = re.search(pattern, line).group(1)
              if "." in dependence_table_name:
                dependence_table = get_table(dependence_table_name)
                table.add_dependencies(dependence_table)
            except Exception as e:
              pass
          elif "JOIN" in line.upper():
            pattern = r"JOIN (\S+)"
            try:
              dependence_table_name = re.search(pattern, line).group(1)
              if "." in dependence_table_name:
                dependence_table = get_table(dependence_table_name)
                table.add_dependencies(dependence_table)
            except Exception as e:
              pass
        return table
      except Exception as e:
          pass
        
  
  
tables = {}
with open('view1.sql', 'r') as f:
  content = f.read()
  statements = sqlparse.split(content)
  for table_sentence in statements:
    table_obj = extract_sql_line(table_sentence.upper())
    if table_obj:
      tables[table_obj.name] = table_obj
      
      
def dfs(table, visited=None):
    if visited is None:
        visited = set()

    print(table.name)
    visited.add(table)

    for dep in table.dependencies:
        if dep.name not in visited:
            dfs(dep, visited)
            
            
dfs(tables['schema.schema.dwt_business_table3'])            
