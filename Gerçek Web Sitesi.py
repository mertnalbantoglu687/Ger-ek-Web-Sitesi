# main -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import random

from flask import Flask

app = Flask(__name__)

liste = [
    "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
    "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası akıllı telefonlarına bağımlı olduğunu düşünüyor.",
    "Sosyal ağların olumlu ve olumsuz yanları var ve bu platformları kullanırken her ikisinin de farkında olmalıyız.",
    "Teknoloji bağımlılığı çalışması, modern bilimsel araştırmanın en alakalı alanlarından biridir."
]

@app.route("/rastgele_gercek")

def index1():
    return f"<h1> MERHABA! Bu sayfada, teknolojik bağımlılıklar hakkında birkaç ilginç gerçeği öğrenebilirsiniz! </h1>"

@app.route("/rastgele_gercekler")

def facts():
    return f"{random.choice(liste)}"

@app.route("/eglence")

def index2():
    return f"<h2> Bu oyun çoooook güzel: https://hub.kodland.org/en/project/289819 </h2>"

app.run(debug = True)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
