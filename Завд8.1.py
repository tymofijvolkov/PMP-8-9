import pandas as pd

try:
    df = pd.read_csv("exports.csv")
    print("Файл успішно завантажено")
except FileNotFoundError:
    print("Помилка: файл не знайдено")
    exit()

print("\nПочаткові дані:")
print(df)

print("\nПерші 3 рядки DataFrame:")
print(df.head(3))

print("\nТипи даних:")
print(df.dtypes)

print("\nРозмір DataFrame:")
print(df.shape)

print("\nОписова статистика:")
print(df.describe())

df["Exports_ratio"] = df["Exports of goods and services (% of GDP)"] / 100
print("\nDataFrame з новим показником:")
print(df)

filtered_df = df[df["Exports of goods and services (% of GDP)"] > 50]
print("\nРезультат фільтрації:")
print(filtered_df)

sorted_df = df.sort_values(
    by="Exports of goods and services (% of GDP)",
    ascending=False
)
print("\nРезультат сортування:")
print(sorted_df)

grouped_df = df.groupby("Year")["Exports of goods and services (% of GDP)"].agg(
    ["mean", "min", "max"]
).reset_index()
print("\nРезультат групування:")
print(grouped_df)

print("\nКількість унікальних країн/регіонів:")
print(df["Country"].nunique())

sorted_df.to_csv("exports_result.csv", index=False)
print("\nРезультати збережено у файл 'exports_result.csv'")
