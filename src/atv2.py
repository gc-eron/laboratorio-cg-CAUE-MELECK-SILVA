import numpy as np
import streamlit as st


def ampliar(imagem, fator=30):
    return imagem.repeat(fator, axis=0).repeat(fator, axis=1)


branco = (255, 255, 255)
azul = (6, 33, 86)
vermelho = (218, 18, 20)

bandeira = np.zeros((48, 72, 3), dtype=np.uint8)
bandeira[:] = branco
bandeira[:24, 36:] = vermelho
bandeira[24:, :36] = azul

estrela = np.array(
    [
        list(linha)
        for linha in (
            ".....##.....",
            ".....##.....",
            "....####....",
            "....####....",
            "############",
            ".##########.",
            "..########..",
            "...######...",
            "...######...",
            "..###..###..",
            "..##....##..",
            ".##......##.",
        )
    ]
) == "#"

bandeira[6:18, 12:24][estrela] = azul
bandeira[30:42, 48:60][estrela] = vermelho

st.title("Bandeira do Panamá")
st.image(ampliar(bandeira))
