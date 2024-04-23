import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
df = pd.read_csv('kc-house-data.csv')

# 3. График зависимости цены от количества ванных комнат
plt.figure(figsize=(8, 6))
plt.boxplot([df[df['bathrooms'] == i]['price'] for i in df['bathrooms'].unique()])
plt.title('Зависимость цены от количества ванных комнат')
plt.xlabel('Количество ванных комнат')
plt.ylabel('Цена, $')
plt.grid(True)
plt.show()

print('По этому графику можно заметить, что недвижимость с большим количеством ванных комнат обычно стоит дороже. Опять же, есть некоторые выбросы, но в целом, чем больше ванных комнат, тем выше цена.')