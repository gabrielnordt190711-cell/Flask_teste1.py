from flask import Flask
import random

app = Flask(__name__)

facts_list = [
    "Elon Musk também defende a regulamentação das redes sociais e a proteção dos dados pessoais dos usuários. Ele afirma que as redes sociais coletam uma enorme quantidade de informações sobre nós, que podem ser usadas para manipular nossos pensamentos e comportamentos.",

    "Elon Musk afirma que as redes sociais são projetadas para nos manter dentro da plataforma, fazendo com que passemos o máximo de tempo possível consumindo conteúdo.",

    "Uma forma de combater a dependência tecnológica é buscar atividades que tragam prazer e melhorem o humor.",

    "As redes sociais têm pontos positivos e negativos, e devemos estar atentos a ambos ao utilizar essas plataformas.",

    "A maioria das pessoas que sofre de dependência tecnológica sente um forte estresse quando fica fora da área de cobertura de rede ou não pode usar seus dispositivos.",

    "De acordo com um estudo realizado em 2018, mais de 50% das pessoas entre 18 e 34 anos se consideram dependentes de seus smartphones."
]

@app.route("/")
def hello_world():
    fact = random.choice(facts_list)
    return f"""
        <h1>Fato sobre tecnologia</h1>
        <p>{fact}</p>
    """

app.run(debug=True)
