import cv2

def decodificar_qr_code(nome_arquivo):
    imagem = cv2.imread(nome_arquivo)
    detector = cv2.QRCodeDetector()
    _, mensagem, _ = detector.detectAndDecode(imagem)
    return mensagem

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo de imagem contendo o QR code: ")
    mensagem_decodificada = decodificar_qr_code(nome_arquivo)
    if mensagem_decodificada:
        print(f"A mensagem decodificada do QR code é: {mensagem_decodificada}")
    else:
        print("Não foi possível decodificar o QR code.")
