import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
df = pd.read_csv('kc-house-data.csv')

#График зависимости цены от количества спален

plt.figure(figsize=(8, 6))
plt.boxplot([df[df['bedrooms'] == i]['price'] for i in range(1, 11)], labels=range(1, 11))
plt.title('Зависимость цены от количества спален')
plt.xlabel('Количество спален')
plt.ylabel('Цена, $')
plt.grid(True)
plt.show()

print('На этом графике видно, что недвижимость с большим количеством спален обычно дороже. Однако есть выбросы (особенно в случае домов с 9 и более спальнями), которые могут быть связаны с особыми типами недвижимости или роскошными объектами.')