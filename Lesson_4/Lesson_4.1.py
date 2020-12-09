from sys import argv

name, prod_time, bid_hours, prize = argv
prod_time = float(prod_time)
bid_hours = float(bid_hours)
prize = float(prize)
salary = ((prod_time*bid_hours)+prize)

print("Имя скрипта: ", name)
print("Выработка в часах: ", prod_time)
print("Ставка в часах: ", bid_hours)
print("Премия: ", prize)
print("Расчёт ЗП: ",salary)

