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
    Pyra = Blade("Pyra", "Fire", "https://babd.wincenworks.com/wp-content/uploads/2017/12/tumblr_p1bvw1TF4g1s755fuo4_r1_1280-2.png")
    Mythra = Blade("Mythra", "Light", "https://vignette.wikia.nocookie.net/p__/images/2/2b/Mythra.png/revision/latest?cb=20180517124742&path-prefix=protagonist")
    Dromarch = Blade("Dromarch", "Water", "https://vignette.wikia.nocookie.net/nintendo/images/2/23/Dromarch.png/revision/latest?cb=20171102161655&path-prefix=en")
    Nia = Blade("Nia", "Water", "https://vignette.wikia.nocookie.net/p__/images/0/09/Nia_artwork.png/revision/latest?cb=20180915200716&path-prefix=protagonist")
    Roc = Blade("Roc", "Wind", "https://vignette.wikia.nocookie.net/nintendo/images/d/d7/Xenoblade_Chronicles_2_-_Roc.png/revision/latest?cb=20171110045232&path-prefix=en")
    Poppi = Blade("Poppi", "Earth", "https://vignette.wikia.nocookie.net/p__/images/1/13/XC2-Poppi-Artwork.png/revision/latest?cb=20180915213526&path-prefix=protagonist")
    Brighid = Blade("Brighid", "Fire", "https://vignette.wikia.nocookie.net/nintendo/images/a/ab/Xenoblade_Chronicles_2_-_Brighid.png/revision/latest?cb=20171107173013&path-prefix=en")
    Aegaeon = Blade("Aegaeon", "Water", "https://vignette.wikia.nocookie.net/xenoblade/images/a/a4/XC2_Aegaeon_Artwork.png/revision/latest?cb=20190203040017")
    Pandoria = Blade("Pandoria", "Electric", "https://vignette.wikia.nocookie.net/nintendo/images/7/7b/XC2_Pandoria.png/revision/latest?cb=20171107173057&path-prefix=en")
    Godfrey = Blade("Godfrey", "Ice", "https://vignette.wikia.nocookie.net/nintendo/images/2/21/Xenoblade_Chronicles_2_-_Godfrey.png/revision/latest?cb=20171110170734&path-prefix=en")
    Wulfric = Blade("Wulfric", "Earth", "https://vignette.wikia.nocookie.net/nintendo/images/d/de/Xenoblade_Chronicles_2_-_Wulfric.png/revision/latest?cb=20171110170733&path-prefix=en")
    Perceval = Blade("Perceval", "Dark", "https://vignette.wikia.nocookie.net/xenoblade/images/f/f8/XC2_Perceval_Artwork.png/revision/latest?cb=20190203040052")
    Vale = Blade("Vale", "Dark", "https://vignette.wikia.nocookie.net/nintendo/images/f/fc/Xenoblade_Chronicles_2_-_Vale.png/revision/latest?cb=20171110171313&path-prefix=en")
    Agate = Blade("Agate", "Earth", "https://vignette.wikia.nocookie.net/xenoblade/images/1/1f/XC2_Agate_Artwork.png/revision/latest/top-crop/width/220/height/220?cb=20190203040017")
    Gorg = Blade("Gorg", "Water", "https://vignette.wikia.nocookie.net/xenoblade/images/2/2d/XC2_Gorg_Artwork.png/revision/latest?cb=20190203040029")
    Boreas = Blade("Boreas", "Wind", "https://vignette.wikia.nocookie.net/xenoblade/images/5/5a/XC2_Boreas_Artwork.png/revision/latest?cb=20190203040018")
    Dagas = Blade("Dagas", "Fire", "https://vignette.wikia.nocookie.net/xenoblade/images/5/57/XC2_Dagas_Artwork.png/revision/latest?cb=20190203040019")
    Kasandra = Blade("Kasandra", "Dark", "https://vignette.wikia.nocookie.net/nintendo/images/a/a5/Kasandra_Artwork.png/revision/latest?cb=20181001005314&path-prefix=en")
    Praxis = Blade("Praxis", "Water", "https://vignette.wikia.nocookie.net/xenoblade/images/c/c0/XC2_Praxis_Artwork.png/revision/latest?cb=20190203040053")
    Theory = Blade("Theory", "Ice", "https://vignette.wikia.nocookie.net/xenoblade/images/0/07/XC2_Theory_Artwork.png/revision/latest/top-crop/width/300/height/300?cb=20190203040101")
    Perun = Blade("Perun", "Ice", "https://vignette.wikia.nocookie.net/xenoblade/images/e/eb/XC2_Perun_Artwork.png/revision/latest/top-crop/width/220/height/220?cb=20190203040052")
    Kora = Blade("Kora", "Electric", "https://vignette.wikia.nocookie.net/xenoblade/images/4/4d/XC2_Kora_Artwork.png/revision/latest?cb=20190203040041")
    Azami = Blade("Azami", "Dark", "https://vignette.wikia.nocookie.net/xenoblade/images/0/0c/XC2_Azami_Artwork.png/revision/latest?cb=20190203040018")
    Ursula = Blade("Ursula", "Ice", "https://vignette.wikia.nocookie.net/xenoblade/images/8/88/XC2_Ursula_Artwork.png/revision/latest/top-crop/width/300/height/300?cb=20190203040101")
    Newt = Blade("Newt", "Fire", "https://vignette.wikia.nocookie.net/xenoblade/images/4/44/XC2_Newt_Artwork.png/revision/latest?cb=20190203040042")
    Nim = Blade("Nim", "Earth", "https://vignette.wikia.nocookie.net/xenoblade/images/9/9e/XC2_Nim_Artwork.png/revision/latest?cb=20190203040043")
    Sheba = Blade("Sheba", "Water", "https://vignette.wikia.nocookie.net/xenoblade/images/0/03/XC2_Sheba_Artwork.png/revision/latest?cb=20190203040101")
    Vess = Blade("Vess", "Electric", "https://vignette.wikia.nocookie.net/nintendo/images/9/90/Xenoblade_Chronicles_2_-_Vess.png/revision/latest?cb=20171110172833&path-prefix=en")
    Adenine = Blade("Adenine", "Wind", "https://vignette.wikia.nocookie.net/xenoblade/images/f/f7/XC2_Adenine_Artwork.png/revision/latest?cb=20190203040017")
    Electra = Blade("Electra", "Electric", "https://vignette.wikia.nocookie.net/xenoblade/images/5/59/XC2_Electra_Artwork.png/revision/latest?cb=20190203040028")
    Zenobia = Blade("Zenobia", "Wind", "https://vignette.wikia.nocookie.net/nintendo/images/8/8c/Xenoblade_Chronicles_2_-_Zenobia.png/revision/latest?cb=20171110171128&path-prefix=en")
    Finch = Blade("Finch", "Wind", "https://vignette.wikia.nocookie.net/nintendo/images/6/66/Xenoblade_Chronicles_2_-_Finch.png/revision/latest?cb=20171110045232&path-prefix=en")
    Floren = Blade("Floren", "Earth", "https://vignette.wikia.nocookie.net/xenoblade/images/1/11/XC2_Floren_Artwork.png/revision/latest?cb=20190203040028")
    Herald = Blade("Herald", "Electric", "https://vignette.wikia.nocookie.net/nintendo/images/6/6d/Herald_Artwork.png/revision/latest?cb=20181001194430&path-prefix=en")
    Dahlia = Blade("Dahlia", "Ice", "https://vignette.wikia.nocookie.net/xenoblade/images/9/9e/XC2_Dahlia_Artwork.png/revision/latest?cb=20190203040027")

    BladeList = [Pyra, Mythra, Dromarch, Nia, Roc, Poppi, Brighid, Aegaeon, Pandoria, Godfrey, Wulfric, Perceval, Vale, Agate, Gorg, Boreas, Dagas, Kasandra, Praxis, Theory, Perun, Kora, Azami, Ursula, Newt, Nim, Sheba, Vess, Adenine, Electra, Zenobia, Finch, Floren, Herald, Dahlia]
    y = BladeList[random.randint(0,33)]
    return {"Blade": str(y.name), "Picture": str(y.picture)}
if __name__ == "__main__":
    app.run() 
app.run(debug=True)