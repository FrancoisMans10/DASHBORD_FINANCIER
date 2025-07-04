import yfinance as yf
import matplotlib.pyplot as plt 
import streamlit as st 
import pandas as pd 

st.title('Dashboard interactif')

symbol= st.text_input("Entrez le symbole boursier (ex : AAPL, TSLA, BTC-USD)")

start_date = st.date_input("Date de debut ", pd.to_datetime("2024-01-01"))
end_date = st.date_input("Date de fin ", pd.to_datetime("2025-01-01"))

ma_period = st.slider("Moyenne mobile(Jours)",5,50,20)


if st.button("Chargement des donnees"):
    try:
        data= yf.download(symbol,start=start_date,end=end_date)

        if data.empty:
            st.error("Aucune donnée trouvée , verifiez le symbole")
        else:
            st.success(f'Donnees chargees pour {symbol}')
            st.write(data.tail())

            data['MA20'] = data['Close'].rolling(window=ma_period).mean()

            fig,ax = plt.subplots(figsize=(10,5))

            ax.plot(data['Close'],label="Prix de cloture")
            ax.plot(data['MA20'],label =f'Moyenne mobile{ma_period}j',linestyle='--')

            ax.set_title(f'Evolution du prix de {symbol}')
            ax.set_xlabel("Dates")
            ax.set_ylabel("Prix")
            ax.legend()
            st.pyplot(fig)

    except Exception as e :
        st.error(f'Erreur{e}')    

