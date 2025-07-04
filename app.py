import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd

# Configuration de la page
st.set_page_config(
    page_title=" Dashboard Boursier",
    page_icon="💹",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Header stylé
st.markdown(
    """
    <div style="background-color:#0e1117;padding:15px;border-radius:10px">
    <h1 style="color:white;text-align:center;"> Dashboard Boursier Interactif</h1>
    <p style="color:white;text-align:center;">
    Analysez les actions et cryptomonnaies en temps réel 
    </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar
st.sidebar.header("Paramètres")
symbol = st.sidebar.text_input("📈 Entrez le symbole boursier (ex: AAPL, TSLA, BTC-USD):", "AAPL")
start_date = st.sidebar.date_input("📅 Date de début", pd.to_datetime("2022-01-01"))
end_date = st.sidebar.date_input("📅 Date de fin", pd.to_datetime("today"))
ma_period = st.sidebar.slider("📏 Période de la Moyenne Mobile", 5, 100, 20)

# Charger les données
data_load_state = st.text("Chargement des données...")
try:
    df = yf.download(symbol, start=start_date, end=end_date)
    data_load_state.text("✅ Données chargées avec succès !")
except Exception as e:
    st.error(f"Erreur lors du chargement des données : {e}")

if not df.empty:
    # 🖤 Calcul de la moyenne mobile
    df[f"MA{ma_period}"] = df['Close'].rolling(window=ma_period).mean()

    # Créer le graphique interactif
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Prix'))
    fig.add_trace(go.Scatter(x=df.index, y=df[f"MA{ma_period}"], mode='lines', name=f'MA{ma_period}'))
    fig.update_layout(
        title=f"Prix de {symbol} de {start_date} à {end_date}",
        xaxis_title="Date",
        yaxis_title="Prix (USD)",
        template="plotly_dark",
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)

    #  Afficher les données sous forme de tableau
    st.subheader(" Données")
    st.dataframe(df.style.format({"Close": "{:.2f}"}))
else:
    st.warning("Aucune donnée disponible pour ce symbole et cette période.")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align:center;color:gray'>Conçu par FrancoisMansare</div>",
    unsafe_allow_html=True,
)
