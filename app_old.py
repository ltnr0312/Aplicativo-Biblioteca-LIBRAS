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

profissoes_imgs = {
    "Médico": get_image_base64("profissoes/médico.png", is_image=True),
    "Engenheiro": get_image_base64("profissoes/engenheiro.png", is_image=True),
    "Professor": get_image_base64("profissoes/professor.png", is_image=True)
}
profissoes_gifs = {
    "Médico": get_image_base64("profissoes/Medic@-1.gif"),
    "Engenheiro": get_image_base64("profissoes/Engenheir@-1.gif"),
    "Professor": get_image_base64("profissoes/Professor@-1.gif")
}

transportes_imgs = {
    "Avião": get_image_base64("transportes/aviao.png", is_image=True),
    "Barco": get_image_base64("transportes/barco.png", is_image=True),
    "Bicicleta": get_image_base64("transportes/bike.png", is_image=True)
}

transportes_gifs = {
    "Avião": get_image_base64("transportes/Aviao-1.gif"),
    "Barco": get_image_base64("transportes/Barco-1.gif"),
    "Bicicleta": get_image_base64("transportes/Bicicleta-1.gif")
}



# Imagens do menu principal
encoded_image_ferramentas = get_image_base64("menu_principal/ferramentas.gif")
encoded_image_profissoes = get_image_base64("menu_principal/profissoes.gif")
encoded_image_transporte = get_image_base64("menu_principal/meiosdetransporte.gif")


# Definir a página ferramentas
def pagina_ferramentas():
    st.header("FERRAMENTAS")
    if st.button("Voltar ao Menu Principal"):
        st.session_state.pagina_atual = 'menu'
        st.experimental_rerun()  # Force a rerun to immediately update the state
    # Seleção da profissão
    ferramenta = st.selectbox("Escolha uma ferramenta:", list(ferramentas_gifs.keys()))
    
    # Exibir imagens e GIFs
    if ferramenta:
        col1, col2 = st.columns(2)
        with col1:
            st.image(ferramentas_imgs[ferramenta], width=300, caption=f"Imagem de {ferramenta}")
        with col2:
            st.image(ferramentas_gifs[ferramenta], width=300, caption=f"GIF representando {ferramenta}")

# Definir a página de profissões
def pagina_profissoes():
    st.header("Profissões")
    if st.button("Voltar ao Menu Principal"):
        st.session_state.pagina_atual = 'menu'
        st.experimental_rerun()  # Force a rerun to immediately update the state
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
        st.session_state.pagina_atual = 'menu'
        st.experimental_rerun()  # Force a rerun to immediately update the state
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
    st.subheader("Escolha uma opção:")
    col1, col2, col3 = st.columns(3)
    with col3:
        st.image(encoded_image_profissoes, caption="PROFISSÕES", width=230)
        if st.button("CLIQUE AQUI PARA PROFISSÕES", key="profissoes"):
            st.session_state.pagina_atual = 'profissoes'
            st.experimental_rerun()  # Force a rerun to immediately update the state
    with col2:
        st.image(encoded_image_transporte, caption="MEIO DE TRANSPORTE", width=230)
        if st.button("CLIQUE AQUI PARA TRANSPORTES", key="transportes"):
            st.session_state.pagina_atual = 'transportes'
            st.experimental_rerun()  # Force a rerun to immediately update the state
    with col1:
        st.image(encoded_image_ferramentas, caption="FERRAMENTAS", width=230)
        if st.button("CLIQUE AQUI PARA FERRAMENTAS", key="ferramentas"):
            st.session_state.pagina_atual = 'ferramentas'
            st.experimental_rerun()  # Force a rerun to immediately update the state

# Gerenciar as páginas
if 'pagina_atual' not in st.session_state:
    st.session_state.pagina_atual = 'menu'

if st.session_state.pagina_atual == 'menu':
    menu_principal()
elif st.session_state.pagina_atual == 'profissoes':
    pagina_profissoes()
elif st.session_state.pagina_atual == 'transportes':
    pagina_transportes()
elif st.session_state.pagina_atual == 'ferramentas':
    pagina_ferramentas()