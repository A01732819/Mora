import streamlit as st
import os

try:
    css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "styles.css")
    if not os.path.exists(css_path):
        st.error(f"Error: El archivo CSS no se encuentra en la ruta esperada: {css_path}")
    else:
        with open(css_path, "r", encoding="utf-8") as css_file:
            css_content = css_file.read()
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
except Exception as e:
    st.error(f"Error inesperado al cargar el archivo CSS: {e}")

st.title("Carta para Morita")
st.markdown(":green-badge[:material/star: Bienvenida a tu carta]")
st.divider()

st.markdown("""
**EVELYN morA Ortega** 

Sé que probablemente pienses que esto es algo que haría un ingeniero... y estás en lo correcto.

Yo, tu novio ingeniero en Datos y Matemáticas, una vez pensó que 
era mucho pero mucho texto el que iba a poner aquí, así que simplemente pensó en utilizar sus conocimientos
para describir de una manera extendida y a detalle lo que quiero decir.

¿Pero qué es exactamente lo que quiero decir? En pocas palabras, es dar una buena razón al porqué:
1) Me gustas.
2) Te veo en mi futuro.
3) Eres tú.
4) Quiero estar en tu vida.
5) Amo amarte.

Entre muchas otras cosas, pero, ¿Vas cachando lo que quiero decir? 

Así que bienvenida a tu carta, esta es
""")

st.subheader("La carta")
st.markdown("que he estado preparando :D")


st.divider()

st.image("images/20241101_210832.png", caption="Esta carta también es un viaje por el tiempo.", width=350)

st.markdown("Esta foto es de la primera vez que salimos, el fokin suburbano iba lento y tuve que tomar un uber al Tec. "
            "Fue la primera vez que me subí a un uber tan moderno, y es un recuerdo que vive en mi choya.")

st.divider()

st.markdown("""
No estoy seguro si esto si esto cuenta como una carta, pero lo hago con mucho cariño :D

Ahora que veo que entiendes qué es lo que quiero hacer, quiero platicar de cómo lo voy a hacer.
Vas a ver que hay 3 divisiones en la barra lateral izquierda:
1) **Tempo** va a explicar un poco cómo ha sido mi percepción del tiempo.
2) **Motivos** va a profundizar en la razón por la que escribí la carta. 
3) **Maesthetic** es algo muy cotorro, matemático y aesthetic.

Pero antes de que vayas a pasar a otras páginas, quiero recordarte que te amo.
""")

st.divider()

st.image("images/20241113_214825.png", caption="Una de las tantas lunas que han visto nuestro amor.",width=350)
st.markdown("Esa fue la segunda vez que salimos. Fuimos a ver la película de Flow. "
            "Recuerdo que estaba nervioso porque algo en mí quería acercarse a ti, pero no quería verme raro. "
            "Supe que tu sonrisa se convertitía en algo especial para mí.")

st.divider()

st.markdown("""
Al inicio tuve mis dudas sobre si estaba bien darte esta carta en este formato era lo ideal, pero me di cuenta que quería darte algo muy yo.
Necesito plantarme en tu psique, quiero darte algo tan yo que nunca lo vayas a olvidar. 
Como sabes, la huella digital es el rastro que dejas en internet, y yo quiero dejar registro de que te amo.

"Nunca tendré miedo de amarte ni de sentir tanto por ti, incluso si mañana sucede lo peor."
""")

col1, col2 = st.columns(2)
with col1:
    st.image("images/20241206_162743.png", caption="Este día fue muy lindo.")

with col2:
    st.image("images/20241206_130235.png", caption="Fue la primera vez que pude sentir tu calidez.")

st.divider()

st.markdown("""
Para terminar con esta sección, quiero hacer énfasis en que esta página estará siempre abierta para ti. 

Al igual que yo, siempre disponible para ti: para tus gustos y antojos. 
""")

st.image("images/20241209_141614.png", caption="Foto de nuestro primer beso<33", width=350)

st.divider()


st.markdown("""
Eve:

En algún momento me voy a ir, y eso no significa que te dejaré de amar, porque estás y estarás en mi mente. 
Pero quiero pedirte un favor, si me amas como dices que amas, quiero pedirte un favor.

Cuando regrese, quiero que estés lista para recibir todo el amor que estoy dipuesto a darte. (No exactamente cuando regrese, pero sí si decidimos formalizar).
Aclaro que si no sucede, no te dejaré de amar, pero no sé cómo te manifestaré todo lo que quiero darte.

Quiero amarte sin que fantasmas del pasado nos persigan, ni nada de lo que alguna vez pasó, importe.

Yo estoy dispuesto a hacer todo lo posible para ayudarte en todo lo que me pidas. Lo que te afecta a ti, también me afecta a mí,
y yo quiero que estemos bien, para amarnos bien.
""")

st.image("images/20241226_135757.jpg", caption="No supe cómo voltear la imagen (xd), ¿Ya te dije que te amo?", width=350)

st.markdown("""
Quiero hacer un pequeño disclaimer: Cuando tenga más conocimientos, esta página será otra!!

Sé que no hay mucha consistencia de colores, pero lo que quise fue que cada página tuviera una paleta de colores diferentes, pero que te gusten.
Curiosamente los colores que te gustan, son colores que me recuerdan a ti jajajaja qué locote.

La página está hecha para que la veas desde el celular, pero sin temas la puedes ver en tu compu o en tu tablet.

Yap, puedes seguir leyendo.
""")