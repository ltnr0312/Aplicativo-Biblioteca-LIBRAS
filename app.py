# Importar bibliotecas
import streamlit as st
import base64
from PIL import Image
from io import BytesIO

# Carregar o CSS
with open("styles/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Função para obter imagem em formato base64 sem alterações para GIFs
def get_image_base64(path, is_image=False):
    if is_image:
        with Image.open(path) as img:
            # Redimensionar mantendo a proporção
            img.thumbnail((300, 300), Image.Resampling.LANCZOS)  # Uso de LANCZOS para redimensionamento de qualidade
            
            # Obter dimensões para cortar no centro
            width, height = img.size
            left = (width - 300) / 2
            top = (height - 300) / 2
            right = (width + 300) / 2
            bottom = (height + 300) / 2
            
            # Cortar a imagem
            img_cropped = img.crop((left, top, right, bottom))
            
            # Converter para base64
            buffer = BytesIO()
            img_cropped.save(buffer, format="PNG")
            encoded_string = base64.b64encode(buffer.getvalue()).decode()
    else:
        with open(path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
    
    return "data:image/png;base64," + encoded_string

# Carregar todas as imagens e GIFs e convertê-las para base64
ferramentas_imgs = {
    "Ponte Rolante e Talha": get_image_base64("ferramentas/ponterolante.png", is_image=True),
    "Alicate": get_image_base64("ferramentas/alicate.png", is_image=True),
    "Dolly": get_image_base64("ferramentas/dolly.png", is_image=True),
    "Parafusadeira Pneumática": get_image_base64("ferramentas/parafusadeirapneumatica.png", is_image=True),
    "Parafusadeira Elétrica": get_image_base64("ferramentas/parafusadeiraeletrica.png", is_image=True),
    "Prensa Hidráulica": get_image_base64("ferramentas/prensahidraulica.png", is_image=True),
    "Prensa Pneumática": get_image_base64("ferramentas/prensapneumatica.png", is_image=True),
    "Torquímetro": get_image_base64("ferramentas/torquimetro.png", is_image=True)
}
ferramentas_gifs = {
    "Ponte Rolante e Talha": get_image_base64("ferramentas/ponterolante.gif"),
    "Alicate": get_image_base64("ferramentas/alicate.gif"),
    "Dolly": get_image_base64("ferramentas/dolly.gif"),
    "Parafusadeira Pneumática": get_image_base64("ferramentas/parafusadeirapneumatica.gif"),
    "Parafusadeira Elétrica": get_image_base64("ferramentas/parafusadeiraeletrica.gif"),
    "Prensa Hidráulica": get_image_base64("ferramentas/prensahidraulica.gif"),
    "Prensa Pneumática": get_image_base64("ferramentas/prensapneumatica.gif"),
    "Torquímetro": get_image_base64("ferramentas/torquimetro.gif")
}

# Imagens do menu principal
encoded_image_ferramentas = get_image_base64("menu_principal/ferramentas.gif")

# Definir a página ferramentas
def pagina_ferramentas():
    st.header("FERRAMENTAS")
    ferramenta = st.selectbox("Escolha uma ferramenta:", list(ferramentas_gifs.keys()))
    
    # Exibir imagens e GIFs
    if ferramenta:
        col1, col2 = st.columns(2)
        with col1:
            st.image(ferramentas_imgs[ferramenta], width=300, caption=f"Imagem de {ferramenta}")
        with col2:
            st.image(ferramentas_gifs[ferramenta], width=300, caption=f"GIF representando {ferramenta}")

# Mostrar diretamente a página de ferramentas
pagina_ferramentas()