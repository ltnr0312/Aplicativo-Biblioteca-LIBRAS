import streamlit as st

# Definir uma função para a página de profissões
def pagina_profissoes():
    st.header("Profissões")
    # Aqui, você pode inserir o código que já criamos para a seleção e exibição de profissões

# Definir uma função para a página de meios de transporte
def pagina_transportes():
    st.header("Meios de Transporte")
    # Aqui, você pode replicar a estrutura da página de profissões para meios de transporte

# Menu principal com GIFs
def menu_principal():
    st.title("Menu Principal")
    col1, col2 = st.columns(2)
    with col1:
        if st.image("https://www.dropbox.com/scl/fi/assf58nt0wu2gdxi9dq06/Profissoes.gif?rlkey=rfh9arna90sgydpifgxhygnec&st=kewrks8w&raw=1", use_column_width=True, caption="Profissões"):
            st.session_state['pagina_atual'] = 'profissoes'
    with col2:
        if st.image("https://www.dropbox.com/scl/fi/xxxxx/transportes.gif?rlkey=xxxx&raw=1", use_column_width=True, caption="Meios de Transporte"):
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