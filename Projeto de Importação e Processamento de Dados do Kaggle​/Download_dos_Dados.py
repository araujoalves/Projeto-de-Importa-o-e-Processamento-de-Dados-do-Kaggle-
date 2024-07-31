import os
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

# Definindo as credenciais da API do Kaggle através de variáveis de ambiente
os.environ['KAGGLE_USERNAME'] = 'daniaalves'
os.environ['KAGGLE_KEY'] = '400f487e997fa869b28dc1fae52a746e'

# Autenticação no Kaggle
api = KaggleApi()
api.authenticate()

# Download do dataset do Kaggle
dataset = 'shivamb/netflix-shows'  # O dataset do Kaggle para Netflix titles
api.dataset_download_files(dataset, path='netflix_data', unzip=True)

print("Download dos dados realizado com sucesso!")
