var_1 = 'level'
var_2 = list(var_1)
var_2.reverse()
var_2 = str(var_2).replace('\', \'', '').replace('[\'', '').replace('\']', '')
print(var_2)
if var_1 == var_2:
    print('Palindrom')
else:
    print('Simple word')
# Вывод:
Palindrome
