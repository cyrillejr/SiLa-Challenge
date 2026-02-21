import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

titanic_path = 'Titanic-Dataset.csv'
amazon_path = 'bestsellers with categories.csv'
weather_path = 'Project 1 - Weather Dataset.csv'

if all(os.path.exists(p) for p in [titanic_path, amazon_path, weather_path]):
    df_titanic = pd.read_csv(titanic_path)
    df_amazon = pd.read_csv(amazon_path)
    df_weather = pd.read_csv(weather_path)
else:
    exit()

df_titanic['Age'] = df_titanic['Age'].fillna(df_titanic['Age'].median())
df_titanic['Famille_Taille'] = df_titanic['SibSp'] + df_titanic['Parch'] + 1
df_titanic['Sex'] = df_titanic['Sex'].map({'male': 'Masculin', 'female': 'Féminin'})

df_titanic = df_titanic.rename(columns={
    'Survived': 'Survécu',
    'Pclass': 'Classe',
    'Name': 'Nom',
    'Sex': 'Sexe',
    'Age': 'Âge',
    'Fare': 'Prix_Billet'
})

amazon_stats = df_amazon.groupby('Genre')['Price'].agg(['mean', 'std']).reset_index()
amazon_stats.columns = ['Genre', 'Prix_Moyen', 'Prix_EcartType']

df_amazon = pd.merge(df_amazon, amazon_stats, on='Genre', how='left')

noms_unifies = pd.concat([df_titanic['Nom'], df_amazon['Name']], axis=0)

try:
    with pd.ExcelWriter('ETL_Final_Global.xlsx', engine='xlsxwriter') as writer:
        df_titanic.to_excel(writer, sheet_name='Titanic', index=False)
        df_amazon.to_excel(writer, sheet_name='Amazon', index=False)
        df_weather.head(100).to_excel(writer, sheet_name='Weather', index=False)
        
        workbook = writer.book
        header_format = workbook.add_format({
            'bold': True,
            'font_color': 'white',
            'bg_color': '#003366',
            'border': 1,
            'align': 'center'
        })

        for sheet_name in writer.sheets:
            worksheet = writer.sheets[sheet_name]
            worksheet.set_column(0, 15, 20)
            
    print("Pipeline ETL multi-source termine")
except Exception as e:
    print(e)
