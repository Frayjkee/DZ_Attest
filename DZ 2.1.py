import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
df = pd.read_csv('kc-house-data.csv')

# Создание барплота
plt.figure(figsize=(8, 6))
df['waterfront'].value_counts().plot(kind='bar', color=['blue', 'green'])
plt.title('Распределение домов по наличию вида на набережную')
plt.xlabel('Вид на набережную')
plt.ylabel('Количество домов')
plt.xticks(ticks=[0, 1], labels=['Нет', 'Да'], rotation=0)
plt.grid(axis='y')
plt.show()

print('На основе графика мы можем сделать следующие выводы: \nБольшинство домов в наборе данных не имеют вид на набережную.\nКоличество домов с видом на набережную значительно меньше, чем количество домов без такого вида.\nНаличие вида на набережную не является распространенным условием для домов в этом наборе данных.')

