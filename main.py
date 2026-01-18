import tkinter as tk
from tkinter import messagebox, Menu
import os

class CrossroadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Программа Перекресток")
        self.root.geometry("800x750")
        self.root.resizable(False, False)

        try:
            if os.path.exists("icon.ico"):
                self.root.iconbitmap("icon.ico")
        except Exception:
            pass

        self.content = [
            ("ped.png", "Светофор для пешеходов: Если горит красный человечек - мы стоим. Если зеленый - можно переходить дорогу!"),
            ("auto.png", "Светофор для машин: Красный свет говорит водителям \"Стой!\", желтый - \"Жди\", а зеленый - \"Езжай\"."),
            ("reg.png", "Главный перекресток: Здесь всеми командует светофор. Машины и люди слушаются его сигналов."),
            ("unreg.png", "Обычный перекресток: Здесь нет светофора. Нужно внимательно посмотреть налево и направо, нет ли машин."),
            ("zebra.png", "Пешеходный переход: Это специальная дорожка \"Зебра\". Только по ней можно переходить через дорогу."),
            ("children.png", "Знак \"Дети\": Этот знак предупреждает водителей, что рядом школа или детский сад. Будьте осторожны!")
        ]
        self.current_index = 0

        self.img_frame = tk.Frame(self.root, width=600, height=450, bg="gray95")
        self.img_frame.pack_propagate(False)
        self.img_frame.pack(pady=20)

        self.img_view = tk.Label(self.img_frame, bg="gray95")
        self.img_view.pack(expand=True)

        self.txt_view = tk.Label(self.root, font=("Arial", 14, "bold"), wraplength=700)
        self.txt_view.pack(pady=10)

        self.nav_frame = tk.Frame(self.root)
        self.nav_frame.pack(side="bottom", pady=30)

        tk.Button(self.nav_frame, text="Назад", width=15, command=self.prev_item).pack(side="left", padx=10)
        tk.Button(self.nav_frame, text="Главная", width=15, command=self.show_home).pack(side="left", padx=10)
        tk.Button(self.nav_frame, text="Вперед", width=15, command=self.next_item).pack(side="left", padx=10)

        self.init_menu()
        self.show_home()
        self.root.after(500, self.welcome)

    def welcome(self):
        messagebox.showinfo("Приветствие", "Добро пожаловать в программу \"Перекресток\"!")

    def init_menu(self):
        m_bar = Menu(self.root)
        self.root.config(menu=m_bar)

        f_menu = Menu(m_bar, tearoff=0)
        m_bar.add_cascade(label="Файл", menu=f_menu)
        f_menu.add_command(label="Выход", command=self.root.quit)

        s_menu = Menu(m_bar, tearoff=0)
        m_bar.add_cascade(label="Светофоры", menu=s_menu)
        s_menu.add_command(label="Пешеходный", command=lambda: self.set_item(0))
        s_menu.add_command(label="Транспортный", command=lambda: self.set_item(1))

        p_menu = Menu(m_bar, tearoff=0)
        m_bar.add_cascade(label="Перекрестки", menu=p_menu)
        p_menu.add_command(label="Регулируемый", command=lambda: self.set_item(2))
        p_menu.add_command(label="Нерегулируемый", command=lambda: self.set_item(3))

        z_menu = Menu(m_bar, tearoff=0)
        m_bar.add_cascade(label="Знаки", menu=z_menu)
        z_menu.add_command(label="Пешеходный переход", command=lambda: self.set_item(4))
        z_menu.add_command(label="Дети", command=lambda: self.set_item(5))

    def update_display(self):
        name, desc = self.content[self.current_index]
        if os.path.exists(name):
            img = tk.PhotoImage(file=name)
            if img.width() > 600 or img.height() > 450:
                img = img.subsample(2, 2)
            self.photo = img
            self.img_view.config(image=self.photo, text="")
        else:
            self.img_view.config(image="", text=f"Файл {name} не найден")
        self.txt_view.config(text=desc)

    def set_item(self, index):
        self.current_index = index
        self.update_display()

    def next_item(self):
        self.current_index = (self.current_index + 1) % len(self.content)
        self.update_display()

    def prev_item(self):
        self.current_index = (self.current_index - 1) % len(self.content)
        self.update_display()

    def show_home(self):
        self.img_view.config(image="", text="Выберите раздел в меню")
        self.txt_view.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = CrossroadApp(root)
    root.mainloop()