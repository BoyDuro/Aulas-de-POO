import streamlit as st
import pandas as pd
import time
from service import Service

class TotalAtendimentosUI:
    def main():
        st.header("Total de Atendimentos")
        profissionais = Service.total_atendimentos()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            list_dic = []
            for obj in profissionais: list_dic.append(obj.to_dict())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)