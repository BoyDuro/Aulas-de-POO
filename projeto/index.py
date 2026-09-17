from templates.manterclienteui import ManterClienteUI
from templates.manterservicoui import ManterServicoUI
from templates.manterhorarioui import ManterHorarioUI
from templates.manterprofissionalui import ManterProfissionalUI
from templates.manteratendimentoui import ManterAtendimentoUI
from templates.abrircontaui import AbrirContaUI
from templates.loginui import LoginUI
from templates.perfilclienteui import PerfilClienteUI
from templates.perfilprofissional import PerfilProfissionalUI
from service import Service
import streamlit as st

class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox('Menu', ['Entrar no Sistema', 'Abrir Conta'])
        if op == 'Entrar no Sistema': LoginUI.main()
        if op == 'Abrir Conta': AbrirContaUI.main()
    def menu_cliente():
        op = st.sidebar.selectbox('Menu', ['Meus Dados'])
        if op == 'Meus Dados': PerfilClienteUI.main()
    def menu_profissional():
        op = st.sidebar.selectbox('Menu', ['Meus Dados'])
        if op == 'Meus Dados': PerfilProfissionalUI.main()
    def menu_admin():
        op = st.sidebar.selectbox('Menu', ['Clientes', 'Serviços', 'Horários', 'Profissionais', 'Atendimentos', 'Convenios'])
        if op == 'Clientes':
            ManterClienteUI.main()
        if op == 'Serviços':
            ManterServicoUI.main()
        if op == 'Horários':
            ManterHorarioUI.main()
        if op == 'Profissionais':
            ManterProfissionalUI.main()
        if op == 'Atendimentos':
            ManterAtendimentoUI.main()
    def sair_do_sistema():
        if st.sidebar.button('Sair'):
            del st.session_state['usuario_id']
            del st.session_state['usuario_nome']
            st.rerun()
    def sidebar():
        if 'usuario_id' not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state['usuario_nome'] == 'admin'
            clientes = Service.cliente_listar()
            profissionais = Service.profissional_listar()
            for obj in clientes:
                cliente = st.session_state['usuario_nome'] == obj.get_nome()
                if cliente: break
            for obj in profissionais:
                profissional = st.session_state['usuario_nome'] == obj.get_nome()
                if profissional: break
            st.sidebar.write('Bem-vindo(a), ' + st.session_state['usuario_nome'])
            if admin: IndexUI.menu_admin()
            elif cliente: IndexUI.menu_cliente()
            elif profissional: IndexUI.menu_profissional()
            
            IndexUI.sair_do_sistema()
    def main():
        # verifica a existe o usuário admin
        Service.cliente_criar_admin()
        # monta o sidebar
        IndexUI.sidebar()

IndexUI.main()