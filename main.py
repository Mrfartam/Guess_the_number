from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from random import randint
from kivy.core.window import Window


class MyApp(App):

    def __init__(self):
        super().__init__()
        self.begin = 0
        self.end = 0
        self.vv = 0
        self.zag = 0
        self.k = 0
        self.box = BoxLayout(orientation='vertical')

    def pressed_begin(self, z):
        self.box.clear_widgets()
        Window.clearcolor = [197 / 255, 1, 0, 1]
        Window.title = 'Первое число'
        lbl2 = Label(text='Введите первое число\nи нажмите "Дальше"', halign='center', font_size=30)
        lbl2.color = [47 / 255, 0, 87 / 255, 1]
        entr2 = TextInput(font_size=30, multiline=False, is_focusable=True)
        entr2.background_color = [1, 1, 1, 1]
        entr2.foreground_color = [0, 0, 0, 1]
        entr2.halign = 'center'
        entr2.bind(on_text_validate=self.vvod_text_first)
        btn2 = Button(text='Дальше', font_size=30,
                      background_color=[119 / 255, 18 / 255, 150 / 255, 1], background_normal='')
        btn2.color = [243 / 255, 207 / 255, 34 / 255, 1]
        btn2.bind(on_press=self.pressed_end)
        self.box.add_widget(lbl2)
        self.box.add_widget(entr2)
        self.box.add_widget(btn2)
        return self.box

    def pressed_end(self, z):
        self.box.clear_widgets()
        Window.clearcolor = [197 / 255, 1, 0, 1]
        Window.title = 'Последнее число'
        lbl3 = Label(text='Введите последнее число\nи нажмите "Начать"', halign='center', font_size=30)
        lbl3.color = [47 / 255, 0, 87 / 255, 1]
        entr3 = TextInput(font_size=30, multiline=False, is_focusable=True)
        entr3.background_color = [1, 1, 1, 1]
        entr3.foreground_color = [0, 0, 0, 1]
        entr3.halign = 'center'
        entr3.bind(on_text_validate=self.vvod_text_last)
        btn3 = Button(text='Начать', font_size=30,
                      background_color=[119 / 255, 18 / 255, 150 / 255, 1], background_normal='')
        btn3.color = [243 / 255, 207 / 255, 34 / 255, 1]
        btn3.bind(on_press=self.pressed_start)
        self.box.add_widget(lbl3)
        self.box.add_widget(entr3)
        self.box.add_widget(btn3)
        return self.box

    def pressed_start(self, z):
        self.box.clear_widgets()
        Window.clearcolor = [197 / 255, 1, 0, 1]
        Window.title = 'Попытка'
        lbl4 = Label(text='Попробуй угадать загаданное число', halign='center', font_size=30)
        lbl4.color = [47 / 255, 0, 87 / 255, 1]
        entr4 = TextInput(font_size=30, multiline=False, is_focusable=True)
        entr4.background_color = [1, 1, 1, 1]
        entr4.foreground_color = [0, 0, 0, 1]
        entr4.halign = 'center'
        entr4.bind(on_text_validate=self.vvod_text)
        btn4 = Button(text='Нажмите сюда после ввода', font_size=30,
                      background_color=[119 / 255, 18 / 255, 150 / 255, 1], background_normal='')
        btn4.color = [243 / 255, 207 / 255, 34 / 255, 1]
        btn4.bind(on_press=self.pressed_prov)
        self.box.add_widget(lbl4)
        self.box.add_widget(entr4)
        self.box.add_widget(btn4)
        return self.box

    def pressed_prov(self, z):
        self.box.clear_widgets()
        if self.vv < self.zag:
            self.less()
        elif self.vv > self.zag:
            self.more()
        elif self.vv == self.zag:
            Window.clearcolor = [2 / 255, 194 / 255, 4 / 255, 1]
            Window.title = 'Победа!!!'
            lbl8 = Label(text='Загаданное число равно введённому!!!', halign='center', font_size=30)
            lbl8.color = [0, 0, 0, 1]
            btn8 = Button(text='Сыграть ещё раз', font_size=30,
                          background_color=[1, 0, 0, 1], background_normal='')
            btn8.color = [205 / 255, 205 / 255, 180 / 255, 1]
            btn8.bind(on_press=self.pressed_begin)
            self.box.add_widget(lbl8)
            self.box.add_widget(btn8)

    def less(self):
        Window.clearcolor = [127 / 255, 1, 212 / 255, 1]
        Window.title = 'Неверный ответ'
        lbl6 = Label(text='Загаданное число больше введённого', halign='center', font_size=30)
        lbl6.color = [75 / 255, 0, 130 / 255, 1]
        btn6 = Button(text='Попробовать ещё раз', font_size=30,
                      background_color=[148 / 255, 0, 211 / 255, 1], background_normal='')
        btn6.color = [1, 1, 0, 1]
        btn6.bind(on_press=self.pressed_start)
        self.box.add_widget(lbl6)
        self.box.add_widget(btn6)
        return self.box

    def more(self):
        Window.clearcolor = [127 / 255, 1, 212 / 255, 1]
        Window.title = 'Неверный ответ'
        lbl7 = Label(text='Загаданное число меньше введённого', halign='center', font_size=30)
        lbl7.color = [75 / 255, 0, 130 / 255, 1]
        btn7 = Button(text='Попробовать ещё раз', font_size=30,
                      background_color=[148 / 255, 0, 211 / 255, 1], background_normal='')
        btn7.color = [1, 1, 0, 1]
        btn7.bind(on_press=self.pressed_start)
        self.box.add_widget(lbl7)
        self.box.add_widget(btn7)
        return self.box

    def pressed_error(self, z):
        Window.clearcolor = [1, 0, 0, 1]
        Window.title = 'Ошибка'
        self.box.clear_widgets()
        lbl5 = Label(text='Первое число должно быть меньше,\nчем последнее', halign='center', font_size=30)
        lbl5.color = [1, 1, 0, 1]
        btn5 = Button(text='Начать сначала', font_size=30,
                      background_color=[1, 128 / 255, 0, 1], background_normal='')
        btn5.color = [170 / 255, 170 / 255, 170 / 255, 1]
        btn5.bind(on_press=self.pressed_begin)
        self.box.add_widget(lbl5)
        self.box.add_widget(btn5)
        return self.box

    def vvod_text_first(self, first):
        self.begin = int(first.text)

    def vvod_text_last(self, last):
        self.end = int(last.text)
        if self.begin > self.end:
            self.pressed_error(540)
        else:
            self.zag = randint(self.begin, self.end)

    def vvod_text(self, vvod):
        self.vv = int(vvod.text)

    def pressed_exit(self, z):
        Window.close()

    def build(self):
        Window.clearcolor = [0, 250 / 255, 154 / 255, 1]
        Window.title = 'Начало'
        if self.k > 0:
            self.box.clear_widgets()
        else:
            self.k += 1
        lbl1 = Label(text='Угадай число\nПравила игры: сначала вы вводите диапазон\n чисел (первое и последнее). '
                          'После этого\nпытаетесь отгадать случайно выбранное\n число из этого '
                          'диапазона.', halign='center', font_size=30)
        lbl1.disabled_color = [0, 250 / 255, 154 / 255, 1]
        lbl1.color = [100 / 255, 100 / 255, 100 / 255, 1]
        btn1 = Button(text='Играть', font_size=30,
                      background_color=[134 / 255, 85 / 255, 138 / 255, 1], background_normal='')
        btn1.color = [200 / 255, 200 / 255, 200 / 255, 1]
        btn1.bind(on_press=self.pressed_begin)
        self.box.add_widget(lbl1)
        self.box.add_widget(btn1)
        btn0 = Button(text='X', font_size=30, background_color=[1, 0, 0, 1], background_normal='',
                      size_hint=(0.07, 0.035))
        btn0.color = [1, 1, 1, 1]
        btn0.bind(on_press=self.pressed_exit)
        anch = AnchorLayout(anchor_x='right', anchor_y='top')
        anch.add_widget(btn0)
        anch.add_widget(self.box)
        return anch


if __name__ == '__main__':
    MyApp().run()