# streamlit_app.py

import streamlit as st
import mysql.connector
Profissoes = ["arquiteto","engenheiro","data analyst"]
# Initialize connection.
# Uses st.cache to only run once.

def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from mytable;")




# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")

    with st.form(key = "teste",clear_on_submit = True):
        st.subheader("cadastro novo")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("dados 01")
            imput_name = st.text_input(label="Seu nome pai:", value="Vacilão")
            imput_idade = st.number_input(label='sua idade zé:', min_value=18, max_value=70, step=2)
        with col2:
            st.subheader("dados 02")
            imput_Profissão = st.selectbox(label='Selecione a sua profissão', options= Profissoes)
        imput_botton = st.form_submit_button("enviar dados")

    if imput_botton:
        cursor = conn.cursor()
        nome = "Mariolina"
        valor = "marcolacaa"
        comando = f'INSERT INTO mytable (name,pet) VALUES ("{nome}","{valor}")'
        cursor.execute(comando)
        conn.commit()
        cursor.close()