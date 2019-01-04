from django.utils.translation import ugettext as _

FISCAL_TYPE = [
    (1, 'RF01', _('Ordinario')),
    (2, 'RF02', _('Contribuenti minimi (art.1, c.96-117, L. 244/07)')),
    (3, 'RF03', _('Nuove iniziative produttive (art.13, L. 388/00)')), 
    (4, 'RF04', _('Agricoltura e attività connesse e pesca (artt.34 e 34-bis, DPR 633/72)')),
    (5, 'RF05', _('Vendita sali e tabacchi (art.74, c.1, DPR. 633/72)')),
    (6, 'RF06', _('Commercio fiammiferi (art.74, c.1, DPR 633/72)')),
    (7, 'RF07', _('Editoria (art.74, c.1, DPR 633/72)')),
    (8, 'RF08', _('Gestione servizi telefonia pubblica (art.74, c.1, DPR 633/72)')),
    (9, 'RF09', _('Rivendita documenti di trasporto pubblico e di sosta (art.74, c.1, DPR 633/72)')),
    (10, 'RF10', _('Intrattenimenti, giochi e altre attività di cui alla tariffa allegata al DPR 640/72 (art.74, c.6, DPR 633/72)')),
    (11, 'RF11', _('Agenzie viaggi e turismo (art.74-ter, DPR 633/72)')),
    (12, 'RF12', _('Agriturismo (art.5, c.2, L. 413/91)')),
    (13, 'RF13', _('Vendite a domicilio (art.25-bis, c.6, DPR 600/73)')),
    (14, 'RF14', _('Rivendita beni usati, oggetti d’arte, d’antiquariato o da collezione (art.36, DL 41/95)')),
    (15, 'RF15', _('Agenzie di vendite all’asta di oggetti d’arte, antiquariato o da collezione (art.40-bis, DL 41/95)')),
    (16, 'RF16', _('IVA per cassa P.A. (art.6, c.5, DPR 633/72)')),
    (17, 'RF17', _('IVA per cassa (art. 32-bis, DL 83/2012)')),
    (18, 'RF18', _('Altro')),
    (19, 'RF19', _('Regime forfettario (art.1, c.54-89, L. 190/2014)')),
]


PROVINCES = [
    (1, 'AG', 'Agrigento'),
    (2, 'AL', 'Alessandria'),
    (3, 'AN', 'Ancona'),
    (4, 'AO', 'Aosta'),
    (5, 'AR', 'Arezzo'),
    (6, 'AP', 'Ascoli Piceno'),
    (7, 'AT', 'Asti'),
    (8, 'AV', 'Avellino'),
    (9, 'BA', 'Bari'),
    (10, 'BT', 'Barletta-Andria-Trani'),
    (11, 'BL', 'Belluno'),
    (12, 'BN', 'Benevento'),
    (13, 'BG', 'Bergamo'),
    (14, 'BI', 'Biella'),
    (15, 'BO', 'Bologna'),
    (16, 'BZ', 'Bolzano'),
    (17, 'BS', 'Brescia'),
    (18, 'BR', 'Brindisi'),
    (19, 'CA', 'Cagliari'),
    (20, 'CL', 'Caltanissetta'),
    (21, 'CB', 'Campobasso'),
    (22, 'CI', 'Carbonia-Iglesias'),
    (23, 'CE', 'Caserta'),
    (24, 'CT', 'Catania'),
    (25, 'CZ', 'Catanzaro'),
    (26, 'CH', 'Chieti'),
    (27, 'CO', 'Como'),
    (28, 'CS', 'Cosenza'),
    (29, 'CR', 'Cremona'),
    (30, 'KR', 'Crotone'),
    (31, 'CN', 'Cuneo'),
    (32, 'EN', 'Enna'),
    (33, 'FM', 'Fermo'),
    (34, 'FE', 'Ferrara'),
    (34, 'FI', 'Firenze'),
    (35, 'FG', 'Foggia'),
    (36, 'FC', 'ForlÏ-Cesena'),
    (37, 'FR', 'Frosinone'),
    (38, 'GE', 'Genova'),
    (39, 'GO', 'Gorizia'),
    (40, 'GR', 'Grosseto'),
    (41, 'IM', 'Imperia'),
    (42, 'IS', 'Isernia'),
    (43, 'SP', 'La Spezia'),
    (44, 'AQ', "L'Aquila"),
    (45, 'LT', 'Latina'),
    (46, 'LE', 'Lecce'),
    (47, 'LC', 'Lecco'),
    (48, 'LI', 'Livorno'),
    (49, 'LO', 'Lodi'),
    (50, 'LU', 'Lucca'),
    (51, 'MC', 'Macerata'),
    (52, 'MN', 'Mantova'),
    (53, 'MS', 'Massa-Carrara'),
    (54, 'MT', 'Matera'),
    (55, 'ME', 'Messina'),
    (56, 'MI', 'Milano'),
    (57, 'MO', 'Modena'),
    (58, 'MB', 'Monza e della Brianza'),
    (59, 'NA', 'Napoli'),
    (60, 'NO', 'Novara'),
    (61, 'NU', 'Nuoro'),
    (62, 'OT', 'Olbia-Tempio'),
    (63, 'OR', 'Oristano'),
    (64, 'PD', 'Padova'),
    (65, 'PA', 'Palermo'),
    (66, 'PR', 'Parma'),
    (67, 'PV', 'Pavia'),
    (68, 'PG', 'Perugia'),
    (69, 'PU', 'Pesaro e Urbino'),
    (70, 'PE', 'Pescara'),
    (71, 'PC', 'Piacenza'),
    (72, 'PI', 'Pisa'),
    (73, 'PT', 'Pistoia'),
    (74, 'PN', 'Pordenone'),
    (75, 'PZ', 'Potenza'),
    (76, 'PO', 'Prato'),
    (77, 'RG', 'Ragusa'),
    (78, 'RA', 'Ravenna'),
    (79, 'RC', 'Reggio Calabria'),
    (80, 'RE', 'Reggio Emilia'),
    (81, 'RI', 'Rieti'),
    (82, 'RN', 'Rimini'),
    (83, 'RM', 'Roma'),
    (84, 'RO', 'Rovigo'),
    (85, 'SA', 'Salerno'),
    (86, 'VS', 'Medio Campidano'),
    (87, 'SS', 'Sassari'),
    (88, 'SV', 'Savona'),
    (89, 'SI', 'Siena'),
    (90, 'SR', 'Siracusa'),
    (91, 'SO', 'Sondrio'),
    (92, 'TA', 'Taranto'),
    (93, 'TE', 'Teramo'),
    (94, 'TR', 'Terni'),
    (95, 'TO', 'Torino'),
    (96, 'OG', 'Ogliastra'),
    (97, 'TP', 'Trapani'),
    (98, 'TN', 'Trento'),
    (99, 'TV', 'Treviso'),
    (100, 'TS', 'Trieste'),
    (101, 'UD', 'Udine'),
    (102, 'VA', 'Varese'),
    (103, 'VE', 'Venezia'),
    (104, 'VB', 'Verbano-Cusio-Ossola'),
    (105, 'VC', 'Vercelli'),
    (106, 'VR', 'Verona'),
    (107, 'VV', 'Vibo Valentia'),
    (108, 'VI', 'Vicenza'),
    (109, 'VT', 'Viterbo')
    
]


COUNTRIES = [
    ('AF', _('Afghanistan')),
    ('AL', _('Albania')),
    ('DZ', _('Algeria')),
    ('AS', _('American Samoa')),
    ('AD', _('Andorra')),
    ('AO', _('Angola')),
    ('AI', _('Anguilla')),
    ('AQ', _('Antarctica')),
    ('AG', _('Antigua And Barbuda')),
    ('AR', _('Argentina')),
    ('AM', _('Armenia')),
    ('AW', _('Aruba')),
    ('AU', _('Australia')),
    ('AT', _('Austria')),
    ('AZ', _('Azerbaijan')),
    ('BS', _('Bahamas')),
    ('BH', _('Bahrain')),
    ('BD', _('Bangladesh')),
    ('BB', _('Barbados')),
    ('BY', _('Belarus')),
    ('BE', _('Belgium')),
    ('BZ', _('Belize')),
    ('BJ', _('Benin')),
    ('BM', _('Bermuda')),
    ('BT', _('Bhutan')),
    ('BO', _('Bolivia')),
    ('BA', _('Bosnia And Herzegowina')),
    ('BW', _('Botswana')),
    ('BV', _('Bouvet Island')),
    ('BR', _('Brazil')),
    ('BN', _('Brunei Darussalam')),
    ('BG', _('Bulgaria')),
    ('BF', _('Burkina Faso')),
    ('BI', _('Burundi')),
    ('KH', _('Cambodia')),
    ('CM', _('Cameroon')),
    ('CA', _('Canada')),
    ('CV', _('Cape Verde')),
    ('KY', _('Cayman Islands')),
    ('CF', _('Central African Rep')),
    ('TD', _('Chad')),
    ('CL', _('Chile')),
    ('CN', _('China')),
    ('CX', _('Christmas Island')),
    ('CC', _('Cocos Islands')),
    ('CO', _('Colombia')),
    ('KM', _('Comoros')),
    ('CG', _('Congo')),
    ('CK', _('Cook Islands')),
    ('CR', _('Costa Rica')),
    ('CI', _('Cote D`ivoire')),
    ('HR', _('Croatia')),
    ('CU', _('Cuba')),
    ('CY', _('Cyprus')),
    ('CZ', _('Czech Republic')),
    ('DK', _('Denmark')),
    ('DJ', _('Djibouti')),
    ('DM', _('Dominica')),
    ('DO', _('Dominican Republic')),
    ('TP', _('East Timor')),
    ('EC', _('Ecuador')),
    ('EG', _('Egypt')),
    ('SV', _('El Salvador')),
    ('GQ', _('Equatorial Guinea')),
    ('ER', _('Eritrea')),
    ('EE', _('Estonia')),
    ('ET', _('Ethiopia')),
    ('FK', _('Falkland Islands (Malvinas)')),
    ('FO', _('Faroe Islands')),
    ('FJ', _('Fiji')),
    ('FI', _('Finland')),
    ('FR', _('France')),
    ('GF', _('French Guiana')),
    ('PF', _('French Polynesia')),
    ('TF', _('French S. Territories')),
    ('GA', _('Gabon')),
    ('GM', _('Gambia')),
    ('GE', _('Georgia')),
    ('DE', _('Germany')),
    ('GH', _('Ghana')),
    ('GI', _('Gibraltar')),
    ('GR', _('Greece')),
    ('GL', _('Greenland')),
    ('GD', _('Grenada')),
    ('GP', _('Guadeloupe')),
    ('GU', _('Guam')),
    ('GT', _('Guatemala')),
    ('GN', _('Guinea')),
    ('GW', _('Guinea-bissau')),
    ('GY', _('Guyana')),
    ('HT', _('Haiti')),
    ('HN', _('Honduras')),
    ('HK', _('Hong Kong')),
    ('HU', _('Hungary')),
    ('IS', _('Iceland')),
    ('IN', _('India')),
    ('ID', _('Indonesia')),
    ('IR', _('Iran')),
    ('IQ', _('Iraq')),
    ('IE', _('Ireland')),
    ('IL', _('Israel')),
    ('IT', _('Italy')),
    ('JM', _('Jamaica')),
    ('JP', _('Japan')),
    ('JO', _('Jordan')),
    ('KZ', _('Kazakhstan')),
    ('KE', _('Kenya')),
    ('KI', _('Kiribati')),
    ('KP', _('Korea (North)')),
    ('KR', _('Korea (South)')),
    ('KW', _('Kuwait')),
    ('KG', _('Kyrgyzstan')),
    ('LA', _('Laos')),
    ('LV', _('Latvia')),
    ('LB', _('Lebanon')),
    ('LS', _('Lesotho')),
    ('LR', _('Liberia')),
    ('LY', _('Libya')),
    ('LI', _('Liechtenstein')),
    ('LT', _('Lithuania')),
    ('LU', _('Luxembourg')),
    ('MO', _('Macau')),
    ('MK', _('Macedonia')),
    ('MG', _('Madagascar')),
    ('MW', _('Malawi')),
    ('MY', _('Malaysia')),
    ('MV', _('Maldives')),
    ('ML', _('Mali')),
    ('MT', _('Malta')),
    ('MH', _('Marshall Islands')),
    ('MQ', _('Martinique')),
    ('MR', _('Mauritania')),
    ('MU', _('Mauritius')),
    ('YT', _('Mayotte')),
    ('MX', _('Mexico')),
    ('FM', _('Micronesia')),
    ('MD', _('Moldova')),
    ('MC', _('Monaco')),
    ('MN', _('Mongolia')),
    ('MS', _('Montserrat')),
    ('MA', _('Morocco')),
    ('MZ', _('Mozambique')),
    ('MM', _('Myanmar')),
    ('NA', _('Namibia')),
    ('NR', _('Nauru')),
    ('NP', _('Nepal')),
    ('NL', _('Netherlands')),
    ('AN', _('Netherlands Antilles')),
    ('NC', _('New Caledonia')),
    ('NZ', _('New Zealand')),
    ('NI', _('Nicaragua')),
    ('NE', _('Niger')),
    ('NG', _('Nigeria')),
    ('NU', _('Niue')),
    ('NF', _('Norfolk Island')),
    ('MP', _('Northern Mariana Islands')),
    ('NO', _('Norway')),
    ('OM', _('Oman')),
    ('PK', _('Pakistan')),
    ('PW', _('Palau')),
    ('PA', _('Panama')),
    ('PG', _('Papua New Guinea')),
    ('PY', _('Paraguay')),
    ('PE', _('Peru')),
    ('PH', _('Philippines')),
    ('PN', _('Pitcairn')),
    ('PL', _('Poland')),
    ('PT', _('Portugal')),
    ('PR', _('Puerto Rico')),
    ('QA', _('Qatar')),
    ('RE', _('Reunion')),
    ('RO', _('Romania')),
    ('RU', _('Russian Federation')),
    ('RW', _('Rwanda')),
    ('KN', _('Saint Kitts And Nevis')),
    ('LC', _('Saint Lucia')),
    ('VC', _('St Vincent/Grenadines')),
    ('WS', _('Samoa')),
    ('SM', _('San Marino')),
    ('ST', _('Sao Tome')),
    ('SA', _('Saudi Arabia')),
    ('SN', _('Senegal')),
    ('SC', _('Seychelles')),
    ('SL', _('Sierra Leone')),
    ('SG', _('Singapore')),
    ('SK', _('Slovakia')),
    ('SI', _('Slovenia')),
    ('SB', _('Solomon Islands')),
    ('SO', _('Somalia')),
    ('ZA', _('South Africa')),
    ('ES', _('Spain')),
    ('LK', _('Sri Lanka')),
    ('SH', _('St. Helena')),
    ('PM', _('St.Pierre')),
    ('SD', _('Sudan')),
    ('SR', _('Suriname')),
    ('SZ', _('Swaziland')),
    ('SE', _('Sweden')),
    ('CH', _('Switzerland')),
    ('SY', _('Syrian Arab Republic')),
    ('TW', _('Taiwan')),
    ('TJ', _('Tajikistan')),
    ('TZ', _('Tanzania')),
    ('TH', _('Thailand')),
    ('TG', _('Togo')),
    ('TK', _('Tokelau')),
    ('TO', _('Tonga')),
    ('TT', _('Trinidad And Tobago')),
    ('TN', _('Tunisia')),
    ('TR', _('Turkey')),
    ('TM', _('Turkmenistan')),
    ('TV', _('Tuvalu')),
    ('UG', _('Uganda')),
    ('UA', _('Ukraine')),
    ('AE', _('United Arab Emirates')),
    ('UK', _('United Kingdom')),
    ('US', _('United States')),
    ('UY', _('Uruguay')),
    ('UZ', _('Uzbekistan')),
    ('VU', _('Vanuatu')),
    ('VA', _('Vatican City State')),
    ('VE', _('Venezuela')),
    ('VN', _('Viet Nam')),
    ('VG', _('Virgin Islands (British)')),
    ('VI', _('Virgin Islands (U.S.)')),
    ('EH', _('Western Sahara')),
    ('YE', _('Yemen')),
    ('YU', _('Yugoslavia')),
    ('ZR', _('Zaire')),
    ('ZM', _('Zambia')),
    ('ZW', _('Zimbabwe')),
]


TAX_RATE = [
    (1, 4, _('Aliquota minima')),
    (2, 10, _('Aliquota ridotta')),
    (3, 22, _('Aliquota ordinaria'))
]