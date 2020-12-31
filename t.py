import time

start = time.time()

for i in range(51):
    if i % 5 == 0:
        print(f'{i} -')
    elif i % 7 == 0:
        print(f'{i} +')
    else:
        print(f'{i}')


exe = (time.time() - start)
print(f'\nExecution time in seconds: {exe}\n')
