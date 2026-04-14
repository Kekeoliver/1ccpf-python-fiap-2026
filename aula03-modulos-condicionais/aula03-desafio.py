#EXERCICIO 1
import pygame
import time


def tocar_musica(nome_arquivo):
    # Inicializa o mixer do pygame
    pygame.mixer.init()

    try:
        # Carrega o arquivo
        pygame.mixer.music.load(nome_arquivo)
        print(f"Reproduzindo: {nome_arquivo}")

        # Inicia a reprodução
        pygame.mixer.music.play()

        # O script precisa continuar rodando enquanto a música toca
        while pygame.mixer.music.get_busy():
            time.sleep(1)

    except pygame.error as e:
        print(f"Erro ao tocar o arquivo: {e}")


if __name__ == "__main__":
    tocar_musica("vilarejo.mp3")




