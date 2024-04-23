import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('kc-house-data.csv')

#График зависимости цены от площади жилого пространства:

plt.figure(figsize=(10, 6))
plt.scatter(df['sqft_living'], df['price'], color='blue', alpha=0.5)
plt.title('Зависимость цены от площади жилого пространства')
plt.xlabel('Жилая площадь, кв. футов')
plt.ylabel('Цена, $')
plt.grid(True)
plt.show()


print('На графике видно, что с увеличением площади жилого пространства цена недвижимости также увеличивается. Это ожидаемо, так как большая площадь обычно означает более дорогостоящее жилье.')