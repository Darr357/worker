import pandas as pd
import os

desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
file_path = os.path.join(desktop_path, 'Рецедивы_в1.xlsx')

df = pd.read_excel(file_path, nrows=54)

print(" Файл успешно прочитан!")
print(f" Путь к файлу: {file_path}")
print(f" Загружено строк: {len(df)}")
print(f" Столбцов: {len(df.columns)}")
print("\n Данные:")
print(df)