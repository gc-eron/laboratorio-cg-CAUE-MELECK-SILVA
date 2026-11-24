import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

foto = Image.open("imagens/foto_trabalho.jpg").convert("RGB")
img = np.array(foto)
altura, largura = img.shape[0], img.shape[1]
st.image(img, caption="Foto original", width=300)

st.header("8. Negativo")
negativo = 255 - img
st.image(negativo, caption="Negativo da foto", width=350)

st.header("9. Recorte")
tamanho = st.slider("Tamanho do recorte", 1, min(altura, largura) - 1, min(altura, largura) // 2)
y = st.slider("Linha inicial do recorte", 0, altura - tamanho, (altura - tamanho) // 2)
x = st.slider("Coluna inicial do recorte", 0, largura - tamanho, (largura - tamanho) // 2)
recorte = img[y:y + tamanho, x:x + tamanho]
st.image(recorte, caption="Recorte quadrado", width=350)

st.header("11. Espelhamento")
col1, col2 = st.columns(2)
col1.image(img[:, ::-1], caption="Espelho horizontal", width=300)
col2.image(img[::-1, :], caption="Espelho vertical", width=300)

st.header("12. Simetria")
metade = largura // 2
simetrica = img.copy()
simetrica[:, -metade:] = img[:, :metade][:, ::-1]
st.image(simetrica, caption="Metade esquerda espelhada na direita", width=350)

st.header("20. Pixel art")
passo = st.slider("Passo dos pixels", 1, 40, 12)
reduzida = img[::passo, ::passo]
ampliada = reduzida.repeat(passo, axis=0).repeat(passo, axis=1)
st.image(ampliada[:altura, :largura], caption="Pixel art", width=350)
