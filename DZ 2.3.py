import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
df = pd.read_csv('kc-house-data.csv')

# Создание гистограммы
plt.figure(figsize=(8, 6))
df['condition'].value_counts().sort_index().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Распределение состояния домов')
plt.xlabel('Уровень состояния')
plt.ylabel('Частота')
plt.grid(axis='y')
plt.xticks(rotation=0)
plt.show()

print('На основе графика мы можем сделать следующие выводы:\nБольшинство домов имеют средний или хороший уровень состояния.\nДома с низким уровнем состояния встречаются гораздо реже.\nДома с отличным уровнем состояния также представлены, но их количество значительно меньше, чем домов со средним и хорошим состоянием.')