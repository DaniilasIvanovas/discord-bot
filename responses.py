import random
opener = "Once upon a time Tomas Plank said:"
tomas_sake = [
    "visa tai, kaip sakoma, nice",
    "na cia toks… lyrinis nukrypimas",
    "kai iškviesit funkciją ir galvosit 'what the fuck is going on' neišsigąskit",
    "tikrai kaip sakant.. no problem",
    "šiandien daug navarotų. Va aš turiu navarotą",
    "sako, šiandien navarotų diena",
    '*nusičiaudi* "prisiuosčiau kreidos. Gerai, kad tik kreidos"',
    "na jus jau tikrai nemažai žinote",
    "bs ten ne bullshit, ten build square",
    "čia tame ir yra bajeris",
    "bet kaip sakoma, who cares???",
    "infarktas nutrenkė windowsus",
    "ir tada iškils klausimas, kaip toj dainoj “ką daryt”, o programuotojų darbas bus “pašokt”",
    "šiandien čia gerokai erorrŲ pamėtė",
    "bloga darosi nuo blogų",
    "neišgėręs nesuprasi..",
    "pavyzdžiui paleisti kokį “jesus christ” metas keltis…. su kokiu 60 decibelų, kad kaimynai pabustų",
    "biski relaxo reik?"
] # 17

sekasi = ['normaliai sian', 'blogai...', 'gerai, o tau?', 'tiesiog super']
tomai = ['ka?', 'taip?', 'klausau', 'idemiai', 'ko nori?', 'kas yra?']
pasisiveikink = ['sveikas', 'gera diena', 'labas', 'hey']


def handle_response(msg) -> str:
    p_msg = msg.lower()

    if p_msg == 'kaip sekasi?' or p_msg == 'kaip sekasi':
        return sekasi[random.randint(0, len(sekasi))]

    if p_msg == 'labas':
        return pasisiveikink[random.randint(0, len(pasisiveikink))]

    if p_msg == 'alio':
        return 'negirdziu taves'

    if p_msg == '!help':
        return 'Ne'

    if p_msg == 'tomai':
        return tomai[random.randint(0, len(tomai))]

    if p_msg == 'kaip laikaisi?' or p_msg == 'kaip laikais':
        return 'As nesilaikau'

    if p_msg == 'ismintis' or p_msg == 'ismintis?':
        return opener + '\n' + f'"{tomas_sake[random.randint(0, len(tomas_sake))]}"'
