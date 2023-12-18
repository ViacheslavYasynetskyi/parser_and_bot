cities_dict = {
    "cherepovets": "@rabota_cherepovets0",
    "orel": "@orel_rabota0",
    "tula": "@tula_vakansii1",
    "arhangelsk": "@vakansii_podrabotka13",
    "vologda": "@vologda_vakansii0",
    "kurgan": "@vakansii_podrabotka7",
    "smolensk": "@vakansii_podrabotka14",
    "volgogradskaya_oblast_volzhskiy": "@rabota_volzhskiy1",
    "podolsk": "@rabota_podrabotka14",
    "moskva": "@rabota_msk_moskva0",
    "chita": "@rabota_chita0",
    "groznyy": "@rabota_groznyyq",
    "kaluga": "@rabota2_podrabotka",
    "nizhniy_tagil": "@rabota_podrabotka88",
    "belgorod": "@vakansii_podrabotka89",
    "vladimir": "@vakansii_podrabotka90",
    "bryansk": "@vakansii_podrabotka23",
    "yakutsk": "@rabota_podrabotka87",
    "ivanovo": "@rabota_podrabotka86",
    "novosibirsk": "@vakansiiqa",
    "sankt-peterburg": "@vakansii_spb_piter",
    "ekaterinburg": "@ekb_vakansii0",
    "ulan-ude": "@vakansii_podrabotka17",
    "kursk": "@vakansii_podrabotka18",
    "kirovskaya_oblast_kirov": "@vakansii_podrabotka19",
    "surgut": "@rabota_podrabotka27",
    "sochi": "@rabotad_v_vakansiiq_podrabotkahw",
    "anapa": "@vakansiij_anapa",
    "magnitogorsk": "@rabota_podrabotka28",
    "simferopol": "@podrabotka_simferopole",
    "tver": "@vakansii_tver",
    "krasnoyarsk": "@podrabotkaq_vakansiiq",
    "astrahan": "@vakansii_podrabotka20",
    "chelyabinsk": "@vakansii_podrabotka25",
    "kazan": "@kazan_vakansii0",
    "nizhniy_novgorod": "@vakansii_podrabotka24",
    "lipetsk": "@vakansii0_podrabotka",
    "cheboksary": "@vakansii1_podrabotka",
    "penza": "@penza_vakansii0",
    "balashiha": "@vakansii_balashikha0",
    "ryazan": "@vakansii_v_ryazani",
    "novokuznetsk": "@vakansii_podrabotka26",
    "samara": "@samara_vakansii0",
    "ufa": "@Ufa_vakansii_podrabotka",
    "sevastopol": "@podrabotka_v_sevastopole0",
    "stavropol": "@stavropole_v_vakansii",
    "kemerovo": "@vakansii_podrabotka30",
    "naberezhnye_chelny": "@vakansii_podrabotka28",
    "tomsk": "@vakansii_podrabotka29",
    "yaroslavl": "@yaroslavl_vakansii0",
    "vladivostok": "@vakansii_podrabotka31",
    "irkutsk": "@vakansii_podrabotka32",
    "perm": "@vakansii1_podrabotka_v",
    "saratov": "@vakansii3_podrabotka_v",
    "volgograd": "@vakansii1_podrabotka_v1",
    "voronezh": "@vakansii1_podrabotka_v2",
    "tyumen": "@podrabotka_v_tyumeni1",
    "tolyatti": "@podrabotka_v2",
    "barnaul": "@podrabotka_v_Barnaule1",
    "izhevsk": "@podrabotka_v_izhevske",
    "mahachkala": "@podrabotka_v_makhachkale",
    "habarovsk": "@podrabotka_v_Khabarovske",
    "ulyanovsk": "@podrabotka_v_Ulyanovske1",
    "vladikavkaz": "@podrabotka_na_Vladikavkaze1",
    "nizhnevartovsk": "@podrabotka_v_nizhnevartovske",
    "yoshkar-ola": "@vakansii0_podrabotka_ole",
    "sterlitamak": "@podrabotka_v_Sterlitamake1",
    "murmansk": "@podrabotka_v_murmanske1",
    "kostroma": "@podrabotka_v_Kostrome1",
    "krasnodar": "@vakansii1_podrabotka2",
    "rostov-na-donu": "@vakansii_podrabotka_rabota0",
    "nizhnekamsk": "@vakansiiq_podrabotkaw",
    "petrozavodsk": "@vakansiiw_podrabotkaw",
    "komsomolsk-na-amure": "@rabota_v_vakansii",
    "korolev": "@vakansiiw_podrabotkae",
    "shahty": "@vakansiie_podrabotkae",
    "engels": "@vakansiie_podrabotkar",
    "velikiy_novgorod": "@vakansiir_podrabotkar",
    "lyubertsy": "@vakansiir_podrabotkat",
    "bratsk": "@vakansiit_podrabotkat",
    "staryy_oskol": "@vakansiit_podrabotkay",
    "angarsk": "@vakansiiy_podrabotkay",
    "syktyvkar": "@vakansiiy_podrabotkau",
    "dzerzhinsk": "@vakansiiu_podrabotkau",
    "pskov": "@vakansiiu_podrabotkai",
    "orsk": "@vakansiii_podrabotkai",
    "moskovskaya_oblast_krasnogorsk": "@vakansiii_podrabotkao",
    "balakovo": "@vakansiia_podrabotkap",
    "biysk": "@vakansiip_podrabotkap",
    "yuzhno-sahalinsk": "@vakansii_podrabotkap",
    "odintsovo": "@vakansiia_podrabotkas",
    "ussuriysk": "@vakansiis_podrabotkas",
    "prokopevsk": "@vakansiis_podrabotkad",
    "rybinsk": "@vakansiid_podrabotkad",
    "norilsk": "@vakansiid_podrabotkaf",
    "volgodonsk": "@vakansiif_podrabotkaf",
    "syzran": "@vakansiif_podrabotkag",
    "petropavlovsk-kamchatskiy": "@vakansiig_podrabotkag",
    "kamensk-uralskiy": "@vakansiig_podrabotkah",
    "novocherkassk": "@vakansiih_podrabotkah",
    "almetevsk": "@vakansiih_podrabotkaj",
    "zlatoust": "@vakansiij_podrabotkaj",
    "severodvinsk": "@vakansiij_podrabotkak",
    "hasavyurt": "@vakansiik_podrabotkak",
    "kerch": "@vakansiik_podrabotkal",
    "domodedovo": "@vakansiil_podrabotkal",
    "salavat": "@vakansiil_podrabotkaz",
    "miass": "@vakansiiz_podrabotkaz",
    "kopeysk": "@vakansiiz_podrabotkax",
    "pyatigorsk": "@vakansii_podrabotkax",
    "elektrostal": "@vakansii_podrabotkaz",
    "maykop": "@vakansii_podrabotkal",
    "nahodka": "@vakansii_podrabotkah",
    "berezniki": "@vakansii_podrabotkad",
    "kolomna": "@vakansii_podrabotkas",
    "schelkovo": "@vakansii_podrabotkao",
    "serpuhov": "@vakansii_podrabotkai",
    "kovrov": "@vakansii_podrabotkat",
    "neftekamsk": "@vakansii_podrabotkar",
    "kislovodsk": "@vakansiiq_podrabotka",
    "bataysk": "@vakansiie_podrabotka",
    "rubtsovsk": "@vakansiir_podrabotka",
    "obninsk": "@vakansiit_podrabotka",
    "kyzyl": "@vakansiiy_podrabotka",
    "derbent": "@vakansiiu_podrabotka",
    "nefteyugansk": "@vakansiio_podrabotka",
    "nazran": "@vakansiip_podrabotka",
    "kaspiysk": "@vakansiia_podrabotka",
    "dolgoprudnyy": "@vakansiis_podrabotka",
    "novocheboksarsk": "@vakansiid_podrabotka",
    "novomoskovsk": "@vakansiif_podrabotka",
    "essentuki": "@vakansiig_podrabotka",
    "nevinnomyssk": "@vakansiih_podrabotka",
    "ramenskoe": "@vakansiiz_podrabotka",
    "pervouralsk": "@vakansiix_podrabotka",
    "novorossiysk": "@vakansii_podrabotka35",
    "tambov": "@vakansii_podrabotka36",
    "himki": "@vakansii_podrabotka37",
    "mytischi": "@vakansii_podrabotka38",
    "nalchik": "@vakansii_podrabotka39",
    "taganrog": "@vakansii_podrabotka40",
    "hanty-mansiysk": "@vakansiim_podrabotkai",
    "murom": "@vakansiim_podrabotkau",
    "evpatoriya": "@vakansiim_podrabotkay",
    "kamyshin": "@vakansiim_podrabotkat",
    "artem": "@vakansiim_podrabotkar",
    "pushkino": "@vakansiim_podrabotkae",
    "dimitrovgrad": "@vakansiim_podrabotkaw",
    "zhukovskiy": "@vakansiim_podrabotkaq",
    "cherkessk": "@vakansiim_podrabotka",
    "reutov": "@vakansiin_podrabotka",
    "kaliningrad": "@vakansii_podrabotka21",
    "novyy_urengoy": "@vakansiim_podrabotkao_vq",
    "seversk": "@vakansiim_podrabotkao",
    "orehovo-zuevo": "@vakansiim_podrabotkap",
    "arzamas": "@vakansiim_podrabotkaa",
    "noginsk": "@vakansiim_podrabotkas",
    "novoshahtinsk": "@vakansiim_podrabotkad",
    "berdsk": "@vakansiim_podrabotkaf",
    "elista": "@vakansiim_podrabotkag",
    "sergiev_posad": "@vakansiim_podrabotkah",
    "vidnoe": "@vakansiim_podrabotkaj_vq",
    "achinsk": "@vakansiim_podrabotkaj",
    "tobolsk": "@vakansiim_podrabotkak",
    "noyabrsk": "@vakansiim_podrabotkal",
    "elets": "@vakansiim_podrabotkaz",
    "zelenodolsk": "@vakansiim_podrabotkax",
    "novokuybyshevsk": "@vakansiim_podrabotkac",
    "votkinsk": "@vakansiim_podrabotkav",
    "voskresensk": "@vakansiim_podrabotkam",
    "gatchina": "@vakansiin_podrabotkam",
    "serov": "@vakansiin_podrabotkan",
    "orenburg": "@vakansiifg_podrabotkagr"}

a = {"kaliningrad": "@vakansii_podrabotka21",
     "orenburg": "@vakansii_podrabotka27",
     "komsomolsk_na_amure": "@rabota_v_vakansii",
     "saransk": "@rabota_podrabotka10",
     "oktyabrsky": "@vakansiik_podrabotka",
     "mikhaylovsk": "@vakansiib_podrabotka",
     "komsomolsk-na-amure": "@rabota_v_vakansii",
     "zheleznogorsk": "@vakansiim_podrabotkab",
     "mezhdurechensk": "@vakansiim_podrabotkan"}
