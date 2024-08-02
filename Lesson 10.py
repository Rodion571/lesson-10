expenses_by_categories = {}
expenses_by_users = {}
with open('hw10.txt', 'rt', encoding='utf-8') as file:
    content = file.read()
lines = content.splitlines()
for line in lines:
    tmp = line.split()
    if len(tmp) >= 4:
        _, *name, money, category = tmp
        name = ' '.join(name)
        money = float(money.replace('$', ''))
        expenses_by_categories[category] = expenses_by_categories.get(category, 0) + money
        expenses_by_users[name] = expenses_by_users.get(name, 0) + money
    else:
        print(f"Ошибка в строке: {line}")
for category, money in expenses_by_categories.items():
    print(f'{category}: {money:.2f}$')
for user, money in expenses_by_users.items():
    print(f'{user}: {money:.2f}$')
