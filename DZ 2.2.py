import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
df = pd.read_csv('kc-house-data.csv')

# Создание гистограммы
plt.figure(figsize=(8, 6))
df['floors'].value_counts().sort_index().plot(kind='bar', color='purple', edgecolor='black')
plt.title('Распределение этажей домов')
plt.xlabel('Количество этажей')
plt.ylabel('Частота')
plt.grid(axis='y')
plt.xticks(rotation=0)
plt.show()

print('На основе графика мы можем сделать следующие выводы:\nБольшинство домов имеют один или два этажа.\nДома с тремя этажами менее распространены, чем одно- или двухэтажные дома.\nДома с четырьмя и более этажами встречаются гораздо реже.')