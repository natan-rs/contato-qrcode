Gerador de QR de Contatos

Aplicação desktop para gerar QR Codes de contatos no formato vCard.

Funcionalidades
- Inserir dados do contato (nome, telefone, email, endereço)
- Gerar QR Code a partir das informações
- Salvar arquivo `.vcf` (cartão de contato)
- Salvar imagem `.png` do QR Code
- Exibir mensagens de sucesso ou erro

Estrutura do projeto
- main.py -> aplicação principal (UI e lógica)
- requirements.txt -> dependências
- README.md -> documentação
- .gitignore -> arquivos ignorados pelo git
- assets/icon.png -> ícone do aplicativo
- qrcodes/ -> saída (QR Codes e vCards)

Tecnologias utilizadas
- Python (PySide6)
- qrcode
- Pillow