from sqlalchemy import create_engine
import pandas as pd

# Leitura do arquivo CSV baixado
data = pd.read_csv('netflix_data/netflix_titles.csv')  # Certifique-se de que o caminho esteja correto

# Configuração da conexão com o banco de dados
DB_HOST = 'localhost'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWORD = '258201'
DB_NAME = 'netflix_titles'

# String de conexão
connection_string = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(connection_string)

# Carregamento dos dados no banco
data.to_sql('netflix_titles', engine, if_exists='replace', index=False)

print("Dados inseridos com sucesso no banco de dados!")
