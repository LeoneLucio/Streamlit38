# Streamlit38

# Credit Scoring para Cartão de Crédito

## Descrição
Projeto de **credit scoring** para prever inadimplência (`mau`) em cartões de crédito, utilizando técnicas de análise exploratória, regressão logística e aprendizado de máquina com PyCaret.

---

## Etapas do Projeto
1. **Pré-Processamento de Dados**: 
   - Exclusão de variáveis irrelevantes (`data_ref`, `index`).
   - Tratamento de valores ausentes e outliers.
   - Transformação de variáveis categóricas e uso de PCA.
2. **Amostragem**:
   - Validação *out of time* (últimos 3 meses).
   - Divisão em treino (70%) e teste (30%).
3. **Análise Exploratória**:
   - **Univariada**: Estatísticas descritivas e gráficos.
   - **Bivariada**: Relações entre variáveis e `mau`.
4. **Desenvolvimento do Modelo**:
   - **Regressão Logística**:
     - Métricas: **Acurácia**, **KS**, **Gini**, **ROC-AUC**.
   - **LightGBM com PyCaret**:
     - Otimização automática com `tune_model()`.
5. **Entrega**:
   - Modelos finais salvos como:
     - `model_final.pkl` (Regressão Logística).
     - `Final_lgbm_Model.pkl` (LightGBM).

---



https://github.com/user-attachments/assets/d44e2b12-8936-4dbf-825a-5a7c35969160

