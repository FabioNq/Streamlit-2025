import streamlit as st
import pandas as pd

st.set_page_config(page_title='Finanças', page_icon=":moneybag:")

st.markdown("""
            
# Boas Vindas!
            
# Nosso App Financeiro!
            

Espero que você curta a experiência da nossa solução para organização financeira.           

""")


# Widget de upload dos dados
file_upload = st.file_uploader(label="Faça upload dos dados aqui",type=['csv'])

# Verifica se algumm arquivo foi feito upload
if file_upload:

    #Leitura dos dados
    df = pd.read_csv(file_upload)
    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y").dt.date
    
    #Exibir os dados no app
    exp1 = st.expander("Dados Brutos")
    columns_fmt ={"Valor":st.column_config.NumberColumn("Valor", format="R$%d")}
    exp1.dataframe(df,hide_index=1, column_config=columns_fmt)

    #Visão Instituição
    exp2 = st.expander("Dados pivot")
    df_instituicao = df.pivot_table(index="Data", columns="Instituição",values='Valor')

    #Abas para diferentes visualizações
    tab_data,tab_history,tab_share = exp2.tabs(["Dados","Historico","Distribuição"])

    # Exibe Dataframe
    with tab_data:
        st.dataframe(df_instituicao)

    # Exibe Histórico 
    with tab_history:
        st.line_chart(df_instituicao)

    # Exibe Dashboard
    with tab_share:

            # Exibe Filtro de Data
            date = st.selectbox("Filtro Data",options=df_instituicao.index)
            
            # Gráfico de Distribuição
            st.bar_chart(df_instituicao.loc[date])

#Não tem Arquivo