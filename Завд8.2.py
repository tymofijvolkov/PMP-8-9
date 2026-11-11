import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (15, 5)

try:
    df = pd.read_csv("comptagevelo2017.csv", parse_dates=["Date"], dayfirst=True)
    print("Файл успішно завантажено")
except FileNotFoundError:
    print("Помилка: файл не знайдено")
    exit()

print("\nПерші 5 рядків DataFrame:")
print(df.head())

print("\nІнформація про DataFrame:")
print(df.info())

print("\nОписова статистика:")
print(df.describe())

bike_cols = df.select_dtypes(include="number").columns.tolist()

total_by_track = df[bike_cols].sum().sort_values(ascending=False)
total_all = total_by_track.sum()

print(f"\nЗагальна кількість велосипедистів за 2017 рік для всіх велодоріжок: {int(total_all)}")
print("\nКількість велосипедистів у розрізі велодоріжок (топ-10):")
print(total_by_track.head(10))

df["Month"] = df["Date"].dt.month
monthly_pivot = df.groupby("Month")[bike_cols].sum()

selected_tracks = total_by_track.index[:3].tolist()
print("\nНайбільш популярний місяць за кількістю велосипедистів для трьох обраних велодоріжок:")
for track in selected_tracks:
    best_month = monthly_pivot[track].idxmax()
    max_val = monthly_pivot[track].max()
    print(f"Велодоріжка '{track}': місяць №{int(best_month)} (кількість: {int(max_val)})")

chosen_track = selected_tracks[0]
monthly_dynamics = monthly_pivot[chosen_track]

print(f"\nДинаміка використання велодоріжки '{chosen_track}' за місяцями (2017 рік):")
print(monthly_dynamics)

monthly_dynamics.plot(
    kind="line",
    marker="o",
    linewidth=2,
    title=f"Зміна кількості велосипедистів на велодоріжці {chosen_track} за 2017 рік (за місяцями)"
)
plt.xlabel("Місяць")
plt.ylabel("Кількість велосипедистів")
plt.xticks(range(1, 13))
plt.grid(True)
plt.tight_layout()
plt.show()
