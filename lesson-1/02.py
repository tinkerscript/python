total = int(input('Введите количество секунд: '))
hours = total // 3600
minutes = total % 3600 // 60
seconds = total % 3600 % 60
print(f'{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}')
