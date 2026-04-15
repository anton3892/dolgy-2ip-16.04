import pandas as pd

class bank():
    def __init__(self, summa, procent, periods):
        self.summa = summa
        self.procent = procent
        self.periods = periods

def payments(person):
    months = person.periods * 12 
    stavka = person.procent / 100 / 12
    payment = person.summa * stavka / (1 - 1 / (1 + stavka)**months)
    return payment

pervyi = bank(20000, 15, 1)
vtoryi = bank(200000, 18, 1)
tretyi = bank(2000000, 29, 1)

p1 = payments(pervyi)
p2 = payments(vtoryi)
p3 = payments(tretyi)

print(f'Человек с кредитом на телефон платит в месяц {p1:.1f}')
print(f'Человек с кредитом на машину платит в месяц {p2:.1f}')
print(f'Человек с кредитом на квартиру платит в месяц {p3:.1f}')

start_balance = 20000
balance = start_balance
data = []
total_monthly = p1 + p2 + p3

for i in range(1, 13):
    balance += total_monthly
    data.append([i, balance])
# записываем результат каждого месяца в список

df = pd.DataFrame(data, columns=['Месяц', 'Баланс банка'])
df.set_index('Месяц', inplace=True) # set_index делает колонку Месяц


print(f"{'Отчет':^32}")
pd.set_option('display.float_format', '{:.2f}'.format)
print(df.to_string(formatters={'Баланс банка': '{:>15.2f}'.format}, justify='right'))
# formatters (Специальный инструмент для красоты)

print(f"Итоговая прибыль за год: {balance - start_balance:.2f}")


# .2f: Оставляет ровно 2 знака после точки
# set_option вид таблицы