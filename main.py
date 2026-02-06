try:
    from colorama import init, Fore, Style
    from plyer import notification
except ModuleNotFoundError as error_mod:
    import ctypes
    ctypes.windll.user32.MessageBoxW(0, f"Модуль {error_mod.name} не найден, пожалуйста, установите его.\nModule {error_mod.name} not found, please install it.", "debug-console", 0x10)
    exit()

init(autoreset=True)
class App:
    def __init__(self, main):
        self.main = main

    def create_plyer(self):
        print(Fore.LIGHTBLUE_EX + "title message app_name timeout(int)")
        while True:
            notif = input("> ")
            parts = notif.split(maxsplit=3)

            if not parts:
                print(f"{Fore.YELLOW}введите что-то\n")
                continue

            if len(parts) > 4:
                print("неправильный тип данных, попробуйте снова\n")
                return

            if notif == "exit":
                self.main.clear()
                break
            try:
                try:
                    timeout_notify = int(parts[3])
                except Exception:
                    print(f"{Fore.RED}Введите целое число")
                    return
                notification.notify(title=parts[0], message=parts[1], app_name=parts[2], timeout=timeout_notify)
            except Exception as e:
                print(f"{Fore.RED}Не удалось создать уведомление.\n{e}")

class Main:
    def __init__(self):
        self.app = App(self)
        self.commands = {
            "clear": self.clear,
            "1": self.app.create_plyer,
            "2": self.help,
            "3": exit,
            "exit": exit
        }

    def run(self):
        self.clear()
        while True:
            cmd = input(f"{Fore.BLUE}choice number: {Style.RESET_ALL}").strip()
            action = self.commands.get(cmd)

            if action:
                try:
                    action()
                except Exception as e:
                    print(f"{Fore.RED}[ERROR] {e}")
            else:
                print(f"{Fore.RED}Неизвестная команда")

    def clear(self):
        import os
        os.system('cls')
        self.logo()
        self.logo_text()

    def help(self):
        print(f"""{Fore.BLUE}
title - название окна уведомления\nmessage - текст в уведомлении\napp_name - названия приложения\ntimeout - сколько будет держаться уведомление (в секундах)\n
Пример: {Fore.LIGHTBLUE_EX}title message app_name timeout{Fore.BLUE}\n
Доп.Команды: {Fore.LIGHTBLUE_EX}exit, clear
{Fore.LIGHTCYAN_EX}Подробней на GitHub: https://github.com/hiikikomorii/plyer-notifications""")
        input("Для продолжения нажмите enter: ")
        self.clear()

    @staticmethod
    def logo():
        ascii_art = """
        ███╗   ██╗ ██████╗ ████████╗██╗███████╗██╗ ██████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗███████╗
        ████╗  ██║██╔═══██╗╚══██╔══╝██║██╔════╝██║██╔════╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
        ██╔██╗ ██║██║   ██║   ██║   ██║█████╗  ██║██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║███████╗
        ██║╚██╗██║██║   ██║   ██║   ██║██╔══╝  ██║██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║╚════██║
        ██║ ╚████║╚██████╔╝   ██║   ██║██║     ██║╚██████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║███████║
        ╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚═╝╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
        """

        def print_cyan_to_darkblue(asciii_art):
            lines = asciii_art.split("\n")
            total_lines = len(lines)

            for i, line in enumerate(lines):
                g = int(255 - (i / max(total_lines - 1, 1)) * 255)
                b = int(255 - (i / max(total_lines - 1, 1)) * (255 - 139))
                print(f"\033[38;2;0;{g};{b}m{line}\033[0m")

        print_cyan_to_darkblue(ascii_art)

    @staticmethod
    def logo_text():
        print(f"""
{Fore.CYAN}1{Fore.RESET} - {Fore.LIGHTCYAN_EX}Start   
{Fore.CYAN}2{Fore.RESET} - {Fore.LIGHTCYAN_EX}Help
{Fore.CYAN}3{Fore.RESET} - {Fore.LIGHTRED_EX}Exit{Fore.RESET}

                """)


if __name__ == '__main__':
    Main().run()
