import sys
from typing import Union, Optional
from operator import add, sub, mul, truediv

import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFontDatabase

from py_calc import Ui_MainWindow

operations = {
    '+': add,
    '-': sub,
    '×': mul,
    '/': truediv
}

zero_div_err = 'Деление на 0!'
err_undefined = 'Неопределенная ошибка'

def_font = 15
def_lineedit_font = 40


class Calc(QMainWindow):
    def __init__(self):
        super(Calc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.maxlen = self.ui.lineEdit.maxLength()

        QFontDatabase.addApplicationFont('E:\Downloads\San Francisco Pro Text\SF-Pro-Display-Light.otf')

        # Digits
        self.ui.btn_0.clicked.connect(lambda: self.add_digits('0'))
        self.ui.btn_1.clicked.connect(lambda: self.add_digits('1'))
        self.ui.btn_2.clicked.connect(lambda: self.add_digits('2'))
        self.ui.btn_3.clicked.connect(lambda: self.add_digits('3'))
        self.ui.btn_4.clicked.connect(lambda: self.add_digits('4'))
        self.ui.btn_5.clicked.connect(lambda: self.add_digits('5'))
        self.ui.btn_6.clicked.connect(lambda: self.add_digits('6'))
        self.ui.btn_7.clicked.connect(lambda: self.add_digits('7'))
        self.ui.btn_8.clicked.connect(lambda: self.add_digits('8'))
        self.ui.btn_9.clicked.connect(lambda: self.add_digits('9'))

        # functions
        self.ui.btn_c.clicked.connect(self.clear_all)
        self.ui.btn_point.clicked.connect(self.point)
        self.ui.btn_min_add.clicked.connect(self.negative)
        self.ui.btn_backspace.clicked.connect(self.backspace)

        # math
        self.ui.btn_equal.clicked.connect(self.calculate)
        self.ui.btn_add.clicked.connect(lambda: self.math_oper('+'))
        self.ui.btn_minus.clicked.connect(lambda: self.math_oper('-'))
        self.ui.btn_mul.clicked.connect(lambda: self.math_oper('×'))
        self.ui.btn_div.clicked.connect(lambda: self.math_oper('/'))

    def add_digits(self, btn_text: str) -> None:
        self.del_error()
        if self.ui.lineEdit.text() == '0':
            self.ui.lineEdit.setText(btn_text)
        else:
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + btn_text)

        self.adjust_enter_font()

    def point(self):
        if '.' not in self.ui.lineEdit.text():
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + '.')
            self.adjust_enter_font()

    def backspace(self) -> None:
        self.del_error()
        enter = self.ui.lineEdit.text()

        if len(enter) != 1:
            if len(enter) == 2 and '-' in enter:
                self.ui.lineEdit.setText('0')
            else:
                self.ui.lineEdit.setText(enter[:-1])
        else:
            self.ui.lineEdit.setText('0')

        self.adjust_enter_font()

    def clear_all(self) -> None:
        self.del_error()
        self.ui.lineEdit.setText('0')
        self.adjust_enter_font()
        self.ui.label.clear()
        self.adjust_label_font()

    def add_memory_label(self, sign: str):
        if not self.ui.label.text() or self.get_math_sigh_label() == '=':
            self.ui.label.setText(self.del_zeros(self.ui.lineEdit.text()) + f' {sign} ')
            self.adjust_label_font()
            self.ui.lineEdit.setText('0')
            self.adjust_enter_font()

    @staticmethod
    def del_zeros(num: str) -> str:
        n = str(float(num))
        return n[:-2] if n[-2:] == '.0' else n

    def get_num(self) -> Union[int, float]:
        enter = self.ui.lineEdit.text().strip('.')
        return float(enter) if '.' in enter else int(enter)

    def get_label_num(self) -> Union[int, float, None]:
        if self.ui.label.text():
            temp = self.ui.label.text().strip('.').split()[0]
        return float(temp) if '.' in temp else int(temp)

    def get_math_sigh_label(self) -> Optional[str]:
        if self.ui.label.text():
            return self.ui.label.text().strip('.').split()[-1]

    def get_enter_text(self) -> int:
        return self.ui.lineEdit.fontMetrics().boundingRect(self.ui.lineEdit.text()).width()

    def get_label_text(self) -> int:
        return self.ui.label.fontMetrics().boundingRect(self.ui.label.text()).width()

    def calculate(self) -> Optional[str]:
        enter = self.ui.lineEdit.text()
        temp = self.ui.label.text()

        try:
            if temp:
                res = self.del_zeros(
                    str(operations[self.get_math_sigh_label()](self.get_label_num(), self.get_num()))
                )
                self.ui.label.setText(temp + self.del_zeros(enter) + ' =')
                self.adjust_label_font()
                self.ui.lineEdit.setText(res)
                self.adjust_enter_font()
                return res
        except KeyError:
            pass
        except ZeroDivisionError:
            if self.get_label_num() == 0:
                self.error(err_undefined)
            else:
                self.error(zero_div_err)

    def math_oper(self, math_sign: str):
        temp = self.ui.label.text()

        try:
            if not temp:
                self.add_memory_label(math_sign)
            else:
                if self.get_math_sigh_label() != math_sign:
                    if self.get_math_sigh_label() == '=':
                        self.add_memory_label(math_sign)
                    else:
                        self.ui.label.setText(temp[:-2] + f' {math_sign} ')
                else:
                    self.ui.label.setText(self.calculate() + f' {math_sign} ')
        except TypeError:
            pass

        self.adjust_label_font()

    def error(self, text: str) -> None:
        self.ui.lineEdit.setMaxLength(len(text))
        self.ui.lineEdit.setText(text)
        self.adjust_enter_font()
        self.off_buttons(True)

    def del_error(self) -> None:
        if self.ui.lineEdit.text() in (err_undefined, zero_div_err):
            self.ui.lineEdit.setMaxLength(self.maxlen)
            self.ui.lineEdit.setText('0')
            self.adjust_enter_font()
            self.off_buttons(False)

    def off_buttons(self, off: bool) -> None:
        self.ui.btn_equal.setDisabled(off)
        self.ui.btn_add.setDisabled(off)
        self.ui.btn_minus.setDisabled(off)
        self.ui.btn_mul.setDisabled(off)
        self.ui.btn_min_add.setDisabled(off)
        self.ui.btn_point.setDisabled(off)
        self.ui.btn_div.setDisabled(off)

        clr = 'color: #999;' if off else ("QPushButton {\n"
                                          "    background-color: #eba352;\n"
                                          "    border: none;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    background-color: #dbb284;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    background-color: #fafafa;\n"
                                          "    color: #eba352;\n"
                                          "    \n"
                                          "}")
        self.change_btn_clr(clr)

    def negative(self):
        enter = self.ui.lineEdit.text()

        if '-' not in enter:
            if enter != '0':
                enter = '-' + enter
        else:
            enter = enter[1:]

        if len(enter) == self.maxlen + 1 and '-' in enter:
            self.ui.lineEdit.setMaxLength(self.maxlen + 1)
        else:
            self.ui.lineEdit.setMaxLength(self.maxlen)

        self.ui.lineEdit.setText(enter)
        self.adjust_enter_font()

    def change_btn_clr(self, color: str) -> None:
        self.ui.btn_equal.setStyleSheet(color)
        self.ui.btn_add.setStyleSheet(color)
        self.ui.btn_minus.setStyleSheet(color)
        self.ui.btn_mul.setStyleSheet(color)
        self.ui.btn_min_add.setStyleSheet(color)
        self.ui.btn_div.setStyleSheet(color)

    def adjust_enter_font(self) -> None:
        font_size = def_font
        while self.get_enter_text() > self.ui.lineEdit.width() - 15:
            font_size -= 1
            self.ui.lineEdit.setStyleSheet('font-size: ' + str(font_size) + 'pt; border: none;')
        font_size = 1
        while self.get_enter_text() < self.ui.lineEdit.width() - 60:
            font_size += 1

            if font_size > def_lineedit_font:
                break

            self.ui.lineEdit.setStyleSheet('font-size: ' + str(font_size) + 'pt; border: none;')

    def adjust_label_font(self) -> None:
        font_size = def_font
        while self.get_label_text() > self.ui.label.width() - 10:
            font_size -= 1
            self.ui.label.setStyleSheet('font-size: ' + str(font_size) + 'pt; border: none;')
        font_size = 1
        while self.get_label_text() < self.ui.label.width() - 60:
            font_size += 1

            if font_size > def_font:
                break

            self.ui.label.setStyleSheet('font-size: ' + str(font_size) + 'pt; border: none;')

    def resizeEvent(self, event) -> None:
        self.adjust_enter_font()
        self.adjust_label_font()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calc()
    window.show()
    sys.exit(app.exec())
