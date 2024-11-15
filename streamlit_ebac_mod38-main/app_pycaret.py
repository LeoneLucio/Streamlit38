
# Imports
import pandas            as pd
import streamlit         as st

from io                     import BytesIO
from pycaret.classification import load_model, predict_model
import xlsxwriter


@st.cache
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

# Função para converter o df para excel
@st.cache
def to_excel(df: pd.DataFrame):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.close()
    processed_data = output.getvalue()
    return processed_data


# Função principal da aplicação
def main():
    # Configuração inicial da página da aplicação
    st.set_page_config(page_title = 'PyCaret', \
        layout="wide",
        initial_sidebar_state='expanded'
    )

    # Título principal da aplicação
    st.write("""## Escorando o modelo gerado no pycaret """)
    st.markdown("---")
    
    # Botão para carregar arquivo na aplicação
    st.sidebar.write("## Suba o arquivo")
    data_file_1 = st.sidebar.file_uploader("Bank Credit Dataset", type = ['csv','ftr'])

    # Verifica se há conteúdo carregado na aplicação
    if (data_file_1 is not None):
        df_credit = pd.read_feather(data_file_1)
        df_credit = df_credit.sample(10000)
        st.write(df_credit)

        model_saved = load_model("Documents/Python Scripts/EBAC/Cientista de dados/M38 - Streamlit VI e Pycaret/Final lgbm Model 01Apr2024")
        predict = predict_model(model_saved, data=df_credit)

        df_xlsx = to_excel(predict)
        st.download_button(label='📥 Download',
                            data=df_xlsx ,
                            file_name= 'predict.xlsx')


if __name__ == '__main__':
	main()
    








