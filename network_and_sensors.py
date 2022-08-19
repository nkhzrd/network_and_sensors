from lib2to3.pytree import Base
import psutil
import os
import time
import sys
from colorama import init, Fore
from colorama import Back
from colorama import Style
init(autoreset=True)

def cpu_system():
    try:
        os.system('cls')
        print('')
        count_of_yader = psutil.cpu_count(logical=False) # Количество ядер (без логических)
        cpu_stats = list(psutil.cpu_stats())
        cpu_freq = list(psutil.cpu_freq())
        cpu_nagruzka = psutil.cpu_percent()
        file_creation = open("./REPORTS_INFO/cpu_info.txt", 'w')
        with open("./REPORTS_INFO/cpu_info.txt", 'a') as file_save:
            print(f'Количество ядер: {count_of_yader}', file = file_save)
            print(f'''Количество переключений контекста с момента загрузки: {cpu_stats[0]}
Количество прерываний с момента загрузки: {cpu_stats[1]}
Количество системных вызовов с момента загрузки: {cpu_stats[3]}''', file = file_save)
            print(f'''Текущая частота процессора (ГГц): {cpu_freq[0]}
Минимальная частота процессора: {cpu_freq[1]}
Максимальная частота процессора: {cpu_freq[2]}''', file = file_save)
            print(f'Нагрузка ЦП: {cpu_nagruzka} %', file = file_save)

        print(f'Количество ядер: {count_of_yader}')
        print(f'''Количество переключений контекста с момента загрузки: {cpu_stats[0]}
Количество прерываний с момента загрузки: {cpu_stats[1]}
Количество системных вызовов с момента загрузки: {cpu_stats[3]}''')
        print(f'''Текущая частота процессора (ГГц): {cpu_freq[0]}
Минимальная частота процессора: {cpu_freq[1]}
Максимальная частота процессора: {cpu_freq[2]}''')
        print(f'Нагрузка ЦП: {cpu_nagruzka} %')
        print('')
        start_menu()
    except BaseException as err_msg:
        os.system('cls')
        print('<-- Произошла ошибка! --> ' + err_msg)

def network_stats():
    try:
        os.system('cls')
        file_creation = open("./REPORTS_INFO/network_info.txt", 'w')
        all_interfaces = dict(psutil.net_io_counters(pernic=True))
        with open("./REPORTS_INFO/network_info.txt", 'a') as file_save:
            print('< ------ Общесистемная статистика сетевого ввода-вывода: ----- >', file = file_save)
            print('< ------ Общесистемная статистика сетевого ввода-вывода: ----- >')
            for k, v in all_interfaces.items():
                dump_net = list(v)

                print(f'''{k}:
Отправлено байт: {dump_net[0]}\nПолучено байт: {dump_net[1]}\nКоличество отправленных пакетов: {dump_net[2]}\nКоличество принятых пакетов: {dump_net[3]}\n''', file=file_save)
                print(f'''{k}:
Отправлено байт: {dump_net[0]}\nПолучено байт: {dump_net[1]}\nКоличество отправленных пакетов: {dump_net[2]}\nКоличество принятых пакетов: {dump_net[3]}\n''')

            net_if_stats = dict(psutil.net_if_stats())
            print('\n< ----- Информация о сетевых картах, установленных в системе (вкл. виртуальные): ----- >\n', file = file_save)
            print('\n< ----- Информация о сетевых картах, установленных в системе (вкл. виртуальные): ----- >\n')
            for k, v in net_if_stats.items():
                dump_net = list(v)
                res_string = f'''Название интерфейса - {k}:
Запущена ли сетевая карта: {dump_net[0]}\nТип дуплексной связи: {dump_net[1]}\nСкорость сетевой карты в МегаБитах: {dump_net[2]}\nMTU: {dump_net[3]}\n'''.replace("True", 'Да').replace("False", "Нет")
                print(res_string, file = file_save)
                print(res_string)
    except BaseException as err_msg:
        print(f"{err_msg}\n")
        sys.exit()




def start_menu():
    if os.path.exists("./REPORTS_INFO"):
        pass
    else:
        os.makedirs('./REPORTS_INFO')
    print(Fore.BLUE + 'Доступные функции:\n1) Получить информацию о процессоре\n2) Получить информацию о сетевой статистике\n3) Очистить терминал\n4) Выйти из программы')
    a = input("Введите номер необходимой функции: ")
    if a == '1':
        cpu_system()
    elif a == '2':
        network_stats()
    elif a == '3':
        try:
            os.system('cls')
        except BaseException:
            pass
    elif a == '4':
        sys.exit()
    else:
        print('Такой функции не существует!')


if __name__ == "__main__":
    print(Fore.GREEN + '< ----- Программа для сбора данных о компьютере и показателей датчиков ----- >')
    while True:
        start_menu()


