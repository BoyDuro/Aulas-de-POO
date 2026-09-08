import streamlit as st
import pandas as pd
import time
from service import Service
from datetime import datetime

class ManterAtendimentoUI:
    def main():
        st.header('Cadastro de Atendimentos')
        tab1, tab2, tab3, tab4 = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])
        with tab1: ManterAtendimentoUI.listar()
        with tab2: ManterAtendimentoUI.inserir()
        with tab3: ManterAtendimentoUI.atualizar()
        with tab4: ManterAtendimentoUI.excluir()

    def listar():
        atendimentos = Service.atendiento_listar()
        if len(atendimentos) == 0:
            st.write('Nenhum atendimento cadastrado')
        else:
            dic = []
            for obj in atendimentos:
                horario = Service.horario_listar_id(obj.get_id_horario())
                if horario != None: horario = Service.cliente_listar_id(horario.get_id_cliente)
                dic.append({'id': obj.get_id(), 'data': obj.get_data(), 'confirmado': obj.get_confirmado(), 'cliente': cliente, 'serviço': servico, 'profissional': profissional})
                df = pd.DataFrame(dic)
                st.dataframe(df)

    def inserir():
        clientes = Service.cliente_listar()
        servicos = Service.servico_listar()
        profissionais = Service.profissional_listar()
        data = st.text_input('Informe a data e horário do serviço', datetime.now().strftime('%d/%m/%Y %H:%M'))
        confirmado = st.checkbox('Confirmado')
        cliente = st.selectbox('Informe o cliente', clientes, index = None)
        servico = st.selectbox('Informe o serviço', servicos, index = None)
        profissional = st.selectbox('Informe o profissional', profissionais, index=None)
        if st.button('Inserir'):
            id_cliente = None
            id_servico = None
            id_profissional = None
            if cliente != None: id_cliente = cliente.get_id()
            if servico != None: id_servico = servico.get_id()
            if profissional != None: id_profissional = profissional.get_id()
            Service.horario_inserir(datetime.strptime(data, '%d/%m/%Y %H:%M'), confirmado, id_cliente, id_servico, id_profissional)
            st.success('Horário inserido com sucesso')

    def atualizar():
        horarios = Service.horario_listar()
        if len(horarios) == 0: st.write('Nenhum horário cadastrado')
        else:
            clientes = Service.cliente_listar()
            servicos = Service.servico_listar()
            profissionais = Service.profissional_listar()
            op = st.selectbox('Atualização de Horários', horarios)
            data = st.text_input('Informe a nova data e horário do serviço', op.get_data().strftime('%d/%m/%Y %H:%M'))
            confirmado = st.checkbox('Nova confirmação', op.get_confirmado())
            id_cliente = None if op.get_id_cliente() in [0, None] else op.get_id_cliente()
            id_servico = None if op.get_id_servico() in [0, None] else op.get_id_servico()
            id_profissional = None if op.get_id_profissional() in [0, None] else op.get_id_profissional()
            cliente = st.selectbox('Informe o novo cliente', clientes, next((i for i, c in enumerate(clientes) if c.get_id() == id_cliente), None))
            servico = st.selectbox('Informe o novo serviço', servicos, next((i for i, s in enumerate(servicos) if s.get_id() == id_servico), None))
            profissional = st.selectbox('Informe o novo profissional', profissionais, next((i for i, p in enumerate(profissionais) if p.get_id() == id_profissional), None))
            if st.button('Atualizar'):
                id_cliente = None
                id_servico = None
                id_profissional = None
                if cliente != None: id_cliente = cliente.get_id()
                if servico != None: id_servico = servico.get_id()
                if profissional != None: id_profissional = profissional.get_id()
                Service.horario_atualizar(op.get_id(), datetime.strptime(data, '%d/%m/%Y %H:%M'), confirmado, id_cliente, id_servico, id_profissional)
                st.success('Horário atualizado com sucesso')

    def excluir():
        horarios = Service.horario_listar()
        if len(horarios) == 0: st.write('Nenhum horário cadastrado')
        else:
            op = st.selectbox('Exclusão de Horários', horarios)
            if st.button('Excluir'):
                Service.horario_excluir(op.get_id())
                st.success('Horário excluído com sucesso')
                time.sleep(2)
                st.rerun()