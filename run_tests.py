import os
import subprocess
import questionary

def run_pytest(args: list):
    """Функция для запуска pytest c заданными аргументами"""
    command = ["pytest"] + args
    try:
        subprocess.run(command,check=True)
    except subprocess.CalledProcessError: print("Во время выполнения теста произошла ошибка")
    except FileNotFoundError: print("команда pytest не найдена.")

def main_menu():
    """Главное меню Cll"""
    while True:
        choice = questionary.select("Добро пожаловать в Cll для запуска тестов.",
                                    choices=["Запустить все тесты",
                                             "Запустить smoke тесты",
                                             "Запустить regression тесты",
                                             "Выход"
                                             ])




        if choice== "Запустить все тесты":
            run_pytest(["-v"])
        elif choice =="Запустить smoke тесты":
            run_pytest(["-v","-m","smoke"])
        elif choice == "Запустить regression тесты":
            run_pytest(["-v","-m","regression"])
            break