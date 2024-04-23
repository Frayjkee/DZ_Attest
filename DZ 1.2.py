import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
df = pd.read_csv('kc-house-data.csv')

# Извлечение столбца 'sqft_living' (жилая площадь недвижимости)
sqft_living = df['sqft_living']

# Создание графика
plt.figure(figsize=(10, 6))
plt.plot(sqft_living, marker='o', linestyle='-', color='g')
plt.title('Жилая площадь недвижимости')
plt.xlabel('Индекс недвижимости')
plt.ylabel('Жилая площадь, кв. футов')
plt.grid(True)
plt.show()
