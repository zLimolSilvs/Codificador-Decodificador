import qrcode # type: ignore

def criar_qr_code(mensagem, nome_arquivo='qrcode.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(mensagem)
    qr.make(fit=True)

    imagem_qr = qr.make_image(fill_color="black", back_color="white")
    imagem_qr.save(nome_arquivo)

if __name__ == "__main__":
    mensagem = input("Digite a mensagem para criar o QR code: ")
    criar_qr_code(mensagem)
    print(f"O QR code com a mensagem '{mensagem}' foi criado com sucesso!")
