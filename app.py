import streamlit as st
import base64
from PIL import Image
from io import BytesIO

# Função para obter imagem em formato base64 sem alterações para GIFs
def get_image_base64(path, is_image=False):
    if is_image:
        with Image.open(path) as img:
            # Redimensionar mantendo a proporção
            img.thumbnail((500, 300), Image.Resampling.LANCZOS)  # Uso de LANCZOS para redimensionamento de qualidade
            
            # Obter dimensões para cortar no centro
            width, height = img.size
            left = (width - 500) / 2
            top = (height - 200) / 2
            right = (width + 500) / 2
            bottom = (height + 450) / 2
            
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
profissoes_gifs = {
    "Médico": get_image_base64("profissoes/Medic@-1.gif"),
    "Engenheiro": get_image_base64("profissoes/Engenheir@-1.gif"),
    "Professor": get_image_base64("profissoes/Professor@-1.gif")
}
transportes_gifs = {
    "Avião": get_image_base64("transportes/Aviao-1.gif"),
    "Barco": get_image_base64("transportes/Barco-1.gif"),
    "Bicicleta": get_image_base64("transportes/Bicicleta-1.gif")
}
profissoes_imgs = {
    "Médico": get_image_base64("profissoes/médico.png", is_image=True),
    "Engenheiro": get_image_base64("profissoes/engenheiro.png", is_image=True),
    "Professor": get_image_base64("profissoes/professor.png", is_image=True)
}
transportes_imgs = {
    "Avião": get_image_base64("transportes/aviao.png", is_image=True),
    "Barco": get_image_base64("transportes/barco.png", is_image=True),
    "Bicicleta": get_image_base64("transportes/bike.png", is_image=True)
}

# Imagens do menu principal
encoded_image_profissoes = get_image_base64("menu_principal/profissoes.gif")
encoded_image_transporte = get_image_base64("menu_principal/meiostransporte.gif")

# Definir a página de profissões
def pagina_profissoes():
    st.header("Profissões")
    if st.button("Voltar ao Menu Principal"):
        st.session_state['pagina_atual'] = 'menu'
    # Seleção da profissão
    profissao = st.selectbox("Escolha uma profissão:", list(profissoes_gifs.keys()))
    
    # Exibir imagens e GIFs
    if profissao:
        col1, col2 = st.columns(2)
        with col1:
            st.image(profissoes_imgs[profissao], width=300, caption=f"Imagem de {profissao}")
        with col2:
            st.image(profissoes_gifs[profissao], width=300, caption=f"GIF representando {profissao}")

# Definir a página de meios de transporte
def pagina_transportes():
    st.header("Meios de Transporte")
    if st.button("Voltar ao Menu Principal"):
        st.session_state['pagina_atual'] = 'menu'
    # Seleção da profissão
    transporte = st.selectbox("Escolha um meio de transporte:", list(transportes_gifs.keys()))
    
    # Exibir imagens e GIFs
    if transporte:
        col1, col2 = st.columns(2)
        with col1:
            st.image(transportes_imgs[transporte], width=300, caption=f"Imagem de {transporte}")
        with col2:
            st.image(transportes_gifs[transporte], width=300, caption=f"GIF representando {transporte}")

# Menu principal com GIFs como botões visuais
def menu_principal():
    st.title("Menu Principal")
    col1, col2 = st.columns(2)
    with col1:
        st.image(encoded_image_profissoes, caption="Profissões", width=300)
        if st.button("Clique para Profissões", key="profissoes"):
            st.session_state['pagina_atual'] = 'profissoes'
    with col2:
        st.image(encoded_image_transporte, caption="Meio de Transporte", width=300)
        if st.button("Clique para Transportes", key="transportes"):
            st.session_state['pagina_atual'] = 'transportes'

# Gerenciar as páginas
if 'pagina_atual' not in st.session_state:
    st.session_state['pagina_atual'] = 'menu'

if st.session_state['pagina_atual'] == 'menu':
    menu_principal()
elif st.session_state['pagina_atual'] == 'profissoes':
    pagina_profissoes()
elif st.session_state['pagina_atual'] == 'transportes':
    pagina_transportes()