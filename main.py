# Versão com geração de vCard e QR Code

import sys, os
import qrcode
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QFormLayout,
    QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QMessageBox
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerador de QR de Contato")
        self.setWindowIcon(QIcon("assets/icon.png"))  # ícone na janela
        self._build_ui()

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        # Campos do formulário
        form = QFormLayout()
        self.input_name = QLineEdit(); form.addRow("Nome completo:", self.input_name)
        self.input_country = QLineEdit(); self.input_country.setPlaceholderText("Ex: 55"); form.addRow("Código do país:", self.input_country)
        self.input_ddd = QLineEdit(); self.input_ddd.setPlaceholderText("Ex: 11"); form.addRow("DDD:", self.input_ddd)
        self.input_number = QLineEdit(); self.input_number.setPlaceholderText("Ex: 999999999"); form.addRow("Número:", self.input_number)
        self.input_email = QLineEdit(); form.addRow("Email:", self.input_email)
        self.input_address = QTextEdit(); self.input_address.setFixedHeight(60); form.addRow("Endereço:", self.input_address)

        # Botão principal
        self.btn_generate = QPushButton("Gerar QR")
        self.btn_generate.clicked.connect(self.on_generate)

        # Layout
        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(self.btn_generate)
        central.setLayout(layout)

    def on_generate(self):
        # Pegando dados digitados
        name = self.input_name.text().strip()
        country = self.input_country.text().strip()
        ddd = self.input_ddd.text().strip()
        number = self.input_number.text().strip()
        email = self.input_email.text().strip()
        address = self.input_address.toPlainText().strip()

        # Validação básica
        if not name or not number:
            QMessageBox.warning(self, "Erro", "Nome e número são obrigatórios!")
            return

        phone = f"+{country}{ddd}{number}"

        # Montando vCard
        vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
ADR:{address}
END:VCARD
"""

        # Garante que a pasta existe
        os.makedirs("qrcodes", exist_ok=True)

        # Salva arquivo vCard
        vcf_path = os.path.join("qrcodes", f"{name}.vcf")
        with open(vcf_path, "w", encoding="utf-8") as f:
            f.write(vcard)

        # Gera QR Code a partir do vCard
        qr = qrcode.make(vcard)
        img_path = os.path.join("qrcodes", f"{name}.png")
        qr.save(img_path)

        # Mensagem final
        QMessageBox.information(
            self,
            "Sucesso",
            f"Arquivos gerados:\n{vcf_path}\n{img_path}"
        )

def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.resize(480, 420)  # define tamanho inicial da janela
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()