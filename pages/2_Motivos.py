import streamlit as st
import os

st.set_page_config(page_title="Motivos")
st.title("Te encuentro en todos lados")

try:
    css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "styles3.css")
    if not os.path.exists(css_path):
        st.error(f"Error: El archivo CSS no se encuentra en la ruta esperada: {css_path}")
    else:
        with open(css_path, "r", encoding="utf-8") as css_file:
            css_content = css_file.read()
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
except Exception as e:
    st.error(f"Error inesperado al cargar el archivo CSS: {e}")


st.write("""
Como lo dice el título **Te encuentro en todos lados** y esto no es un chiste barato, lo que es tu esencia, tu personificacicón y 
lo que eres está en muchas partes de mi vida.

Ojo, soy consciente de que soy yo quien te ha atribuido todas estas características y la verdad es que no me arrepiento de nada. Creo que somos nosotros quienes otorgan el peso a lo que sentimos y cómo lo sentimos... 
Y para mí, significas tanto porque he decidido hacerlo. 

Elijo amarte a ti todos los días

""")

st.subheader("Quiero que me entiendaAas")

st.divider()
st.write("En el apartado de motivos voy a exponerte conceptos físico/matemáticos, y cómo se relacionan contigo (cómo yo te encuentro en ellos). "
         "Si bien es cierto que muchas cosas dentro de las matemáticas son muy rectas, en realidad las matemáticas tienen mucha belleza oculta debajo de las fórmulas. "
         "Y lo que es cierto es que tú tienes muchísima belleza que me gusta ver en ti, pero lo más importante es que tú también puedas verla.")

st.divider()
st.header("Sucesión de Fibanocci y el número de Oro")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**Definición:** Secuencia donde cada número es la suma de los dos anteriores:")

    # Fórmula de definición
    st.latex(r"F_0 = 0, \quad F_1 = 1, \quad F_n = F_{n-1} + F_{n-2}")

    st.markdown("**Ejemplo:** 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...")

    st.markdown("**Número de Oro (φ):** Proporción áurea obtenida del límite:")

    # Fórmula del número de oro
    st.latex(r"\lim_{n \to \infty} \frac{F_{n+1}}{F_n} = \varphi = \frac{1+\sqrt{5}}{2} \approx 1.618")

    st.markdown("**Origen:** Creada por Fibonacci en el siglo XIII.")
    st.image("images/20250110_170306.png", caption="La vida siendo tan hermosa como matemática.", width=350)

with col2:
    st.subheader("¿Cómo se relaciona contigo?")

    st.markdown("""
    La sucesión de fibanocci es casi la manera en que te amo. Como lo expliqué en **Tempo**: Te amo la suma de lo que te amé los días anteriores.
    
    Y el número de oro es simplemente increíble y hermoso, e igual que tú, lo encuentro en muchos lados. Un ejemplo es en plantas, como esta pero incluso aparece en las rosas.
    Solo digo que tú eres preciosa, y todo lo bonito que veo en ti, lo veo también en muchos lados gracias a ti.   
    """)
    st.image("images/20250502_185248.png", caption="El número de oro también está en la geometría.")



st.divider()
st.header("Transformada de Fourier")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**Definición:** Descompone una función en suma de senos y cosenos.")

    st.markdown("**Versión continua:**")
    st.latex(r"F(\omega) = \int_{-\infty}^{\infty} f(t)e^{-i\omega t} dt")

    st.markdown("**Versión discreta (DFT):**")
    st.latex(r"X_k = \sum_{n=0}^{N-1} x_n \cdot e^{-2\pi ikn/N}")

    st.markdown("**Origen:** Desarrollada por Joseph Fourier en el siglo XIX para resolver ecuaciones de calor.")
    st.image("images/20250214_133714.png", caption="Hasta lo que parece pequeño, tiene infinito detalle.", width=350)

with col2:
    st.subheader("¿Cómo se relaciona contigo?")
    st.markdown("""
    Así como un microscopio nos permite ver de cerca bacterias, hongos y parásitos, la Transformada de Fourier funciona como un microscopio matemático para señales digitales. Esta herramienta descompone imágenes y audios en sus componentes fundamentales: las ondas que los forman. En imágenes, nos revela dónde están los detalles finos y texturas; en audios, identifica la presencia de graves y agudos. Sus aplicaciones son infinitas.
    
    Personalmente creo que si te aplico una Transformada de Fourier nunca terminaría de encontrarte algo nuevo: Eres tantísimo que cada pequeño de ti es inmenso, siempre hay algo nuevo qué descubrir, "tienes tantas ondas" que su respectivo análisis duraría una eternidad. Pero yo quiero, anhelo, adoraría encontrar hasta el último detalle de lo que eres y lo que te hace ser tú, para así pasar una eternidad junto a ti.
    """)
    st.image("images/20250609_180938.jpg", caption="Agradezco todos los días de poder conocerte más y más.", width=350)

st.divider()

st.header("Representaciones de números")
col1, col2 = st.columns(2)
with col1:

    st.markdown("**Sistemas de numeración:**")
    st.markdown("""
    - **Decimal (base 10):** Usa dígitos 0-9
    - **Binario (base 2):** Solo usa 0 y 1
    - **Hexadecimal (base 16):** Usa 0-9 y A-F (donde A=10, B=11, ..., F=15)
    """)

    st.markdown("**Ejemplo:** El número 13 se representa como:")
    st.latex(r"13_{(decimal)} = 1101_{(binario)} = D_{(hexadecimal)}")

    st.image("images/20250214_143813.png", caption="Siempre hay otras maneras de ver la vida.", width=350)

with col2:
    st.subheader("¿Cómo se relaciona contigo?")
    st.markdown("""
    Evelyn, tú tienes algo (tdah) que hace que siempre un dinamismo en ti tan grande. Me refiero a que hay "facetas" en toda tu personalidad que simplemente es muy lindo de ver.
    Si me preguntas, tú al igual que los números, tiene varias representaciones. Al final del día eres Evelyn, pero con todas las cosas que eres, haces, puedo verte de distintas maneras y no perderás tu esencia. 
    """)
    st.image("images/20250515_160620.png", caption="Una carta de pokemon tiene muchas representaciones, todas son bonitas, pero al final del día, es una carta pokemon. Y tú eres mi favorita.", width=350)

st.divider()
st.header("Entropía")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**Definición:** Mide la incertidumbre o cantidad de información de una fuente:")

    st.latex(r"H(X) = -\sum p(x) \log_2 p(x)")

    st.markdown(
        "**Origen:** Introducida por Clausius en física (termodinámica) y por Claude Shannon en teoría de la información (1948).")
    st.image("images/20250304_181511.png", caption="¿Te imaginaste alguna vez así conmigo?", width=350)
with col2:
    st.subheader("¿Cómo se relaciona contigo?")
    st.markdown("""
    La entropía mide cuán impredecible es algo. Si todo es ordenado, la entropía es baja. Si todo es caótico, es alta. En mensajes, mide cuánta sorpresa hay: si todo es repetido, no hay sorpresa. En las personas...
    
    El hecho de hayan pasado tantas cosas en la relación, y que compartamos esa energía hot, me hace pensar, ¿Será que la entropía fue alta, y por eso somos tan calientes? ¿O la entropía siempre baja, y por eso somos tan calientes?
    
    La primera pregunta dice que fue un producto del azar que tengamos el mismo líbido, mientras que la segunda pregunta indica que ya estaba planeado que íbamos a tener el mismo líbido. Es una pregunta interesante.
    """)
    st.image("Mora/images/20250418_193733.jpg", caption="Neta que me la paso bien padre cuando te tengo cerca.")

st.divider()
st.markdown("Eve, cuando te digo que te encuentro en todo lados, es que hasta en la sopa te veo. Te he aprendido tanto, y no podría estar más feliz por eso.")
st.image("images/20250322_184225.png", caption="Todo es todo.", width=350)

