per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input())
deposit = [int(per_cent[key] * money / 100) for key in per_cent]
print("Максимальная сумма, которую вы можете заработать —", max(deposit))