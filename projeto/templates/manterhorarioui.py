import streamlit as st
import pandas as pd
import time
from service import Service
from datetime import datetime

class ManterHorarioUI:
    def main():
        st.header('Cadastro de Horários')
        tab1, tab2, tab3, tab4 = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])
        with tab1: ManterHorarioUI.listar()
        with tab2: ManterHorarioUI.inserir()
        with tab3: ManterHorarioUI.atualizar()
        with tab4: ManterHorarioUI.excluir()

    def listar():
        horario = Service.horario_listar()
        if len(horario) == 0:
            st.write('Nenhum horário cadastrado')
        else:
            list_dic = []
            for obj in horario:
                list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        dia = st.date_input('Informe a data')
        hora = st.time_input('Informe o horário')
        data = datetime.strptime(f'{hora}, {dia}', "%H%M, %d/%m/%Y")
        if st.button('Inserir'):
            Service.horario_inserir(data)
            st.success('Serviço inserido com sucesso')
            time.sleep(2)
            st.rerun()

    def atualizar():
        horario = Service.horario_listar()
        if len(horario) == 0:
            st.write('Nenhum horário cadastrado')
        else:
            op = st.selectbox('Atualização de serviço', horario)
            dia = st.date_input('Informe a data')
            hora = st.time_input('Informe o horário')
            data = datetime.strptime(f'{hora}, {dia}', "%H%M, %d/%m/%Y")
            if st.button('Atualizar'):
                id = op.get_id()
                Service.horario_atualizar(id, data)
                st.success('Serviço atualizado com sucesso')
    def excluir():
        horario = Service.horario_listar()
        if len(horario) ==0:
            st.write('Nenhum horário cadastrado')
        else:
            op = st.selectbox('Exclusão de serviço', horario)
            if st.button('Excluir'):
                id = op.get_id()
                Service.cliente_excluir(id)
                st.success('Horário excluído com sucesso')