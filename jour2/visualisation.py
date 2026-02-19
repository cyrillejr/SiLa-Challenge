import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = sns.load_dataset('iris')
 
print("--- STATISTIQUES DESCRIPTIVES ---")
print(f"Moyenne :\n{df.mean(numeric_only=True)}\n")
print(f"Médiane :\n{df.median(numeric_only=True)}\n")
print(f"Écart-type :\n{df.std(numeric_only=True)}\n")
print(f"Quartiles :\n{df.quantile([0.25, 0.75], numeric_only=True)}")

plt.style.use('ggplot')
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Dashboard Iris - Jour 2', fontsize=20)

sns.histplot(df['sepal_length'], kde=True, ax=axes[0, 0], color="skyblue")
axes[0, 0].set_title('Distribution Sepal Length')

sns.regplot(x='sepal_width', y='sepal_length', data=df, ax=axes[0, 1])
axes[0, 1].set_title('Régression : Width vs Length')

corr = df.select_dtypes(include=[np.number]).corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=axes[1, 0])
axes[1, 0].set_title('Heatmap de Corrélation')

sns.boxplot(x='species', y='petal_length', data=df, ax=axes[1, 1])
axes[1, 1].set_title('Pétales par Espèce')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
