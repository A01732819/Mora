import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
# import streamlit.components.v1 as components
# import base64 # Necesitamos esta librería para mostrar el GIF

try:
    css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "styles4.css")
    if not os.path.exists(css_path):
        st.error(f"Error: El archivo CSS no se encuentra en la ruta esperada: {css_path}")
    else:
        with open(css_path, "r", encoding="utf-8") as css_file:
            css_content = css_file.read()
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
except Exception as e:
    st.error(f"Error inesperado al cargar el archivo CSS: {e}")

st.title("Corazones para mi corazón")
st.write("""
Hola, vi unos corazones y pensé que como tú eres mi corazón, quería que te vieras como te veo.
""")

# --- SECCIÓN 1: ANIMACIÓN CON COORDENADAS POLARES ---
st.header("1. Corazón en Coordenadas Polares")
st.latex(r"r(\theta) = 2 - 2\sin\theta + \frac{\sin\theta\sqrt{|\cos\theta|}}{\sin\theta + 1.4}")

# Usamos un string multilínea para mostrar el código de forma limpia
codigo_animacion = """
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configurar el estilo del gráfico
plt.style.use('dark_background')
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.tick_params(colors='lightgray', grid_color='gray')
ax.spines['polar'].set_color('lightgray')

# Preparar los datos para la curva
theta = np.linspace(0, 2 * np.pi, 1000)
r = (2 - 2 * np.sin(theta) + 
     np.sin(theta) * np.sqrt(np.abs(np.cos(theta))) / (np.sin(theta) + 1.4))

# Fijar los límites para que quepa toda la figura
ax.set_rlim(0, np.max(r) * 1.1) 
ax.set_yticklabels([])

# Configurar la línea que se va a animar
line, = ax.plot([], [], color='#E45D5D', lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    line.set_data(theta[:i], r[:i])
    return line,

# Crear la animación
ani = FuncAnimation(fig, animate, frames=len(theta), init_func=init, 
                    interval=10, blit=True)

# Convertir la animación a un formato compatible con HTML5
# En lugar de plt.show()
html_video = ani.to_html5_video()
"""

st.code(codigo_animacion, language='python')

# Botón para ejecutar el código de la animación
if st.button("Generar Animación Polar"):
    with st.spinner("Creando animación... esto puede tardar unos segundos."):
        # Aquí se ejecuta el código real cuando se presiona el botón

        plt.style.use('dark_background')
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')
        ax.tick_params(colors='lightgray', grid_color='gray')
        ax.spines['polar'].set_color('lightgray')

        theta = np.linspace(0, 2 * np.pi, 1000)
        r = (2 - 2 * np.sin(theta) +
             np.sin(theta) * np.sqrt(np.abs(np.cos(theta))) / (np.sin(theta) + 1.4))

        ax.set_rlim(0, np.max(r) * 1.1)
        ax.set_yticklabels([])

        line, = ax.plot([], [], color='#E45D5D', lw=2)


        def init():
            line.set_data([], [])
            return line,


        def animate(i):
            # Animamos un poco más rápido para que el GIF no sea tan pesado
            step = 10
            line.set_data(theta[:i * step], r[:i * step])
            return line,


        # Creamos la animación con menos fotogramas para que el GIF sea más ligero
        ani = FuncAnimation(fig, animate, frames=len(theta) // 10, init_func=init, interval=50, blit=True)

        # --- CAMBIO PRINCIPAL AQUÍ ---
        # 1. Guardar la animación como un archivo GIF
        gif_path = "heart_animation.gif"
        ani.save(gif_path, writer='pillow', fps=20)

        # 2. Mostrar el GIF en Streamlit
        st.image(gif_path)

        plt.close(fig)  # Liberar memoria

st.markdown("---")

# --- SECCIÓN 2: GRÁFICO CON ECUACIÓN IMPLÍCITA ---
st.header("2. Otro corazao")
st.latex(r"(x^2 + y^2 - 1)^3 - x^2y^3 = 0")

codigo_implicito = """
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1.5, 1.5, 500)
y = np.linspace(-1.5, 1.5, 500)
X, Y = np.meshgrid(x, y)

equation = (X**2 + Y**2 - 1)**3 - X**2 * Y**3

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.contour(X, Y, equation, levels=[0], colors=['#E45D5D'])

ax.set_title("Heart Curve (Implicit)")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True, linestyle='--', alpha=0.6)
"""
st.code(codigo_implicito, language='python')

if st.button("Generar Gráfico Implícito"):
    # Ejecutamos el código para el gráfico
    x = np.linspace(-1.5, 1.5, 500)
    y = np.linspace(-1.5, 1.5, 500)
    X, Y = np.meshgrid(x, y)
    equation = (X ** 2 + Y ** 2 - 1) ** 3 - X ** 2 * Y ** 3

    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.contour(X, Y, equation, levels=[0], colors=['#E45D5D'])
    ax.set_title("Heart Curve (Implicit)", fontsize=16, family='serif', color='#E48A8A')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True, linestyle='--', alpha=0.6)

    # Usamos st.pyplot() para mostrar la figura de matplotlib
    st.pyplot(fig)

st.markdown("---")

# --- SECCIÓN 3: GRÁFICO CON ECUACIÓN EXPLÍCITA ---
st.header("3. ¿Apoco no se ve padre?")
st.latex(r"x^2 + \left(y - \frac{2(x^2+|x|-6)}{3(x^2+|x|+2)}\right)^2 = 16")

codigo_explicito = """
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 1000)

term = (2 * (x**2 + np.abs(x) - 6)) / (3 * (x**2 + np.abs(x) + 2))
sqrt_term = np.sqrt(np.maximum(0, 16 - x**2))

y1 = term + sqrt_term
y2 = term - sqrt_term

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')

ax.plot(x, y1, color='#E45D5D')
ax.plot(x, y2, color='#E45D5D')
ax.set_title("Heart Curve (Explicit)")
"""
st.code(codigo_explicito, language='python')

if st.button("Generar Gráfico Explícito"):
    # Ejecutamos el código
    x = np.linspace(-4, 4, 1000)
    term = (2 * (x ** 2 + np.abs(x) - 6)) / (3 * (x ** 2 + np.abs(x) + 2))
    sqrt_term = np.sqrt(np.maximum(0, 16 - x ** 2))
    y1 = term + sqrt_term
    y2 = term - sqrt_term

    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.plot(x, y1, color='#E45D5D')
    ax.plot(x, y2, color='#E45D5D')
    ax.set_title("Heart Curve (Explicit)", fontsize=16, family='serif', color='#E48A8A')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True, linestyle='--', alpha=0.6)

    st.pyplot(fig)

st.divider()

st.subheader("Solo recuerda que te amo")

st.markdown("""
Esta parte solo quería andar de cotorro porque aprendí a hacer animaciones (aunque solo puse una) en python, pero antes de 
que termines de leer, quiero que recuerdes el objetivo de la carta:

**Te recuerdo que te amo**

Creo que con eso podría rematar aquí, todo lo que te quise decir, lo dije ya. Pero es que el sentimiento no se puede solo plasmar en una frase.
Y creo que no hay palabra, frase, libro, idioma, acción o plan que me permitan representarte lo tanto que te amo. Neta.

Creo que el color rojo, es uno que fácilmente te podría representar
""")

st.image("Mora/images/20250523_180607.png", caption="Amo amarte, Evelyn Mora Ortega, dame tu apellidoOoo", width=350)
st.divider()
st.image("Mora/images/20250620_154045.png", caption="Con cariño, Popel")
