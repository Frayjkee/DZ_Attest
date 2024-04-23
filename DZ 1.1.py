import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
df = pd.read_csv('kc-house-data.csv')

# Извлечение столбца 'price' (стоимость недвижимости)
prices = df['price']

# Создание графика
plt.figure(figsize=(10, 6))
plt.plot(prices, marker='o', linestyle='-', color='b')
plt.title('Цены недвижимости')
plt.xlabel('Индекс недвижимости')
plt.ylabel('Цена, $')
plt.grid(True)
plt.show()
