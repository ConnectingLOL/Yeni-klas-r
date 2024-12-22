from flask import Flask
import random

app = Flask(__name__)

ilginc_bilgiler = [
    "Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
    "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
    "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
    "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
    "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.",
    "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor."
    ]

yazı_tura = [
    "Yazı"
    "Tura"
]

@app.route("/")
def hello_world():
    return f'<p>Hoş Geldiniz </p><a href="/ilginc-bilgiler">İlginç Bilgiler</a> </p><a href="/yazı-tura">Yazı Tura</a>'

@app.route("/ilginc-bilgiler")
def yakup():
    return f"<p>İlginç Bilgiler: {random.choice(ilginc_bilgiler)}</p>"

@app.route("/yazı-tura")
def berk():
    return f"<p>Atılıyor bozuk para: {random.choice(yazı_tura)}</p>"

app.run(debug=True)
