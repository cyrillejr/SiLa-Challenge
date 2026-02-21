import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
import xlsxwriter

file_path = 'Titanic-Dataset.csv'

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    exit()

df['Age'] = df['Age'].fillna(df['Age'].median())

Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 - Q1
limite_sup = Q3 + 1.5 * IQR

df['Famille_Taille'] = df['SibSp'] + df['Parch'] + 1

df['Sex'] = df['Sex'].map({'male': 'Masculin', 'female': 'Féminin'})

df = df.rename(columns={
    'Survived': 'Survécu',
    'Pclass': 'Classe',
    'Name': 'Nom',
    'Sex': 'Sexe',
    'Age': 'Âge',
    'Fare': 'Prix_Billet',
    'Embarked': 'Port_Embarquement'
})

df.to_csv('titanic_clean.csv', index=False)

plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Prix_Billet'])
plt.title('Détection des Outliers - Prix du Billet (Titanic)')
plt.savefig('outliers_fare.png')

try:
    with pd.ExcelWriter('titanic_final.xlsx', engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Analyse_Titanic', index=False)
        
        workbook  = writer.book
        worksheet = writer.sheets['Analyse_Titanic']

        header_format = workbook.add_format({
            'bold': True,
            'font_color': 'white',
            'bg_color': '#003366',
            'border': 1,
            'align': 'center'
        })

        for i, col in enumerate(df.columns):
            column_len = max(df[col].astype(str).str.len().max(), len(col)) + 3
            worksheet.set_column(i, i, column_len)
            worksheet.write(0, i, col, header_format)
except Exception as e:
    print(e)
