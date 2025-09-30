# Primeira versão da interface gráfica do app

import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QFormLayout,
    QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QMessageBox
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerador de QR de Contato")

        # Definindo ícone do aplicativo
        self.setWindowIcon(QIcon("assets/icon.png"))

        self._build_ui()

    def _build_ui(self):
        # Layout central da janela
        central = QWidget()
        self.setCentralWidget(central)

        # Formulário com os campos do contato
        form = QFormLayout()
        self.input_name = QLineEdit(); form.addRow("Nome completo:", self.input_name)
        self.input_country = QLineEdit(); form.addRow("Código do país:", self.input_country)
        self.input_ddd = QLineEdit(); form.addRow("DDD:", self.input_ddd)
        self.input_number = QLineEdit(); form.addRow("Número:", self.input_number)
        self.input_email = QLineEdit(); form.addRow("Email:", self.input_email)
        self.input_address = QTextEdit(); form.addRow("Endereço:", self.input_address)

        # Botão para gerar QR (ainda só de teste)
        self.btn_generate = QPushButton("Gerar QR")
        self.btn_generate.clicked.connect(self.on_generate)

        # Layout principal (form + botão)
        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(self.btn_generate)
        central.setLayout(layout)

    def on_generate(self):
        # Por enquanto só mostra uma mensagem de teste
        QMessageBox.information(self, "Teste", "Botão funcionando!")

def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()