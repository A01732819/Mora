import streamlit as st
import os

st.set_page_config(page_title="Colección")
st.title("El tiempo y nuestro tiempo")

try:
    css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "styles2.css")
    if not os.path.exists(css_path):
        st.error(f"Error: El archivo CSS no se encuentra en la ruta esperada: {css_path}")
    else:
        with open(css_path, "r", encoding="utf-8") as css_file:
            css_content = css_file.read()
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
except Exception as e:
    st.error(f"Error inesperado al cargar el archivo CSS: {e}")

st.subheader("Porque nada ni nadie nos dice cómo debemos amarnos. ")

st.divider()
st.image("Mora/images/20250103_125111.png", caption="El primer día que pasamos juntos", width=350)

st.markdown("""
Hice un análisis temporal de nuestras citas, las veces que hemos convidido y quiero contarte unas cosas chistosas:

a) ¿Sabías que nuestras 21 y 22 fueron los días 21 y 22 de marzo respectivamente?

b) La primera vez que salimos fue el 1 de noviembre y hasta el 4 de julio han pasado 245 días, que divididos entre las 35 citas que 
hemos tenido, nos da que nos hemos vista una vez cada 7 días. 

c) Te amo mucho. 
""")

st.subheader("Gráfico importante")

st.image("Mora/images/imagen2.png", caption="OJITO con la escala del eje y.", width=796)

show_chart = st.checkbox("Pícale aquí: ")

if show_chart:
    st.image("Mora/images/grafica2.png", width=796)
    st.markdown("Mira, la escala es importante. El primero tiene el eje y logarítmico. Mientras que el segundo tiene el eje y lineal.")

st.subheader("Escalas logarítmicas")

st.markdown("""
La escala logarítmica me permite ver y comparar números grande con números pequeños al mismo tiempo sin perder visualización.
Es decir, en vez de tener pasos de [1, 2, 3] tengo pasos de [10^0, 10^1, 10^2]. 

Esto es muy bueno porque cada día te amo más que ayer, y la suma de todo lo que te amo desde el día 1 que te empecé a amar, es muy grande. Kuchao.

Como fun fact, quiero decir algo que cuando tengo datos exponenciales en una escala logarítmica, estos parecerán una línea recta 
(como ves en el gráfica de arriba). Pero a diferencia de lo que parece en la primera gráfica, lo que siento por ti no ha sido lineal, sino que 
ha pasado por muchas fases, colores. En resumen, te amo. 
""")

st.divider()

st.markdown("""
**¿Y por qué esto es importante?**

Me gusta pensar que desde que nos conocemos, parece que solo estábamos esperando a tener un poco más de confianza para tener algo.
¿No sentiste una conexión desde ese momento en que encontramos la panadería cerrada? 
""")

st.image("Mora/images/20250103_205911.png", caption="La mejor cena que había tenido, y no fue el lugar, fue que dormí contigo después de eso.", width=350)

st.divider()

st.markdown("""
Algo que me parece muy curioso, es que ambos pensábamos que estábamos yendo demasiado rápido (incluso antes de llamarle una relación a este vínculo),
a lo cual yo digo "¿y lo malo?". Si desde el minuto en que nos vimos pensamos que sería algo lindo el ser de nosotros y lo razonamos, no veo porqué
deberíamos pensar que algo va rápido. El tiempo que es, a la hora que es. Y si nosotros vamos así, yo soy muy feliz de esa manera.

Solo queda esperar a que regrese de España y de verdad que nuestro tiempos sigan siendo de verdad nuestros: Me refiero a que
tú y yo estemos cómodos con cómo hemos llevado la relación.
""")

st.image("Mora/images/20250118_130029.png", caption="Tengo recuerdos muy lindos de ti en Tepo.", width=350)

st.markdown("""
Este apartado solo es un recordatorio para ti de que quiero estar en tu vida. 

Quiero vivir sabiendo que soy tuyo, y que no importa qué, me gustaría seguir siendo tuyo.

Estar en tu vida es algo que planeo.
""")
st.image("Mora/images/20250125_130017.png", caption="Es un espectáculo amarte.", width=350)

st.markdown("¿Ya te dije que te amo, evelyn?")


st.image("Mora/images/20250418_191357.png", caption="Quiero seguir formando recuerdos contigo.")