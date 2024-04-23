import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
df = pd.read_csv('kc-house-data.csv')

# 4. График зависимости цены от уровня состояния
plt.figure(figsize=(8, 6))
plt.boxplot([df[df['condition'] == i]['price'] for i in df['condition'].unique()])
plt.title('Зависимость цены от уровня состояния')
plt.xlabel('Уровень состояния')
plt.ylabel('Цена, $')
plt.grid(True)
plt.show()

print(' На этом графике видно, что недвижимость в лучшем состоянии (оценка 5) имеет более высокие цены по сравнению с недвижимостью в менее хорошем состоянии.')