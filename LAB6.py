#1
a = ['admin', 'operator']
a.append(input('Введите имя нового пользователя: '))
print(a)

#2
a = ['root', 'security']
a.insert(0, input('Введите имя администратора: '))
print(a)

#3
a = ['bob', 'charlie', 'alice']
a.remove(input('Введите имя пользователя для удаления: '))
print(a)

#4
a = ['Access granted', 'Login failed', 'Connection lost']
b = a.pop()
print(b)
print(a)

#5
a = ['ok', 'error', 'ok', 'error', 'error']
b = a.count('error')
print('Количество ошибок входа:', b)

#6
a = ['Access ok', 'Breach detected', 'System reboot', 'Breach detected']
b = a.index('Breach detected')
print('Первое обнаружение вторжения на позиции: ', b)

#7
a = [3, 1, 2, 3, 1, 2]
a.sort()
print(a)

#8
a = ['2025-10-01', '2025-10-02', '2025-10-03']
a.reverse()
print(a)

#9
a = ["alert", "spam", "login", "error", "spam", "alert"]
for i in range(a.count('spam')):
    a.remove('spam')
a.append("END_LOG")
a.reverse()
b=a.count('alert')
print('Журнал после очистки: ', a)
print('Количество "alert": ', b)

#10
whitelist = ['192.168.0.1', '192.168.0.2', '192.168.0.3', '192.168.0.4', '192.168.0.5']
whitelist.remove(input('Введите IP для удаления: '))
new = input('Введите новый IP: ')
whitelist.insert(3,new)
whitelist.sort()
print('Обновлённый белый список: ', whitelist)
print('Индекс нового IP: ', whitelist.index(new))

#11
a = ['ok', 'fail', 'fail', 'ok', 'fail']
b = a.count('fail')
for i in range(b):
    a.remove('fail')
a.append("audit_completed")
a.reverse()
c = a.index('ok')
print('Количество неудачных входов: ', b)
print('Итоговый список: ', a)
print("Первый индекс 'ok': ", c)

