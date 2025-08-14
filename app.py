from flask import Flask, jsonify, request
import sqlite3
import pandas as pd

app = Flask(__name__)

DATABASE = 'live.sqlite'

# Função para conectar ao banco
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Rota para listar todas as tabelas
@app.route('/tabelas', methods=['GET'])
def listar_tabelas():
    conn = get_db_connection()
    tabelas = pd.read_sql_query(
        "SELECT name FROM sqlite_master WHERE type='table';",
        con=conn
    )
    conn.close()
    return jsonify(tabelas['name'].tolist())

# Rota para listar dados de uma tabela específica
@app.route('/tabela/<nome>', methods=['GET'])
def listar_tabela(nome):
    conn = get_db_connection()
    try:
        df = pd.read_sql_query(f"SELECT * FROM {nome} LIMIT 10;", con=conn)
        result = df.to_dict(orient='records')
    except Exception as e:
        result = {'error': str(e)}
    conn.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
