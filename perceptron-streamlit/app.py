import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("🧠 Perceptrón Interactivo")

# -------------------------
# SLIDERS
# -------------------------

w1 = st.slider("Peso w1", -10.0, 10.0, 1.0)

w2 = st.slider("Peso w2", -10.0, 10.0, 1.0)

bias = st.slider("Sesgo (bias)", -10.0, 10.0, 0.0)

# -------------------------
# ETIQUETAS
# -------------------------

st.subheader("🎯 Etiquetas deseadas")

y00 = st.selectbox("(0,0)", [0,1], key="a")

y01 = st.selectbox("(0,1)", [0,1], key="b")

y10 = st.selectbox("(1,0)", [0,1], key="c")

y11 = st.selectbox("(1,1)", [0,1], key="d")

# -------------------------
# DATOS
# -------------------------

datos = [
    [0,0,y00],
    [0,1,y01],
    [1,0,y10],
    [1,1,y11]
]

resultados = []

correctos = 0

# -------------------------
# PERCEPTRON
# -------------------------

for x1, x2, esperado in datos:

    z = (x1 * w1) + (x2 * w2) + bias

    salida = 1 if z >= 0 else 0

    correcto = salida == esperado

    if correcto:
        correctos += 1

    resultados.append({
        "x1": x1,
        "x2": x2,
        "Esperado": esperado,
        "Suma": round(z,2),
        "Salida": salida,
        "Correcto": "✅" if correcto else "❌"
    })

# -------------------------
# TABLA
# -------------------------

df = pd.DataFrame(resultados)

st.subheader("📋 Resultados")

st.dataframe(df)

# -------------------------
# CONTADOR
# -------------------------

st.metric("Patrones Correctos", f"{correctos}/4")

if correctos == 4:
    st.success("🎉 ¡Clasificación perfecta!")

# -------------------------
# GRAFICA
# -------------------------

st.subheader("📈 Frontera de Decisión")

fig, ax = plt.subplots()

# Dibujar puntos
for x1, x2, esperado in datos:

    color = "green" if esperado == 1 else "red"

    ax.scatter(x1, x2, color=color, s=200)

    ax.text(x1 + 0.03, x2 + 0.03, f"({x1},{x2})")

# Dibujar frontera
x = np.linspace(-1, 2, 100)

if w2 != 0:

    y = -(w1 * x + bias) / w2

    ax.plot(x, y)

# Configuración
ax.set_xlim(-0.5, 1.5)

ax.set_ylim(-0.5, 1.5)

ax.set_xlabel("x1")

ax.set_ylabel("x2")

ax.grid(True)

st.pyplot(fig)

# -------------------------
# FORMULA
# -------------------------

st.subheader("🧮 Fórmula")

st.latex(r"z = w_1x_1 + w_2x_2 + b")