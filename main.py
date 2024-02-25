per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print(per_cent)

money = int(input('введите сумму вклада:'))
deposit = []
deposit.append(per_cent['ТКБ']*money/100)
deposit.append(per_cent['СКБ']*money/100)
deposit.append(per_cent['ВТБ']*money/100)
deposit.append(per_cent['СБЕР']*money/100)
print('годовой процент:', deposit)
print("Максимальная сумма, которую вы можете заработать — ", max(deposit))


