import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
df = pd.read_csv('kc-house-data.csv')

# Извлечение столбца 'yr_built' (год постройки)
yr_built = df['yr_built']

# Создание гистограммы
plt.figure(figsize=(10, 6))
plt.hist(yr_built, bins=30, color='orange', edgecolor='black')
plt.title('Распределение года постройки недвижимости')
plt.xlabel('Год постройки')
plt.ylabel('Частота')
plt.grid(True)
plt.show()
