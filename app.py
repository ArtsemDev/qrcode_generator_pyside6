from PySide6.QtWidgets import QApplication, QWidget

from templates.window import Ui_Form


if __name__ == "__main__":
    import sys

    app = QApplication()
    w = Ui_Form()
    form = QWidget()
    w.setupUi(form)
    form.show()
    sys.exit(app.exec())
