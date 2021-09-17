'''
这是使用三个单引号的多行注释
打印高为10,宽为10的平行四边形
'''

h = 0
while h < 10:
    i = 0
    while i < h:
        print(' ', end='')
        i += 1

    i = 0
    while i < 10:
        print('*', end='')
        i += 1

    print('\n')
    h += 1
h = 0
