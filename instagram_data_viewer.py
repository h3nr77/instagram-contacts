import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carga los datos desde el archivo CSV
df = pd.read_csv("seguidores.csv")

# Título de la aplicación
st.title("Visualización de Perfiles Seguidos en Instagram")

# Muestra los datos en una tabla
st.subheader("Datos de los Perfiles Seguidos")
st.dataframe(df)

# Conteo de perfiles privados y públicos
status_counts = df["status"].value_counts()

# Muestra el conteo en la aplicación
st.subheader("Conteo de Perfiles Privados y Públicos")
st.write(status_counts)

# Visualiza los resultados en un gráfico de pastel
fig, ax = plt.subplots()
ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', colors=["blue", "orange"])
ax.set_title("Perfiles Privados vs Públicos")

# Muestra el gráfico en Streamlit
st.pyplot(fig)
