import streamlit as st
from datetime import datetime
from paciente import Paciente

class PacienteUI:
    def main():
        st.header('Dados de paciente')
        nome = st.text_input('Digite o nome:')
        cpf = st.text_input('Digite o CPF:')
        fone = st.text_input('Digite o fone:')
        nasc = st.text_input('Digite a data de nascimento:')
        if st.button('Idade'):
            x = Paciente(nome, cpf, fone, datetime.strptime(nasc, '%d/%m/%Y'))
            st.write(x.idade())
            st.write(f'nome: {x.get_nome()} - CPF: {x.get_cpf()} - fone: {x.get_fone()}')