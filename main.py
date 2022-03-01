import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog


class Edit_Dialog(QDialog):
    def __init__(self, dad, id):
        super().__init__()
        self.dad = dad
        self.id = id
        self.dad.statusbar.showMessage('')
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.setWindowTitle('Редактировать элемент')

        res = list(self.dad.con.cursor().execute(f"""SELECT * FROM coffee WHERE id = {id}"""))[0]
        print(res)
        self.sort.setText(res[1])
        self.stepen.setText(res[2])
        self.type.setText(res[3])
        self.smel.setText(res[4])
        self.price.setValue(res[5])
        self.massa.setValue(res[6])
        self.label_5.setHidden(True)
        self.setModal(True)
        self.pushButton.clicked.connect(self.edit_elem)

    def edit_elem(self):
        try:
            self.label_5.setHidden(True)
            assert self.sort.text() != ''
            assert self.stepen.text() != ''
            assert self.type.text() != ''
            assert self.smel.text() != ''
            self.dad.con.cursor().execute(f"UPDATE coffee SET "
                                          f"Сорт = '{self.sort.text()}', "
                                          f"Обжарка = '{self.stepen.text()}', "
                                          f"Зерна = '{self.type.text()}', "
                                          f"Вкус = '{self.smel.text()}', "
                                          f"Цена = {float(self.price.value())}, "
                                          f"Объем = {float(self.massa.value())} "
                                          f"WHERE id = {int(self.id)}")
            self.dad.con.commit()
            self.dad.update_result()
            self.close()
        except Exception as e:
            print(e)
            self.label_5.setHidden(False)


class Add_Dialog(QDialog):
    def __init__(self, dad):
        super().__init__()
        self.dad = dad
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.setWindowTitle('Добавить элемент')
        self.label_5.setHidden(True)  # невидимая надпись
        self.setModal(True)
        self.pushButton.clicked.connect(self.add_elem)

    def add_elem(self):
        try:
            self.label_5.setHidden(True)
            assert self.sort.text() != ''
            assert self.stepen.text() != ''
            assert self.type.text() != ''
            assert self.smel.text() != ''
            self.dad.con.cursor().execute(
                f"""INSERT INTO coffee(Сорт, Обжарка, Зерна, Вкус, Цена, Объем) VALUES ('{self.sort.text()}', 
                                            '{self.stepen.text()}', '{self.type.text()}', '{self.smel.text()}',
                                           {float(self.price.value())}, {float(self.massa.value())})""")
            self.dad.con.commit()
            self.dad.update_result()
            self.close()
        except Exception as e:
            print(e)
            self.label_5.setHidden(False)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.con = sqlite3.connect("coffee.db")
        self.name.setText('coffee.db')
        self.btn_load.clicked.connect(self.update_result)
        self.btn_edit.clicked.connect(self.edit_elem)
        self.btn_new.clicked.connect(self.add_elem)
        self.tableWidget.setColumnWidth(0, 20)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 115)
        self.tableWidget.setColumnWidth(3, 115)
        self.tableWidget.setColumnWidth(4, 115)
        self.tableWidget.setColumnWidth(5, 75)
        self.tableWidget.setColumnWidth(6, 100)

    def update_result(self):
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM coffee").fetchall()
        self.tableWidget.setRowCount(len(result))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def closeEvent(self, event):
        self.con.close()

    def add_elem(self):
        self.dialog = Add_Dialog(self)
        self.dialog.show()
        self.dialog.exec_()

    def edit_elem(self):
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        if len(rows) == 1:
            self.dialog = Edit_Dialog(self, self.tableWidget.item(rows[0], 0).text())
            self.dialog.show()
            self.dialog.exec_()
        else:
            self.statusbar.showMessage('Выберите один элемент')


# будет выводить понятно ошибку
def expert_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.__excepthook__ = expert_hook
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())

# pip install -r requirements.txt
