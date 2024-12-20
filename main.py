import sys
from pathlib import Path

from PyQt6.QtWidgets import *

from design import Ui_MainWindow
from excel import create_examples


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.selectDir.clicked.connect(self.setDir)
        self.ui.startBtn.clicked.connect(self.generate)

        self.uploadDir = ''

        themes_dict = {'Операции с целыми числами': 1}
        self.ui.themeBox.addItems([i for i in themes_dict])


    def setDir(self):
        home_dir = str(Path.home())
        dir_choose = QFileDialog.getExistingDirectory(
            self, 
            'Выберите папку', 
            home_dir
        )

        if dir_choose:
            dir_choose = dir_choose + '/'
            self.ui.currentDir.setText(f'Выбранная папка: {dir_choose}')
            self.uploadDir = dir_choose

    
    def generate(self):
        
        if not self.uploadDir:
            QMessageBox.warning(self, "Предупреждение", "Сначала выберите папку!")
            return

        if not self.ui.minValue.text() or not self.ui.maxValue.text():
            QMessageBox.warning(self, "Предупреждение", "Введите диапазон чисел!")
            return
        
        try:
        
            create_examples(
                dir=self.uploadDir,
                actions=['+', '-'],
                number_range=[
                    int(self.ui.minValue.text()),
                    int(self.ui.maxValue.text()),
                ],
                only_positive=True
            )

            QMessageBox.information(self, "Успешно", "Нужные файлы были созданы в указанной папке.")
            return
        
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Предупреждение", "При работе возникла ошибка!")
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())