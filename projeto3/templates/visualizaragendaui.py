import streamlit as st
import pandas as pd
from service import Service
from datetime import datetime
import time

class VisualizarAgendaUI:
    def main():
        horarios = Service.profissional_visualizar_agenda(id_profissional=st.session_state)