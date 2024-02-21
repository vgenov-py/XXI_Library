import sqlite3
from flask import g, current_app
from uuid import uuid4
import datetime as dt
from functools import reduce
import msgspec
from typing import Optional
import re
from multiprocessing import Process
from os import system
from secrets import token_hex

countries = {
    '': '', 'aa': 'Albania', 'abc': 'Alberta', 'ac': 'Islas Ashmore y Cartier', 'aca': 'Territorio de la Capital Australiana', 'ae': 'Argelia', 'af': 'Afganistán', 'ag': 'Argentina', 'ai': 'Armenia (República)', 'air': 'RSS de Armenia', 'aj': 'Azerbaiyán', 'ajr': 'RSS de Azerbaiyán', 'aku': 'Alaska', 'alu': 'Alabama', 'am': 'Anguila', 'an': 'Andorra', 'ao': 'Angola', 'aq': 'Antigua y Barbuda', 'aru': 'Arkansas', 'as': 'Samoa Americana', 'at': 'Australia', 'au': 'Austria', 'aw': 'Aruba', 'ay': 'Antártida', 'azu': 'Arizona', 'ba': 'Baréin', 'bb': 'Barbados', 'bcc': 'Columbia Británica', 'bd': 'Burundi', 'be': 'Bélgica', 'bf': 'Bahamas', 'bg': 'Bangladés', 'bh': 'Belice', 'bi': 'Territorio Británico del Océano Índico', 'bl': 'Brasil', 'bm': 'Islas Bermudas', 'bn': 'Bosnia y Herzegovina', 'bo': 'Bolivia', 'bp': 'Islas Salomón', 'br': 'Birmania', 'bs': 'Botsuana', 'bt': 'Bután', 'bu': 'Bulgaria', 'bv': 'Isla Bouvet', 'bw': 'Bielorrusia', 'bwr': 'RSS de Bielorrusia', 'bx': 'Brunéi', 'ca': 'Países Bajos Caribeños', 'cau': 'California', 'cb': 'Camboya', 'cc': 'China', 'cd': 'Chad', 'ce': 'Sri Lanka', 'cf': 'Congo (Brazzaville)', 'cg': 'Congo (República Democrática)', 'ch': 'China (República: 1949- )', 'ci': 'Croacia', 'cj': 'Islas Caimán', 'ck': 'Colombia', 'cl': 'Chile', 'cm': 'Camerún', 'cn': 'Canadá', 'co': 'Curazao', 'cou': 'Colorado', 'cp': 'Islas de Cantón y Enderbury', 'cq': 'Comoras', 'cr': 'Costa Rica', 'cs': 'Checoslovaquia', 'ctu': 'Connecticut', 'cu': 'Cuba', 'cv': 'Cabo Verde', 'cw': 'Islas Cook', 'cx': 'República Centroafricana', 'cy': 'Chipre', 'cz': 'Zona del Canal', 'dcu': 'Distrito de Columbia', 'deu': 'Delaware', 'dk': 'Dinamarca', 'dm': 'Benín', 'dq': 'Dominica', 'dr': 'República Dominicana', 'ea': 'Eritrea', 'ec': 'Ecuador', 'eg': 'Guinea Ecuatorial', 'em': 'Timor Oriental', 'enk': 'Inglaterra', 'er': 'Estonia', 'err': 'Estonia', 'es': 'El Salvador', 'et': 'Etiopía', 'fa': 'Islas Feroe', 'fg': 'Guayana Francesa', 'fi': 'Finlandia', 'fj': 'Fiyi', 'fk': 'Islas Malvinas', 'flu': 'Florida', 'fm': 'Estados Federados de Micronesia', 'fp': 'Polinesia Francesa', 'fr': 'Francia', 'fs': 'Tierras Australes y Antárticas Francesas', 'ft': 'Yibuti', 'gau': 'Georgia', 'gb': 'Kiribati', 'gd': 'Granada', 'ge': 'Alemania Oriental', 'gg': 'Guernsey', 'gh': 'Ghana', 'gi': 'Gibraltar', 'gl': 'Groenlandia', 'gm': 'Gambia', 'gn': 'Islas Gilbert y Ellice', 'go': 'Gabón', 'gp': 'Guadalupe', 'gr': 'Grecia', 'gs': 'Georgia (República)', 'gsr': 'RSS de Georgia', 'gt': 'Guatemala', 'gu': 'Guam', 'gv': 'Guinea', 'gw': 'Alemania', 'gy': 'Guyana', 'gz': 'Franja de Gaza', 'hiu': 'Hawái', 'hk': 'Hong Kong', 'hm': 'Islas Heard y McDonald', 'ho': 'Honduras', 'ht': 'Haití', 'hu': 'Hungría', 'iau': 'Iowa', 'ic': 'Islandia', 'idu': 'Idaho', 'ie': 'Irlanda', 'ii': 'India', 'ilu': 'Illinois', 'im': 'Isla de Man', 'inu': 'Indiana', 'io': 'Indonesia', 'iq': 'Irak', 'ir': 'Irán', 'is': 'Israel', 'it': 'Italia', 'iu': 'Zonas Desmilitarizadas de Israel y Siria', 'iv': 'Costa de Marfil', 'iw': 'Zonas Desmilitarizadas de Israel y Jordania', 'iy': 'Zona Neutral de Irak y Arabia Saudita', 'ja': 'Japón', 'je': 'Jersey', 'ji': 'Atolón Johnston', 'jm': 'Jamaica', 'jn': 'Jan Mayen', 'jo': 'Jordania', 'ke': 'Kenia', 'kg': 'Kirguistán', 'kgr': 'RSS de Kirguistán', 'kn': 'Corea del Norte', 'ko': 'Corea del Sur', 'ksu': 'Kansas', 'ku': 'Kuwait', 'kv': 'Kosovo', 'kyu': 'Kentucky', 'kz': 'Kazajistán', 'kzr': 'RSS de Kazajistán', 'lau': 'Luisiana', 'lb': 'Liberia', 'le': 'Líbano', 'lh': 'Liechtenstein', 'li': 'Lituania', 'lir': 'Lituania', 'ln': 'Islas del Sur y Central', 'lo': 'Lesoto', 'ls': 'Laos', 'lu': 'Luxemburgo', 'lv': 'Letonia', 'lvr': 'Letonia', 'ly': 'Libia', 'mau': 'Massachusetts', 'mbc': 'Manitoba', 'mc': 'Mónaco', 'mdu': 'Maryland', 'meu': 'Maine', 'mf': 'Mauricio', 'mg': 'Madagascar', 'mh': 'Macao', 'miu': 'Míchigan', 'mj': 'Montserrat', 'mk': 'Omán', 'ml': 'Malí', 'mm': 'Malta', 'mnu': 'Minnesota', 'mo': 'Montenegro', 'mou': 'Misuri', 'mp': 'Mongolia', 'mq': 'Martinica', 'mr': 'Marruecos', 'msu': 'Misisipi', 'mtu': 'Montana', 'mu': 'Mauritania', 'mv': 'Moldavia', 'mvr': 'RSS de Moldavia', 'mw': 'Malaui', 'mx': 'México', 'my': 'Malasia', 'mz': 'Mozambique', 'na': 'Antillas Neerlandesas', 'nbu': 'Nebraska', 'ncu': 'Carolina del Norte', 'ndu': 'Dakota del Norte', 'ne': 'Países Bajos', 'nfc': 'Terranova y Labrador', 'ng': 'Níger', 'nhu': 'Nuevo Hampshire', 'nik': 'Irlanda del Norte', 'nju': 'Nueva Jersey', 'nkc': 'Nuevo Brunswick', 'nl': 'Nueva Caledonia', 'nm': 'Islas Marianas del Norte', 'nmu': 'Nuevo México', 'nn': 'Vanuatu', 'no': 'Noruega', 'np': 'Nepal', 'nq': 'Nicaragua', 'nr': 'Nigeria', 'nsc': 'Nueva Escocia', 'ntc': 'Territorios del Noroeste', 'nu': 'Nauru', 'nuc': 'Nunavut', 'nvu': 'Nevada', 'nw': 'Islas Marianas del Norte', 'nx': 'Isla Norfolk', 'nyu': 'Estado de Nueva York', 'nz': 'Nueva Zelanda', 'ohu': 'Ohio', 'oku': 'Oklahoma', 'onc': 'Ontario', 'oru': 'Oregón', 'ot': 'Mayotte', 'pau': 'Pensilvania', 'pc': 'Isla Pitcairn', 'pe': 'Perú', 'pf': 'Islas Paracel', 'pg': 'Guinea-Bisáu', 'ph': 'Filipinas', 'pic': 'Isla del Príncipe Eduardo', 'pk': 'Pakistán', 'pl': 'Polonia', 'pn': 'Panamá', 'po': 'Portugal', 'pp': 'Papúa Nueva Guinea', 'pr': 'Puerto Rico', 'pt': 'Timor Portugués', 'pw': 'Palaos', 'py': 'Paraguay', 'qa': 'Catar', 'qea': 'Queensland', 'quc': 'Quebec (Provincia)', 'rb': 'Serbia', 're': 'Reunión', 'rh': 'Zimbabue', 'riu': 'Rhode Island', 'rm': 'Rumania', 'ru': 'Federación Rusa', 'rur': 'RSS de la URSS', 'rw': 'Ruanda', 'ry': 'Islas Ryukyu, Sur', 'sa': 'Sudáfrica', 'sb': 'Svalbard', 'sc': 'San Bartolomé', 'scu': 'Carolina del Sur', 'sd': 'Sudán del Sur', 'sdu': 'Dakota del Sur', 'se': 'Seychelles', 'sf': 'Santo Tomé y Príncipe', 'sg': 'Senegal', 'sh': 'África del Norte Española', 'si': 'Singapur', 'sj': 'Sudán', 'sk': 'Sikkim', 'sl': 'Sierra Leona', 'sm': 'San Marino', 'sn': 'Sint Maarten', 'snc': 'Saskatchewan', 'so': 'Somalia', 'sp': 'España', 'sq': 'Esuatini', 'sr': 'Surinam', 'ss': 'Sáhara Occidental', 'st': 'San Martín', 'stk': 'Escocia', 'su': 'Arabia Saudita', 'sv': 'Islas Swan', 'sw': 'Suecia', 'sx': 'Namibia', 'sy': 'Siria', 'sz': 'Suiza', 'ta': 'Tayikistán', 'tar': 'RSS de Tayikistán', 'tc': 'Islas Turcas y Caicos', 'tg': 'Togo', 'th': 'Tailandia', 'ti': 'Túnez', 'tk': 'Turkmenistán', 'tkr': 'RSS de Turkmenistán', 'tl': 'Tokelau', 'tma': 'Tasmania', 'tnu': 'Tennessee', 'to': 'Tonga', 'tr': 'Trinidad y Tobago', 'ts': 'Emiratos Árabes Unidos', 'tt': 'Territorio en Fideicomiso de las Islas del Pacífico', 'tu': 'Turquía', 'tv': 'Tuvalu', 'txu': 'Texas', 'tz': 'Tanzania', 'ua': 'Egipto', 'uc': 'Islas del Caribe de Estados Unidos', 'ug': 'Uganda', 'ui': 'Islas Varias del Reino Unido', 'uik': 'Islas Varias del Reino Unido', 'uk': 'Reino Unido', 'un': 'Ucrania', 'unr': 'Ucrania', 'up': 'Islas Varias del Pacífico de Estados Unidos', 'ur': 'Unión Soviética', 'us': 'Estados Unidos', 'utu': 'Utah', 'uv': 'Burkina Faso', 'uy': 'Uruguay', 'uz': 'Uzbekistán', 'uzr': 'RSS de Uzbekistán', 'vau': 'Virginia.', 'vb': 'Islas Vírgenes Británicas', 'vc': 'Ciudad del Vaticano', 've': 'Venezuela', 'vi': 'Islas Vírgenes de los Estados Unidos', 'vm': 'Vietnam', 'vn': 'Vietnam del Norte', 'vp': 'Varios lugares', 'vra': 'Victoria', 'vs': 'Vietnam del Sur', 'vtu': 'Vermont', 'wau': 'Estado de Washington', 'wb': 'Berlín Oeste', 'wea': 'Australia Occidental', 'wf': 'Wallis y Futuna', 'wiu': 'Wisconsin', 'wj': 'Margen Occidental del Río Jordán', 'wk': 'Isla Wake', 'wlk': 'Gales', 'ws': 'Samoa', 'wvu': 'Virginia Occidental', 'wyu': 'Wyoming', 'xa': 'Isla de Navidad (Océano Índico)', 'xb': 'Islas Cocos (Keeling)', 'xc': 'Maldivas', 'xd': 'San Cristóbal y Nieves', 'xe': 'Islas Marshall', 'xf': 'Islas Midway', 'xga': 'Territorio de las Islas del Mar del Coral', 'xh': 'Niue', 'xi': 'San Cristóbal y Nieves-Anguila', 'xj': 'Santa Elena', 'xk': 'Santa Lucía', 'xl': 'San Pedro y Miquelón', 'xm': 'San Vicente y las Granadinas', 'xn': 'Macedonia del Norte', 'xna': 'Nueva Gales del Sur', 'xo': 'Eslovaquia', 'xoa': 'Territorio del Norte', 'xp': 'Isla Spratly', 'xr': 'República Checa', 'xra': 'Australia Meridional', 'xs': 'Islas Georgias del Sur y Sandwich del Sur', 'xv': 'Eslovenia', 'xx': 'Sin lugar, desconocido o indeterminado', 'xxc': 'Canadá', 'xxk': 'Islas varias del Reino Unido', 'xxr': 'Unión Soviética', 'xxu': 'Estados Unidos', 'ye': 'Yemen', 'ykc': 'Territorio de Yukón', 'ys': 'Yemen (República Democrática Popular)', 'yu': 'Serbia y Montenegro', 'za': 'Zambia'}        
languages = {
    '': '', 'aar': 'Afar', 'abk': 'abjasio', 'ace': 'achinés', 'ach': 'acoli', 'ada': 'adangme', 'ady': 'adigué', 'afa': 'afroasiático (otros)', 'afh': 'afrihili (lengua artificial)', 'afr': 'afrikáans', 'ain': 'ainu', 'ajm': 'aljamía', 'aka': 'akan', 'akk': 'acadio', 'alb': 'albanés', 'ale': 'aleutiano', 'alg': 'algonquino (otros)', 'alt': 'altai', 'amh': 'amárico', 'ang': 'inglés antiguo (ca. 450-1100)', 'anp': 'angika', 'apa': 'lenguas apache', 'ara': 'árabe', 'arc': 'arameo', 'arg': 'aragonés', 'arm': 'armenio', 'arn': 'mapuche', 'arp': 'arapaho', 'art': 'artificial (otros)', 'arw': 'arahuaco', 'asm': 'asamés', 'ast': 'bable', 'ath': 'atapascos (otros)', 'aus': 'lenguas australianas', 'ava': 'ávaro', 'ave': 'avéstico', 'awa': 'awadhi', 'aym': 'aimara', 'aze': 'azerí', 'bad': 'lenguas banda', 'bai': 'lenguas bamileke', 'bak': 'bashkir', 'bal': 'baluchi', 'bam': 'bambara', 'ban': 'balinés', 'baq': 'vasco', 'bas': 'basa', 'bat': 'báltico (otros)', 'bej': 'beja', 'bel': 'bielorruso', 'bem': 'bemba', 'ben': 'bengalí', 'ber': 'bereber (otros)', 'bho': 'bhojpuri', 'bih': 'bihari (otros)', 'bik': 'bikol', 'bin': 'edo', 'bis': 'bislama', 'bla': 'siksika', 'bnt': 'bantú (otros)', 'bos': 'bosnio', 'bra': 'braj', 'bre': 'bretón', 'btk': 'batak', 'bua': 'buriat', 'bug': 'bugis', 'bul': 'búlgaro', 'bur': 'birmano', 'byn': 'bilin', 'cad': 'caddo', 'cai': 'indio centroamericano (otros)', 'cam': 'jemer', 'car': 'caribe', 'cat': 'catalán', 'cau': 'caucásico (otros)', 'ceb': 'cebuano', 'cel': 'céltico (otros)', 'cha': 'chamorro', 'chb': 'chibcha', 'che': 'checheno', 'chg': 'chagatai', 'chi': 'chino', 'chk': 'chuukés', 'chm': 'mari', 'chn': 'jerga chinook', 'cho': 'choctaw', 'chp': 'chipewyan', 'chr': 'cheroqui', 'chu': 'eslavo eclesiástico', 'chv': 'chuvasio', 'chy': 'cheyenne', 'cmc': 'lenguas cham', 'cnr': 'montenegrino', 'cop': 'copto', 'cor': 'córnico', 'cos': 'corso', 'cpe': 'criollos y pidgins basados en el inglés (otros)', 'cpf': 'criollos y pidgins basados en el francés (otros)', 'cpp': 'criollos y pidgins basados en el portugués (otros)', 'cre': 'cree', 'crh': 'tártaro de Crimea', 'crp': 'criollos y pidgins (otros)', 'csb': 'casubio', 'cus': 'cushita (otros)', 'cze': 'checo', 'dak': 'dakota', 'dan': 'danés', 'dar': 'dargwa', 'day': 'dayak', 'del': 'delaware', 'den': 'slavey', 'dgr': 'dogrib', 'din': 'dinka', 'div': 'divehi', 'doi': 'dogri', 'dra': 'dravidiano (otros)', 'dsb': 'sorbio inferior', 'dua': 'duala', 'dum': 'neerlandés medio (ca. 1050-1350)', 'dut': 'neerlandés', 'dyu': 'dyula', 'dzo': 'dzongkha', 'efi': 'efik', 'egy': 'egipcio', 'eka': 'ekajuk', 'elx': 'elamita', 'eng': 'inglés', 'enm': 'inglés medio (1100-1500)', 'epo': 'esperanto', 'esk': 'lenguas esquimales', 'esp': 'esperanto', 'est': 'estonio', 'eth': 'etiópico', 'ewe': 'ewe', 'ewo': 'ewondo', 'fan': 'fang', 'fao': 'feroés', 'far': 'feroés', 'fat': 'fanti', 'fij': 'fiyiano', 'fil': 'filipino', 'fin': 'finlandés', 'fiu': 'fino-ugrio (otros)', 'fon': 'fon', 'fre': 'francés', 'fri': 'frisón', 'frm': 'francés medio (ca. 1300-1600)', 'fro': 'francés antiguo (ca. 842-1300)', 'frr': 'frisón septentrional', 'frs': 'frisón oriental', 'fry': 'frisón', 'ful': 'fula', 'fur': 'friulano', 'gaa': 'gã', 'gae': 'gaélico escocés', 'gag': 'gallego', 'gal': 'oromo', 'gay': 'gayo', 'gba': 'gbaya', 'gem': 'germánico (otros)', 'geo': 'georgiano', 'ger': 'alemán', 'gez': 'etiópico', 'gil': 'gilbertés', 'gla': 'gaélico escocés', 'gle': 'irlandés', 'glg': 'gallego', 'glv': 'manés', 'gmh': 'alemán medio alto (ca. 1050-1500)', 'goh': 'alemán antiguo alto (ca. 750-1050)', 'gon': 'gondi', 'gor': 'gorontalo', 'got': 'gótico', 'grb': 'grebo', 'grc': 'griego antiguo (hasta 1453)', 'gre': 'griego moderno (1453-)', 'grn': 'guaraní', 'gsw': 'alemán suizo', 'gua': 'guaraní', 'guj': 'guyaratí', 'gwi': "gwich'in", 'hai': 'haida', 'hat': 'criollo francés haitiano', 'hau': 'hausa', 'haw': 'hawaiano', 'heb': 'hebreo', 'her': 'herero', 'hil': 'hiligaynon', 'him': 'lenguas pahari occidentales', 'hin': 'hindi', 'hit': 'hitita', 'hmn': 'hmong', 'hmo': 'hiri motu', 'hrv': 'croata', 'hsb': 'alto sorbio', 'hun': 'húngaro', 'hup': 'hupa', 'iba': 'iban', 'ibo': 'igbo', 'ice': 'islandés', 'ido': 'ido', 'iii': 'yi de sichuán', 'ijo': 'ijo', 'iku': 'inuktitut', 'ile': 'interlingue', 'ilo': 'ilocano', 'ina': 'interlingua (Asociación de la Lengua Auxiliar Internacional)', 'inc': 'índico (otros)', 'ind': 'indonesio', 'ine': 'indoeuropeo (otros)', 'inh': 'ingush', 'int': 'interlingua (Asociación Lingüística Internacional Auxiliar)', 'ipk': 'inupiaq', 'ira': 'iraní (otros)', 'iri': 'irlandés', 'iro': 'iroquiano (otros)', 'ita': 'italiano', 'jav': 'javanés', 'jbo': 'lojban (lengua artificial)', 'jpn': 'japonés', 'jpr': 'judeo-persa', 'jrb': 'judeo-árabe', 'kaa': 'karakalpako', 'kab': 'cabila', 'kac': 'kachin', 'kal': 'kalaallisut', 'kam': 'kamba', 'kan': 'kannada', 'kar': 'lenguas karen', 'kas': 'cachemiro', 'kau': 'kanuri', 'kaw': 'kawi', 'kaz': 'kazajo', 'kbd': 'cabardiano', 'kha': 'khasi', 'khi': 'khoisan (otros)', 'khm': 'jemer', 'kho': 'hotanés', 'kik': 'kikuyu', 'kin': 'kinyarwanda', 'kir': 'kirguís', 'kmb': 'kimbundu', 'kok': 'konkani', 'kom': 'komi', 'kon': 'kongo', 'kor': 'coreano', 'kos': 'kosraeano', 'kpe': 'kpelle', 'krc': 'karachay-bálcaro', 'krl': 'carelio', 'kro': 'kru (otros)', 'kru': 'kurukh', 'kua': 'kuanyama', 'kum': 'kumyk', 'kur': 'kurdo', 'kus': 'kusaie', 'kut': 'kootenai', 'lad': 'ladino', 'lah': 'lahndā', 'lam': 'lamba (Zambia y Congo)', 'lan': 'occitano (después de 1500)', 'lao': 'lao', 'lap': 'sami', 'lat': 'latín', 'lav': 'letón', 'lez': 'lezgiano', 'lim': 'limburgués', 'lin': 'lingala', 'lit': 'lituano', 'lol': 'mongo-nkundu', 'loz': 'lozi', 'ltz': 'luxemburgués', 'lua': 'luba-lulua', 'lub': 'luba-katanga', 'lug': 'ganda', 'lui': 'luiseño', 'lun': 'lunda', 'luo': 'luo (Kenia y Tanzania)', 'lus': 'lushai', 'mac': 'macedonio', 'mad': 'madurés', 'mag': 'magahi', 'mah': 'marshalés', 'mai': 'maithili', 'mak': 'makasar', 'mal': 'malayalam', 'man': 'mandingo', 'mao': 'maorí', 'map': 'austronesio (otros)', 'mar': 'marathi', 'mas': 'masái', 'max': 'manés', 'may': 'malayo', 'mdf': 'moksha', 'mdr': 'mandar', 'men': 'mende', 'mga': 'irlandés medio (ca. 1100-1550)', 'mic': 'micmac', 'min': 'minangkabau', 'mis': 'lenguas varias', 'mkh': 'mon-jemer (otros)', 'mla': 'malgache', 'mlg': 'malgache', 'mlt': 'maltés', 'mnc': 'manchú', 'mni': 'manipuri', 'mno': 'lenguas manobo', 'moh': 'mohawk', 'mol': 'moldavo', 'mon': 'mongol', 'mos': 'mooré', 'mul': 'varios idiomas', 'mun': 'munda (otros)', 'mus': 'creek', 'mwl': 'mirandés', 'mwr': 'marwari', 'myn': 'lenguas mayas', 'myv': 'erzya', 'nah': 'náhuatl', 'nai': 'indio norteamericano (otros)', 'nap': 'italiano napolitano', 'nau': 'nauruano', 'nav': 'navajo', 'nbl': 'ndebele (Sudáfrica)', 'nde': 'ndebele (Zimbabue)', 'ndo': 'ndonga', 'nds': 'bajo alemán', 'nep': 'nepalí', 'new': 'newari', 'nia': 'nias', 'nic': 'nigerocongo (otros)', 'niu': 'niueano', 'nno': 'noruego (nynorsk)', 'nob': 'noruego (bokmål)', 'nog': 'nogai', 'non': 'nórdico antiguo', 'nor': 'noruego', 'nqo': "n'ko", 'nso': 'sotho septentrional', 'nub': 'nilo-sahariano (otros)', 'nwc': 'newari antiguo', 'nya': 'nyanya', 'nym': 'nyamwesi', 'nyn': 'nyankole', 'nyo': 'nyoro', 'nzi': 'nzima', 'oci': 'occitano (después de 1500)', 'oji': 'ojibwa', 'ori': 'oriya', 'orm': 'oromo', 'osa': 'osage', 'oss': 'osetio', 'ota': 'turco otomano', 'oto': 'lenguas otomí', 'paa': 'papú (otros)', 'pag': 'pangasinán', 'pal': 'pahleví', 'pam': 'pampanga', 'pan': 'punjabi', 'pap': 'papiamento', 'pau': 'palauano', 'peo': 'persa antiguo (ca. 600-400 a.C.)', 'per': 'persa', 'phi': 'filipino (otros)', 'phn': 'fenicio', 'pli': 'pali', 'pol': 'polaco', 'pon': 'pohnpeiano', 'por': 'portugués', 'pra': 'prácrito', 'pro': 'provenzal (hasta 1500)', 'pus': 'pashto', 'que': 'quechua', 'raj': 'rajasthani', 'rap': 'rapanui', 'rar': 'rarotongano', 'roa': 'romance (otros)', 'roh': 'rético-romance', 'rom': 'romaní', 'rum': 'rumano', 'run': 'rundi', 'rup': 'aromaniano', 'rus': 'ruso', 'sad': 'sandawe', 'sag': 'sango (ubangiense criollo)', 'sah': 'yakuto', 'sai': 'indio sudamericano (otros)', 'sal': 'lenguas salish', 'sam': 'arameo samaritano', 'san': 'sánscrito', 'sao': 'samoano', 'sas': 'sasak', 'sat': 'santalí', 'scc': 'serbio', 'scn': 'siciliano italiano', 'sco': 'escocés', 'scr': 'croata', 'sel': 'selkup', 'sem': 'semítico (otros)', 'sga': 'irlandés antiguo (hasta 1100)', 'sgn': 'lenguas de signos', 'shn': 'shan', 'sho': 'shona', 'sid': 'sidamo', 'sin': 'cingalés', 'sio': 'siouan (otros)', 'sit': 'sino-tibetano (otros)', 'sla': 'eslavo (otros)', 'slo': 'eslovaco', 'slv': 'esloveno', 'sma': 'sami meridional', 'sme': 'sami septentrional', 'smi': 'sami', 'smj': 'sami lule', 'smn': 'sami inari', 'smo': 'samoano', 'sms': 'sami skolt', 'sna': 'shona', 'snd': 'sindhi', 'snh': 'cingalés', 'snk': 'soninké', 'sog': 'sogdiano', 'som': 'somalí', 'son': 'songhay', 'sot': 'sotho', 'spa': 'español', 'srd': 'sardo', 'srn': 'sranan', 'srp': 'serbio', 'srr': 'serer', 'ssa': 'nilosahariano (otros)', 'sso': 'sotho', 'ssw': 'suazi', 'suk': 'sukuma', 'sun': 'sundanés', 'sus': 'susu', 'sux': 'sumerio', 'swa': 'suajili', 'swe': 'sueco', 'swz': 'suazi', 'syc': 'siríaco', 'syr': 'siríaco moderno', 'tag': 'tagalo', 'tah': 'tahitiano', 'tai': 'tai (otros)', 'taj': 'tayiko', 'tam': 'tamil', 'tar': 'tártaro', 'tat': 'tártaro', 'tel': 'telugu', 'tem': 'temne', 'ter': 'terena', 'tet': 'tetum', 'tgk': 'tayiko', 'tgl': 'tagalo', 'tha': 'tailandés', 'tib': 'tibetano', 'tig': 'tigre', 'tir': 'tigriña', 'tiv': 'tiv', 'tkl': 'tokelauano', 'tlh': 'klingon (lengua artificial)', 'tli': 'tlingit', 'tmh': 'támazight', 'tog': 'tonga (Nyasa)', 'ton': 'tongano', 'tpi': 'tok pisin', 'tru': 'chuukés', 'tsi': 'tsimshiano', 'tsn': 'tswana', 'tso': 'tsonga', 'tsw': 'tswana', 'tuk': 'turcomano', 'tum': 'tumbuka', 'tup': 'lenguas tupi', 'tur': 'turco', 'tut': 'altaico (otros)', 'tvl': 'tuvaluano', 'twi': 'twi', 'tyv': 'tuviniano', 'udm': 'udmurto', 'uga': 'ugarítico', 'uig': 'uigur', 'ukr': 'ucraniano', 'umb': 'umbundu', 'und': 'indeterminado', 'urd': 'urdu', 'uzb': 'uzbeko', 'vai': 'vai', 'ven': 'venda', 'vie': 'vietnamita', 'vol': 'volapük', 'vot': 'votic', 'wak': 'lenguas wakash', 'wal': 'wolaytta', 'war': 'waray', 'was': 'washo', 'wel': 'galés', 'wen': 'sorbio (otro)', 'wln': 'walloon', 'wol': 'wolof', 'xal': 'oirat', 'xho': 'xhosa', 'yao': 'yao (África)', 'yap': 'yapés', 'yid': 'yiddish', 'yor': 'yoruba', 'ypk': 'lenguas yupik', 'zap': 'zapotec', 'zbl': 'símbolos Bliss', 'zen': 'zenaga', 'zha': 'zhuang', 'znd': 'lenguas zándicas', 'zul': 'zulú', 'zun': 'zuñi', 'zxx': 'Sin contenido:Optional[str] =Noneal', 'zza': 'Zazaki'}

structs = {}

class QMO:
    def __init__(self,dataset:str,  args:dict=None):
        self.dataset = dataset
        self.args = args

    @staticmethod
    def get_db(file:str=None):
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(current_app.config.get("DB_FILE") if not file else file)
        return db

    @property
    def con(self, file:str=None):
        return self.get_db(file)
    
    @property
    def cur(self):
        return self.con.cursor()
    
    @property
    def available_fields(self) -> list:
        '''
        Todos los campos disponibles del dataset (marc21 + humans)
        '''
        return [row[1] for row in self.cur.execute(f"pragma table_info({self.dataset});")]
                
    @property
    def marc_fields(self) -> str:
        '''
        Todos los campos marc21 del dataset 
        '''
        return [field[1] for field in self.cur.execute(f"pragma table_info({self.dataset});") if field[1].startswith("t_")]

    @property
    def human_fields(self) -> str:
        '''
        Todos los campos humans del dataset
        '''
        return [field[1] for field in self.cur.execute(f"pragma table_info({self.dataset});") if not field[1].startswith("t_")]

    def create_struct(self,fields:list):
        '''
        struct generado por el dataset con el que se esté trabajando en definitiva es la conversión dict -> JSON (Object de JS)
        '''
        to_execute = f'''class {self.dataset.capitalize()}(msgspec.Struct, omit_defaults=True):\n    '''
        for field in fields:
            to_execute += f"{field}: Optional[str] = None\n    "
        exec(to_execute)
        exec(f"structs['{self.dataset}'] = {self.dataset.capitalize()}")     
    
    @property
    def datasets(self):
        '''
        Todos los datasets disponibles en la aplicación
        '''
        return list(map(lambda name:name[0],filter(lambda name: len(name[0]) == 3, self.cur.execute("select name from sqlite_master where type='table';"))))
    
    @property
    def all_fields(self):
        '''
        Método utilizado por la ruta /api/schema para generar los esquemas de cada conjunto
        '''
        '''
        all fields of all tables
        {
            dataset1_human: [],
            dataset1_marc: [],
            dataset1_all: []
            dataset2...
        }
        '''
        result = {}
        for  dataset in self.datasets:
            self.dataset = dataset
            result[dataset] = self.available_fields
        return result

    @property
    def purgue(self) -> dict:
        '''
        Método que limpia y maneja el mal uso de la aplicación por parte del cliente
        '''
        result = {}
        error = {"success": False}
        args = self.args.copy()

        dataset_2 = [{dataset:args.pop(dataset)} for dataset in self.datasets if dataset in args.keys()] # Ésto es utilizado cuando el usuario hace una joining query entre por ejemplo, per y mon
        fields = args.pop("fields", None) # Los campos que quiere ver el cliente, ejemplo fields=id,nombre_de_persona
        limit = args.pop("limit", "1000") # El usuario no puede especificar límite, pero si es que se quiere aumentar por parte del desarrollador, se puede hacer desde aquí
        order_by = args.pop("order_by", None) # SQL ORDER BY (asc default, desc optional)
        view = args.pop("view", False) # Campos a mostrar, por defecto todos, y sino view=marc o view=human
        result["is_from_web"] = args.pop("is_from_web", False) # Si la consulta fue generada desde las rutas de web (cajitas - wikidata style) o en formato RESTful API
        filters = args.items() # Todos los filtros del usuario, ejemplo nombre_de_persona=Vito Genovese

        if limit:
            try:
                int(limit)
            except ValueError:
                error["message"] = f"limit debe ser un número entero"
                return error
        result["limit"] = limit

        if order_by:
            order_key = order_by.split(",")[0]
            if order_key not in self.available_fields: # Es necesario verificar si el usuario está filtrando por un campo existente
                result["message"] = f"No se puede ordenar por {order_key} en {self.dataset}"
                return error
            try:
                order_direction:str = order_by.split(",")[1].strip()
                if order_direction not in ("asc", "desc"):
                    error["message"] = f"Orden ascendente: asc - Orden descendente: desc"
                    return error
            except Exception:
                pass
        result["order_by"] = order_by

        for field in fields.split(",") if fields else ():
            fields = fields.replace(field, field.strip())
            field:str = field.strip()
            if field not in self.available_fields:
                error["message"] = f"El campo no existe en la base de datos: {field} - campos disponibles: {self.available_fields}"
                return error        
       
        not_available_filter = next(filter(lambda kv: kv[0] not in self.available_fields, filters), None) # Se verifica que los filtros indicados sean campos existentes en la DB
        if not_available_filter:
            error["message"] = f"El filtro {not_available_filter[0]}, no es un campo disponible - campos disponibles: {self.available_fields}"
            return error
        result["filters"] = dict(filters)
        
        if view:
            if view == "marc":
                fields = reduce(lambda x,y:f"{x},{y}", self.marc_fields)

            elif view == "human":
                fields = reduce(lambda x,y:f"{x},{y}", self.human_fields)
        result["fields"] = fields if fields else None # campos a consultar en la DB todos, marc21, humans o custom

        try:
            result["dataset_2"] = dataset_2[0] # Se verifica si hay un segundo dataset a consultar para realizar una consulta cruzada
        except:
            pass

        result["success"] = True
        return result
    
    def where(self, args: dict, dataset:str = None) -> str:
        '''Creación de la clausula WHERE de la consulta SQL'''
        args = dict(args)
        dataset = dataset if dataset else self.dataset # Comprobación por si se están consultado dos datasets
        if not args:
            return ""
        result = f"WHERE "
        and_or = " AND " 
        for k,value in args.items():
            v = value.strip()
            # v:str = v.replace("!","")
            v:str = v.replace("|","") 
            v = re.sub("[^\w !-]", " ", v) # Los caracters especiales generan error en el módulo FTS5
            if v.endswith("OR"):
                v = v.replace("OR", "")
                and_or = " OR  "
            if v.find("null") >= 0:
                v_where = f'''{dataset}.{k} IS NULL{and_or}'''
                if v.find("!") >= 0:
                    v_where = v_where.replace("IS NULL", "IS NOT NULL")
            elif v.startswith('"') and v.endswith('"'):
                v_where = f'''{dataset}.{k} MATCH '{v}'{and_or}'''
            elif k == "siglo" or k == "decada":
                v_where = f'''{dataset}.{k} MATCH '{v}'{and_or}'''
            elif v.find("<") >= 0: # Evitar que el operador de comparación < caiga dentro del filtro ya que no es válido en la sintaxis
                v = v.replace("<", "")
                v_where = f'''{k} >= '{v}' {and_or}'''
            elif v.find(">") >= 0:
                v = v.replace(">", "")
                v_where = f'''{k} <= '{v}' {and_or}'''
            elif re.search("\d{4}\-\d{4}", v): # trabajo con dígitos y más especificamente con años de las fechas como fecha_de_nacimiento
                s, e = v.split("-")
                v_where = f'''{k} BETWEEN '{s}' AND '{e}' {and_or}'''
            else:
                v_where = f'''{dataset}.{k} MATCH '{v}*'{and_or}'''


            result += v_where
        return result[:-5] # Debe ser quitado el último operador AND o OR

    def joining(self) -> str:
        '''
        Método a utlizar cuando se consultan más de un conjunto a la vez
        La forma de hacer ésto no es mediante un INNER JOIN común, sino, realizado dos consultas simples, donde se extraen las FOREIGN KEYS del dataset 2 para utilizarlos como filtro en el dataset 1
        '''
        '''WHERE id XX OR XX OR XX...'''
        dataset_2 = self.purgue["dataset_2"]
        d_2 = list(dataset_2.keys())[0].strip()
        filters = {}
        for kv in dataset_2[d_2].split(","): # Filtros del dataset 2 
            k,v = kv.split(":")
            filters[k] = v
        query_2 = f"SELECT id FROM {d_2} "
        d_2_where = self.where(filters, d_2)
        query_2 += d_2_where
        d_2_ids = map(lambda r_id: f"{r_id[0]} OR ", self.cur.execute(query_2))
        ids = ""
        for i,r_id in enumerate(d_2_ids):
            if i == 10000:
                break
            ids += r_id
        ids = ids[:-4]
        return f"WHERE {d_2}_id MATCH '{ids}'"
        
    def query(self, count=False, limit=True) -> str:
        '''Unificación de los métodos purge, joining, where'''
        fields = self.purgue.get("fields")
        order_by = self.purgue.get("order_by")
        filters = self.purgue.get("filters")
        dataset_2 = self.purgue.get("dataset_2")

        if count and not dataset_2:
            query = f"SELECT count(*) FROM {self.dataset} "
        else:
            if fields:
                query = f"SELECT {fields} FROM {self.dataset} "
            else:
                query = f"SELECT * FROM {self.dataset} "

        if dataset_2:
            where_ids = self.joining()
            query += where_ids
            d_1_where = self.where(filters.items())
            if d_1_where:
                d_1_where = d_1_where.replace("WHERE", "")
                query += f" AND ({d_1_where})"
        else:
            query += self.where(filters.items())    
        # if order_by:
        #     if order_by.find(",") >= 0:
        #         order_by = order_by.replace(",", " ")
        #     query += f" ORDER BY {order_by} "
        if limit:
            return query + " LIMIT 1000;"
        return query
                 
    def get_estimated(self) -> None:
        '''Método para consultar cuántos resultados la consulta entregará con un timeout de 1.5 segundos (en desuso)'''
        def auxiliar():
            try:
                with open("length.txt", "w") as file:
                    file.write(f"")
                length = tuple(self.cur.execute(self.query(count=True)))[0][0]
                with open("length.txt", "w") as file:
                    file.write(f"{length}")
            except Exception:
                pass
        try:
            p = Process(target=auxiliar)
            p.start()
            p.join(1.5)
            if p.is_alive():
                p.terminate()
        except:
            pass
    
    def json(self) -> dict:
        '''Método que genera el JSON en base a lo que query haya entregado'''
        res_json = self.purgue
        if not res_json["success"]: # False sólo cuando el usuario haga mal uso de la aplicación. True puede suceder por más que la consulta no entregue resultados
            return {"success":False,"message":res_json["message"]}
        
        if res_json["fields"]: # Se crea un modelo en base a cada campo extraido del dataset (si fields=id, sólo se generará id)
            self.create_struct(res_json["fields"].split(","))
        else:
            self.create_struct(self.available_fields)

        query = self.query()   
        print(query)
                    
        '''
        saving query:
        '''
        if self.dataset != "queries": # Comprobar que se guarde la consulta a un conjunto y no a queries en sí
            self.enter(query, error=True, date=dt.datetime.now(), dataset=self.dataset, is_from_web=True if res_json.get("is_from_web") else False) # Se guarda la consulta en la db queries

        try:
            if self.dataset == "queries":
                con = sqlite3.connect("instance/users.db")
                res = con.execute(query)
            else:
                res = self.cur.execute(query)

        except sqlite3.OperationalError as e:
            res = {}
            res["success"] = False
            res["message"] = "SQLite3 Operational Error"
            res["error"] = f"{e}"
            if res["error"] == 'fts5: syntax error near ""':
                res["message"] += ": La búsqueda no ha entregado resultados en el dataset 1"
            return res
        
        result = {}
        result["success"] = True
        result["data"] = map(lambda row:structs[self.dataset](*row),res) # generar un _generator_ para luego utilizar el método msgspec en route en pos de aumentar el rendimiento de la aplicación
        result["query"] = query
        return result
    
    def export_csv(self) -> None:
        '''sqlite3 db.sqlite3 '.mode json' '.once out.json' 'select * from foo'''
        try:
            system(f"rm -r {self.dataset}*")
        except:
            pass
        file_name = self.dataset + "_" + token_hex(2)
        query = self.query(limit=False)
        query = query.replace('"',"") 
        query = f'sqlite3 instance/bne.db -header -csv -separator ";" " {query} " > {file_name}.csv'
        system(query)
        system(f"zip {file_name} {file_name}.csv")
        return file_name
    
    def export_json(self) -> None:
        try:
            system(f"rm -r {self.dataset}*")
        except:
            pass
        file_name = self.dataset + "_" + token_hex(2) 
        query = f'''sqlite3 instance/bne.db -json " {self.query(count=False, limit=False)} " > {file_name}.json'''
        system(query)
        system(f"zip {file_name} {file_name}.json")
        return file_name
    
    def enter(self, query:str, length:int=None, date:str=None, dataset:str=None, time:float=None,is_from_web:bool=False ,error:bool=None, update:bool=False):
        # g._database = None
        # con = self.get_db("instance/users.db")
        '''método para guardar la query en queries'''
        try:
            self.cur.execute("ATTACH 'instance/users.db' as queries;")
            query = query[:2000]
        except Exception as e:
            pass
        if update:
            last_id = tuple(self.cur.execute("SELECT id FROM queries.queries ORDER BY date DESC LIMIT 1;"))[0][0]
            query_str = f'''
                        UPDATE queries.queries SET length = ?, date=?, dataset=?, time=?, is_from_web=?, error=0 WHERE id = '{last_id}';
                        '''
            self.cur.execute(query_str, (length, date, dataset, time, True if is_from_web else False))
            self.con.commit()
            
        else:
            if is_from_web:
                error = False
            query_str = f'''
                    INSERT INTO queries.queries VALUES(
                    '{uuid4().hex}',
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?
                    )
                    '''
            self.cur.execute(query_str, (query, length, date, dataset, time,is_from_web ,error))
            self.con.commit()
            # g._database = sqlite3.connect("instance/bne.db")
        
if __name__ == "__main__":
    def get_db(file:str=None):
        return sqlite3.connect(current_app.config.get("DB_FILE") if not file else file)
    import unittest 
    # Estos tests ya no son necesarios
    class test_QMO(unittest.TestCase):

        def setUp(self) -> None:
            self.n_0 = QMO("geo", {"fields":"id"})
            self.n_1 = QMO("geo", {"id": "XX1000003", "limit": "1", "fields":"id"})
            self.purgue = QMO("geo", {"id": "XX", "t_024": "XX","limit":"101", "fields": "id,t_781,  t_024", "order_by": "t_781,desc", "view": "human", "per": "t_100:XX"})
            self.d2 = QMO("mon", {"fields":"id", "per":{"t_100": "Vito du"}})
            self.d2_with_filters = QMO("mon", {"fields":"id", "per":{"t_100": "Vito du"}, "id":"bimo"})

        def test_query(self):
            self.assertEqual(self.n_1.query(count=True), "SELECT count(*) FROM geo WHERE geo.id MATCH 'XX1000003*'")
            self.assertEqual(self.n_1.query(), "SELECT id FROM geo WHERE geo.id MATCH 'XX1000003*'")
            self.assertEqual(self.n_0.query(), "SELECT id FROM geo ")
            self.assertEqual(self.d2.query(), "SELECT id FROM mon WHERE per_id MATCH 'XX1024517'")
            self.assertEqual(self.d2_with_filters.query(), "SELECT id FROM mon WHERE per_id MATCH 'XX1024517' AND ( mon.id MATCH 'bimo*')")

        def test_joining(self):
            self.assertEqual(self.d2.joining(), "WHERE per_id MATCH 'XX1024517'")
            self.assertEqual(self.d2_with_filters.joining(), "WHERE per_id MATCH 'XX1024517'")


    unittest.main()
    
