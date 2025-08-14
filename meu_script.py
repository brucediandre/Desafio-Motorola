# -*- coding: utf-8 -*-

import sqlite3
import pandas as pd


#connectar ao banco
conn = sqlite3.connect("live.sqlite")
#listar as tabelas 
tabelas = pd.read_sql_query (
    "SELECT name FROM sqlite_master WHERE type='table';", con=conn
    )
print("Tabelas:", tabelas)
cursor = conn.cursor()

# Ler uma tabela específica
#df = pd.read_sql_query("SELECT * FROM processes2", conn)

conn.close()
