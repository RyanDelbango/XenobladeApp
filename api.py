# ./python_code/api.py
import os
import random
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import numpy as np
from Blade import Blade
app = Flask(__name__)
CORS(app)
api = Api(app)
@app.route("/")                 
def BladeList():
    Pyra = Blade("Pyra", "Fire", "https://vignette.wikia.nocookie.net/xenoblade/images/e/ee/Pyra_pic.png/revision/latest/top-crop/width/360/height/360?cb=20170712045817")
    Mythra = Blade("Mythra", "Light", "https://vignette.wikia.nocookie.net/xenoblade/images/5/56/Mythra-portrait.png/revision/latest/scale-to-width-down/350?cb=20171222071213")
    Dromarch = Blade("Dromarch", "Water", "https://vignette.wikia.nocookie.net/xenoblade/images/2/2f/Dromarch-portrait.png/revision/latest/scale-to-width-down/350?cb=20171222183325")
    Nia = Blade("Nia", "Water", "https://vignette.wikia.nocookie.net/xenoblade/images/7/7a/Nia-portrait.png/revision/latest?cb=20171222174412")
    Roc = Blade("Roc", "Wind", "https://vignette.wikia.nocookie.net/xenoblade/images/6/60/Roc_Portrait.png/revision/latest/top-crop/width/360/height/360?cb=20180306215144")
    Poppi = Blade("Poppi", "Earth", "https://vignette.wikia.nocookie.net/xenoblade/images/6/60/Poppi-a-portrait.png/revision/latest?cb=20180306213337")
    Brighid = Blade("Brighid", "Fire", "https://vignette.wikia.nocookie.net/xenoblade/images/6/6d/Brighid_Portrait.png/revision/latest?cb=20180306220141")
    Aegaeon = Blade("Aegaeon", "Water", "https://vignette.wikia.nocookie.net/xenoblade/images/9/9e/Aegaeon_Portrait.png/revision/latest/top-crop/width/360/height/450?cb=20180808075450")
    Pandoria = Blade("Pandoria", "Electric", "https://vignette.wikia.nocookie.net/xenoblade/images/d/df/Pandoria_Portrait.png/revision/latest?cb=20180306215616")
    Godfrey = Blade("Godfrey", "Ice", "https://vignette.wikia.nocookie.net/xenoblade/images/2/2b/Godfrey_Portrait.png/revision/latest/top-crop/width/360/height/450?cb=20180309222845")
    Wulfric = Blade("Wulfric", "Earth", "https://vignette.wikia.nocookie.net/xenoblade/images/0/07/Wulfric_Portrait.png/revision/latest/top-crop/width/360/height/450?cb=20180309215812")
    Perceval = Blade("Perceval", "Dark", "https://vignette.wikia.nocookie.net/xenoblade/images/5/56/Perceval_Portrait.png/revision/latest/top-crop/width/360/height/450?cb=20200424072742")
    Vale = Blade("Vale", "Dark", "https://vignette.wikia.nocookie.net/xenoblade/images/6/6f/Vale_Portrait.png/revision/latest/top-crop/width/360/height/450?cb=20180309214859")
    Agate = Blade("Agate", "Earth", "https://vignette.wikia.nocookie.net/xenoblade/images/9/9c/Agate_Portrait.png/revision/latest/top-crop/width/360/height/450?cb=20200424071925")
    Gorg = Blade("Gorg", "Water", "https://vignette.wikia.nocookie.net/xenoblade/images/c/c9/Gorg_Portrait.png/revision/latest/top-crop/width/360/height/450?cb=20200424072333")
    Boreas = Blade("Boreas", "Wind", "https://vignette.wikia.nocookie.net/xenoblade/images/5/5a/XC2_Boreas_Artwork.png/revision/latest?cb=20190203040018")
    Dagas = Blade("Dagas", "Fire", "https://vignette.wikia.nocookie.net/xenoblade/images/e/ec/Dagas_Portrait.png/revision/latest/top-crop/width/360/height/450?cb=20200424072135")
    Kasandra = Blade("Kasandra", "Dark", "https://vignette.wikia.nocookie.net/xenoblade/images/c/ca/Kasandra_Portrait.png/revision/latest/top-crop/width/360/height/450?cb=20180312215038")
    Praxis = Blade("Praxis", "Water", "https://vignette.wikia.nocookie.net/xenoblade/images/b/bb/Praxis_Portrait.png/revision/latest/top-crop/width/360/height/450?cb=20180312202351")
    Theory = Blade("Theory", "Ice", "https://vignette.wikia.nocookie.net/xenoblade/images/9/95/Theory_Portrait.png/revision/latest/top-crop/width/360/height/450?cb=20200424074139")
    Perun = Blade("Dromarch", "Ice", "https://vignette.wikia.nocookie.net/xenoblade/images/f/fa/Perun_Portrait.png/revision/latest/top-crop/width/360/height/450?cb=20200424074154")
    Kora = Blade("Kora", "Electric", "https://vignette.wikia.nocookie.net/xenoblade/images/7/7a/Kora_Portrait.png/revision/latest/top-crop/width/360/height/450?cb=20200424072527")
    Azami = Blade("Azami", "Dark", "https://vignette.wikia.nocookie.net/xenoblade/images/9/95/Azami_Portrait.png/revision/latest/top-crop/width/360/height/360?cb=20200424071940")
    Ursula = Blade("Ursula", "Ice", "https://vignette.wikia.nocookie.net/xenoblade/images/8/88/XC2_Ursula_Artwork.png/revision/latest/top-crop/width/300/height/300?cb=20190203040101")
    Newt = Blade("Newt", "Fire", "https://vignette.wikia.nocookie.net/xenoblade/images/1/1c/Newt_Portrait.png/revision/latest/top-crop/width/360/height/450?cb=20200424072647")
    Nim = Blade("Nim", "Earth", "https://vignette.wikia.nocookie.net/xenoblade/images/6/6e/Nim_Portrait.png/revision/latest/top-crop/width/360/height/450?cb=20180307230729")
    Sheba = Blade("Sheba", "Water", "https://vignette.wikia.nocookie.net/xenoblade/images/4/4c/Sheba_Portrait.png/revision/latest/top-crop/width/360/height/450?cb=20200424074209")
    Vess = Blade("Vess", "Electric", "https://vignette.wikia.nocookie.net/xenoblade/images/5/56/Vess_Portrait.png/revision/latest/top-crop/width/360/height/450?cb=20180309212408")
    Adenine = Blade("Adenine", "Wind", "https://vignette.wikia.nocookie.net/xenoblade/images/5/5c/Adenine_Portrait.png/revision/latest/top-crop/width/360/height/450?cb=20200424071652")
    Electra = Blade("Electra", "Electric", "https://vignette.wikia.nocookie.net/xenoblade/images/f/f7/Electra_Portrait.png/revision/latest/top-crop/width/360/height/450?cb=20180308123235")
    Zenobia = Blade("Zenobia", "Wind", "https://vignette.wikia.nocookie.net/xenoblade/images/d/da/Zenobia_Portrait.png/revision/latest/top-crop/width/360/height/450?cb=20180309225847")
    Finch = Blade("Finch", "Wind", "https://vignette.wikia.nocookie.net/xenoblade/images/7/7c/Finch_Portrait.png/revision/latest?cb=20180307212952")
    Floren = Blade("Dromarch", "Earth", "https://vignette.wikia.nocookie.net/xenoblade/images/a/af/Floren_Portrait.png/revision/latest/top-crop/width/360/height/450?cb=20180307223618")
    KOSMOS = Blade("KOS-MOS", "Light", "https://vignette.wikia.nocookie.net/xenoblade/images/b/b3/KOS-MOS_Portrait.png/revision/latest/top-crop/width/360/height/450?cb=20200424072541")
    Herald = Blade("Herald", "Electric", "https://vignette.wikia.nocookie.net/xenoblade/images/6/64/Herald_Portrait.png/revision/latest?cb=20180309222150")
    Dahlia = Blade("Dahlia", "Ice", "https://vignette.wikia.nocookie.net/xenoblade/images/a/af/Dahlia_Portrait.png/revision/latest?cb=20180313155424")

    BladeList = [Pyra, Mythra, Dromarch, Nia, Roc, Poppi, Brighid, Aegaeon, Pandoria, Godfrey, Wulfric, Perceval, Vale, Agate, Gorg, Boreas, Dagas, Kasandra, Praxis, Theory, Perun, Kora, Azami, Ursula, Newt, Nim, Sheba, Vess, Adenine, Electra, Zenobia, Finch, Floren, KOSMOS, Herald, Dahlia]
    y = BladeList[random.randint(0,34)]
    return {"Blade": str(y.name), "Picture": str(y.picture)}
if __name__ == "__main__":
    app.run() 
app.run(debug=True)