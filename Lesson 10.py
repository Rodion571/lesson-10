expenses_by_categories = {}
expenses_by_users = {}
with open('hw10.txt', 'rt', encoding='utf-8') as file:
    for line in file:
        tmp = line.split()
        if len(tmp) >= 4:
            _, *name, money, category = tmp
            name = ' '.join(name)
            money = float(money.replace('$', ''))
            if category in expenses_by_categories:
                expenses_by_categories[category] += money
            else:
                expenses_by_categories[category] = money
            if name in expenses_by_users:
                expenses_by_users[name] += money
            else:
                expenses_by_users[name] = money
        else:
            print(f"Ошибка в строке: {line}")
print("Расходы по категориям:")
for category, money in expenses_by_categories.items():
    print(f'{category}: {money:.2f}$')
print("\nРасходы по пользователям:")
for user, money in expenses_by_users.items():
    print(f'{user}: {money:.2f}$')
