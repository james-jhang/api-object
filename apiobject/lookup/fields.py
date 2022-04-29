from .lookup import ValueID

class AssignmentLevel:
	DATA_PANEL_PORT = ValueID('Data Panel Port', 93204)
	DATA_PORT = ValueID('Data Port', 93202)
	ITEM = ValueID('Item', 93201)
	POWER_SUPPLY_PORT = ValueID('Power Supply Port', 93205)
	SFP_CONNECTOR = ValueID('SFP Connector', 93203)


class Class:
	AC_DISTRIBUTION = ValueID('AC Distribution', 2600)
	BATTERY = ValueID('Battery', 2500)
	CABINET = ValueID('Cabinet', 1100)
	DATA_PANEL = ValueID('Data Panel', 1500)
	DEVICE = ValueID('Device', 1200)
	FLOOR_PDU = ValueID('Floor PDU', 2300)
	HVAC = ValueID('HVAC', 3500)
	NETWORK = ValueID('Network', 1300)
	PASSIVE = ValueID('Passive', 4100)
	POWER_OUTLET = ValueID('Power Outlet', 2200)
	POWER_SOURCE = ValueID('Power Source', 2700)
	PROBE = ValueID('Probe', 1400)
	RACK_PDU = ValueID('Rack PDU', 2100)
	UPS = ValueID('UPS', 2400)


class SoltType:
	NONE = ValueID('None', 93251)
	CPU_SOCKET = ValueID('CPU Socket', 93252)
	RAM_SLOT = ValueID('RAM Slot', 93253)
	EXPANSION_SLOT = ValueID('Expansion Slot', 93254)
	DAUGHTER_BOARD_SLOT = ValueID('Daughter Board Slot', 93255)
	DISK_BAY = ValueID('Disk Bay', 93256)
	POWER_SUPPLY_SLOT = ValueID('Power Supply Slot', 93257)


class TrackingType:
	COLLECTIVELY = ValueID('Collectively', 93352)
	INDIVIDUALLY = ValueID('Individually', 93351)


class CustomFieldDataType:
	TEXT = ValueID('text', 91016)
	TEXTAREA = ValueID('textarea', 91017)
	NUMERIC = ValueID('numeric', 91018)
	DATE = ValueID('date', 91019)
	CHECKBOX = ValueID('checkbox', 91020)
	PICK_LIST = ValueID('pick-list', 91021)
	MULTI_SELECT_PICK_LIST = ValueID('multi-select pick-list', 91022)
	TAGS = ValueID('tags', 91023)
	CONTACTS = ValueID('contacts', 91024)


class ItemStatus:
	ARCHIVED = ValueID('Archived', 5085)
	INSTALLED = ValueID('Installed', 5082)
	OFF_SITE = ValueID('Off-Site', 5084)
	PLANNED = ValueID('Planned', 5081)
	PLANNED_DECOMM_ = ValueID('Planned Decomm.', 5092)
	POWERED_OFF = ValueID('Powered-off', 5083)
	STORAGE = ValueID('Storage', 5088)


class PartStatus:
	BROKEN = ValueID('Broken', 2447)
	LOST = ValueID('Lost', 2448)
	IN_STOCK = ValueID('In Stock', 2463)
	IN_USE = ValueID('In Use', 2464)
	ARCHIVED = ValueID('Archived', 2465)


class Location:
	ACDC = ValueID('ACDC', 41)
	DC___FL___RO = ValueID('DC > FL > RO', 39)
	DGS_CHANGECONTROL = ValueID('DGS-CHANGECONTROL', 40)
	RBAC0 = ValueID('RBAC0', 35)
	RBAC1 = ValueID('RBAC1', 18)
	SITE_A = ValueID('SITE A', 1)
	SITE_B = ValueID('SITE B', 2)
	SITE_C = ValueID('SITE C', 7)
	SITE_COLO = ValueID('SITE COLO', 8)
	SITE_IDF = ValueID('SITE IDF', 6)


class PartClassField:
	CPU = ValueID('CPU', 2449)
	DAUGHTER_BOARD = ValueID('Daughter Board', 2456)
	HARD_DRIVE = ValueID('Hard Drive', 2450)
	MPO_CASSETTE = ValueID('MPO Cassette', 2451)
	NIC = ValueID('NIC', 2452)
	POWER_SUPPLY = ValueID('Power Supply', 2453)
	POWER_SUPPLY = ValueID('Power Supply', 2453)
	POWER_SUPPLY = ValueID('Power Supply', 2453)
	RAM = ValueID('RAM', 2454)
	SFP = ValueID('SFP', 2455)
	SFP = ValueID('SFP', 2455)


class Make:
	_3COM = ValueID('3Com', 59)
	_911_ENABLE = ValueID('911 Enable', 437)
	A10_NETWORKS = ValueID('A10 Networks', 160)
	ABN_BRAUN = ValueID('ABN Braun', 304)
	ABOVENET_COMMUNICATIONS = ValueID('AboveNet Communications', 305)
	ACBEL_POLYTECH = ValueID('AcBel Polytech', 79)
	ACCEDIAN_NETWORKS = ValueID('Accedian Networks', 306)
	AC_DC = ValueID('AC/DC', 544)
	ACER = ValueID('Acer', 307)
	ACMEPACKET = ValueID('AcmePacket', 161)
	ACNC = ValueID('ACNC', 308)
	ACTELIS_NETWORKS = ValueID('Actelis Networks', 162)
	ACTERNA = ValueID('Acterna', 309)
	ACTIVEPOWER = ValueID('ActivePower', 85)
	ADC = ValueID('ADC', 86)
	ADDLOGIX = ValueID('Addlogix', 163)
	ADIC = ValueID('ADIC', 164)
	ADI_ENGINEERING = ValueID('ADI Engineering', 459)
	ADTRAN = ValueID('Adtran', 18)
	ADVA = ValueID('ADVA', 165)
	AETA = ValueID('AETA', 310)
	AETHRA = ValueID('Aethra', 166)
	AFCO = ValueID('Afco', 142)
	AIRDEFENSE = ValueID('AirDefense', 87)
	AKG_ACOUSTICS = ValueID('AKG Acoustics', 311)
	AKONIX = ValueID('Akonix', 167)
	ALBIS_TECHNOLOGIES = ValueID('Albis Technologies', 168)
	ALCATEL_LUCENT = ValueID('Alcatel-Lucent', 169)
	ALLIED_TELESIS = ValueID('Allied Telesis', 88)
	ALLOY = ValueID('Alloy', 446)
	ALTIGA = ValueID('Altiga', 476)
	ALTINEX = ValueID('Altinex', 447)
	ALTRONIX = ValueID('Altronix', 89)
	ALTUSEN = ValueID('Altusen', 477)
	AMAX = ValueID('Amax', 148)
	AMDAHL = ValueID('Amdahl', 312)
	AMP_NETCONNECT = ValueID('Amp Netconnect', 46)
	AMX = ValueID('AMX', 170)
	ANDA_NETWORKS = ValueID('ANDA Networks', 171)
	AOC = ValueID('AOC', 172)
	APC = ValueID('APC', 10)
	APERTURE = ValueID('Aperture', 448)
	APEX = ValueID('APEX', 173)
	APPLE = ValueID('Apple', 174)
	APPOSITE_TECHNOLOGIES = ValueID('Apposite Technologies', 313)
	APT = ValueID('APT', 460)
	ARISTA_NETWORKS = ValueID('Arista Networks', 436)
	ARP = ValueID('ARP', 62)
	ARUBA_NETWORKS = ValueID('Aruba Networks', 175)
	ASCEND = ValueID('Ascend', 90)
	ATEN = ValueID('ATEN', 177)
	ATLAS_SOUND = ValueID('Atlas Sound', 178)
	AT_T = ValueID('AT&T', 176)
	ATTO_TECHNOLOGY = ValueID('ATTO Technology', 458)
	ATX_NETWORKS = ValueID('ATX Networks', 548)
	AUDIOCODES = ValueID('AudioCodes', 179)
	AUDIO_NET = ValueID('Audio Net', 449)
	AURORA = ValueID('Aurora', 450)
	AVAYA = ValueID('Avaya', 91)
	AVOCENT = ValueID('Avocent', 57)
	AVOTUS = ValueID('Avotus', 180)
	AVTECH = ValueID('Avtech', 149)
	AXERRA = ValueID('Axerra', 181)
	AXWAY = ValueID('Axway', 92)
	BARRACUDA_NETWORKS = ValueID('Barracuda Networks', 182)
	BAYTECH = ValueID('BayTech', 80)
	BELDEN = ValueID('Belden', 138)
	BELKIN = ValueID('Belkin', 93)
	BENQ = ValueID('Benq', 478)
	BIAMP = ValueID('Biamp', 183)
	BITSTREAM = ValueID('BitStream', 184)
	BLACKBOX = ValueID('Blackbox', 60)
	BLADE_NETWORK_TECHNOLOGIES = ValueID('Blade Network Technologies', 74)
	B_LINE = ValueID('B-Line', 185)
	BLONDER_TONGUE = ValueID('Blonder Tongue', 186)
	BLUEARC = ValueID('BlueArc', 52)
	BLUECAT = ValueID('BlueCat', 150)
	BLUECOAT = ValueID('BlueCoat', 64)
	BLUE_RIDGE = ValueID('Blue Ridge', 451)
	BNI_SOLUTIONS = ValueID('BNI Solutions', 187)
	BOMGAR = ValueID('Bomgar', 528)
	BRADFORD_NETWORKS = ValueID('Bradford Networks', 94)
	BRAND_REX = ValueID('Brand-Rex', 314)
	BROADBAND_NETWORKS = ValueID('Broadband Networks', 315)
	BROCADE = ValueID('Brocade', 14)
	BROOKS_POWER_SYSTEMS = ValueID('Brooks Power Systems', 188)
	BT = ValueID('BT', 189)
	BTDIAMONDIP = ValueID('BTDiamondIP', 438)
	BUFFALO_TECHNOLOGIES = ValueID('Buffalo Technologies', 479)
	BURLE = ValueID('Burle', 190)
	CABLE_TALK = ValueID('Cable Talk', 139)
	CABLEXPRESS = ValueID('CABLExpress', 191)
	CACHE_FLOW = ValueID('Cache Flow', 317)
	CANOGA_PERKINS = ValueID('Canoga Perkins', 135)
	CARLING = ValueID('Carling', 318)
	CARRIER_ACCESS_CORP = ValueID('Carrier Access Corp', 192)
	CASTELLE = ValueID('Castelle', 319)
	CA_TECHNOLOGIES = ValueID('CA Technologies', 316)
	CDI = ValueID('CDI', 452)
	CDI_UNIGUARD = ValueID('CDI Uniguard', 480)
	CELESTIX = ValueID('Celestix', 481)
	CHECKPOINT = ValueID('Checkpoint', 193)
	CIENA = ValueID('Ciena', 95)
	CINEMASSIVE = ValueID('CineMassive', 453)
	CISCO_SYSTEMS = ValueID('Cisco Systems', 17)
	CITEL = ValueID('Citel', 194)
	CITRIX = ValueID('Citrix', 151)
	CLEARFIELD_CONNECTION = ValueID('Clearfield Connection', 320)
	CLINT = ValueID('Clint', 195)
	CODEX = ValueID('Codex', 96)
	COGECO = ValueID('Cogeco', 196)
	COLO_PROVIDED = ValueID('Colo Provided', 457)
	COLT = ValueID('COLT', 321)
	COMCAST = ValueID('Comcast', 322)
	COMMSCOPE = ValueID('CommScope', 2)
	COMPAQ = ValueID('Compaq', 454)
	COMPUMASTER = ValueID('CompuMaster', 197)
	COMPUTONE = ValueID('Computone', 97)
	COMTECH = ValueID('Comtech', 455)
	CONTROL_RESOURCES = ValueID('Control Resources', 323)
	CORNING = ValueID('Corning', 29)
	CORVIL = ValueID('Corvil', 537)
	CPI = ValueID('CPI', 12)
	CRC = ValueID('CRC', 482)
	CREATIVE = ValueID('Creative', 483)
	CRESTRON = ValueID('Crestron', 484)
	CROSSBEAM = ValueID('Crossbeam', 198)
	CROWN_AUDIO = ValueID('Crown Audio', 199)
	CRYTYCAL_SERVICE_MANAGEMENT = ValueID('Crytycal Service Management', 324)
	CTC = ValueID('CTC', 325)
	CTCSP = ValueID('CTCSP', 326)
	CTDI = ValueID('CTDI', 200)
	CTV = ValueID('CTV', 538)
	CUBIX = ValueID('Cubix', 98)
	CURRYS = ValueID('Currys', 201)
	CWSS = ValueID('CWSS', 327)
	CYAN = ValueID('Cyan', 328)
	CYBER_ARK = ValueID('Cyber-Ark', 202)
	CYBERGUARD = ValueID('CyberGuard', 329)
	CYBEX = ValueID('Cybex', 99)
	CYCLADES = ValueID('Cyclades', 16)
	CYGNET = ValueID('Cygnet', 330)
	DATACOM = ValueID('Datacom', 203)
	DATACOM_SYSTEMS = ValueID('Datacom Systems', 204)
	DATA_DOMAIN = ValueID('Data Domain', 75)
	DATAPROBE = ValueID('Dataprobe', 205)
	DDN = ValueID('DDN', 546)
	DEES_COMMUNICATIONS = ValueID('DEES Communications', 206)
	DELL = ValueID('Dell', 3)
	DELTA_ELECTRONICS = ValueID('Delta Electronics', 331)
	DIALOGIC = ValueID('Dialogic', 207)
	DIAMOND = ValueID('Diamond', 533)
	DIAMOND_MULTIMEDIA = ValueID('Diamond Multimedia', 332)
	DIGI = ValueID('DIGI', 100)
	DIGITAL = ValueID('Digital', 208)
	DIGITAL_LINK = ValueID('Digital Link', 209)
	DIGITAL_WATCHDOG = ValueID('Digital Watchdog', 101)
	DINTEK = ValueID('Dintek', 333)
	DIRECTV = ValueID('DirecTV', 210)
	D_LINK = ValueID('D-Link', 152)
	DROBO = ValueID('Drobo', 485)
	DVTEL = ValueID('DVTel', 211)
	EATON = ValueID('Eaton', 55)
	EDGEWATER_NETWORKS = ValueID('Edgewater Networks', 486)
	EDP = ValueID('EDP', 334)
	EIZO = ValueID('Eizo', 335)
	ELECTRON_METAL = ValueID('Electron Metal', 534)
	ELECTRORACK = ValueID('Electrorack', 102)
	ELPROMA = ValueID('Elproma', 336)
	ELTEK_VALERE = ValueID('Eltek Valere', 103)
	EMC = ValueID('EMC', 4)
	EMERSON = ValueID('Emerson', 212)
	EMPIRIX = ValueID('Empirix', 337)
	ENDRUN_TECHNOLOGIES = ValueID('EndRun Technologies', 213)
	ENGINUITY_COMMUNICATIONS = ValueID('Enginuity Communications', 338)
	ENTERASYS = ValueID('Enterasys', 214)
	ERICSSON = ValueID('Ericsson', 215)
	ETHERACCESS = ValueID('EtherAccess', 487)
	EXABYTE = ValueID('Exabyte', 153)
	EXAGRID = ValueID('Exagrid', 143)
	EXCEL = ValueID('Excel', 339)
	EXTREME_NETWORKS = ValueID('Extreme Networks', 23)
	EXTRON_ELECTRONICS = ValueID('Extron Electronics', 216)
	F5_NETWORKS = ValueID('F5 Networks', 81)
	FAXBOX = ValueID('Faxbox', 340)
	FAXFINDER = ValueID('FaxFinder', 461)
	FEI_ZYFER = ValueID('FEI-Zyfer', 488)
	FIBERNET = ValueID('Fibernet', 342)
	FIBER_OPTIONS = ValueID('Fiber Options', 341)
	FIBRIDGE = ValueID('Fibridge', 343)
	FIDELTRONIK = ValueID('Fideltronik', 217)
	FIREEYE = ValueID('FireEye', 462)
	FIREMON = ValueID('Firemon', 439)
	FORCE_10_NETWORKS = ValueID('Force 10 Networks', 47)
	FORESCOUT = ValueID('ForeScout', 218)
	FORE_SYSTEMS = ValueID('Fore Systems', 489)
	FORTIGATE = ValueID('FortiGate', 490)
	FORTINET = ValueID('Fortinet', 219)
	FOUNDRY = ValueID('Foundry', 21)
	FUJITSU = ValueID('Fujitsu', 72)
	FUKUDA = ValueID('Fukuda', 344)
	FUNKWERK = ValueID('Funkwerk', 63)
	GARRETTCOMM = ValueID('GarrettComm', 345)
	GATEWAY = ValueID('Gateway', 220)
	GDC = ValueID('GDC', 346)
	GE = ValueID('GE', 347)
	GEA = ValueID('GEA', 348)
	GEFEN = ValueID('Gefen', 349)
	GEIST = ValueID('Geist', 56)
	GENERAL_DYNAMICS = ValueID('General Dynamics', 491)
	GENERAL_PROJECTION = ValueID('General Projection', 350)
	GENERIC = ValueID('Generic', 1)
	GENTNER = ValueID('Gentner', 351)
	GIGAMON = ValueID('Gigamon', 221)
	GIGA_PLUS = ValueID('Giga Plus', 352)
	GIGASTAR = ValueID('Gigastar', 353)
	GLOBAL_DATAGUARD = ValueID('Global DataGuard', 434)
	GOOGLE = ValueID('Google', 104)
	GRAHAM_SMITH = ValueID('Graham Smith', 354)
	GREAT_LAKES = ValueID('Great Lakes', 492)
	GTA = ValueID('GTA', 355)
	H3C = ValueID('H3C', 154)
	HAFLER = ValueID('Hafler', 356)
	HAIVISION = ValueID('Haivision', 539)
	HAMMOND_MFG = ValueID('Hammond Mfg', 144)
	HAYES = ValueID('Hayes', 222)
	HELLERMANNTYTON = ValueID('HellermannTyton', 493)
	HENSEL = ValueID('Hensel', 357)
	HIKVISION = ValueID('HIKVision', 540)
	HITACHI = ValueID('Hitachi', 145)
	HOFFMAN = ValueID('Hoffman', 146)
	HOMACO = ValueID('Homaco', 358)
	HONEYWELL = ValueID('Honeywell', 359)
	HP = ValueID('HP', 20)
	HUAWEI = ValueID('Huawei', 360)
	HUBBELL = ValueID('Hubbell', 26)
	HYPEREDGE = ValueID('Hyperedge', 223)
	IBM = ValueID('IBM', 8)
	IBOSS = ValueID('Iboss', 494)
	IFS = ValueID('IFS', 224)
	IKUSI = ValueID('IKUSI', 361)
	IMAGETAG = ValueID('Imagetag', 225)
	IMC = ValueID('IMC', 362)
	IMPERVAGUARD = ValueID('ImpervaGuard', 226)
	IMPRIVATA = ValueID('Imprivata', 521)
	INFOBLOX = ValueID('Infoblox', 227)
	INFORTREND = ValueID('Infortrend', 228)
	INGRAIN_NETWORKS = ValueID('Ingrain Networks', 229)
	INLET_TECHNOLOGIES = ValueID('Inlet Technologies', 463)
	INTEL = ValueID('Intel', 105)
	INTELLINET = ValueID('Intellinet', 230)
	INTERALIA = ValueID('Interalia', 106)
	IP_ACCESS = ValueID('ip.access', 363)
	IPC = ValueID('IPC', 231)
	IPHONE = ValueID('Iphone', 495)
	IRONPORT = ValueID('IronPort', 496)
	ISILON = ValueID('Isilon', 45)
	ISTAR = ValueID('Istar', 497)
	ITE = ValueID('ITE', 364)
	ITWATCHDOGS = ValueID('ITWatchdogs', 232)
	IXIA = ValueID('IXIA', 464)
	JBM_ELECTRONICS = ValueID('JBM Electronics', 365)
	JDS_UNIPHASE = ValueID('JDS Uniphase', 107)
	JUNIPER_NETWORKS = ValueID('Juniper Networks', 43)
	JUPITER = ValueID('Jupiter', 498)
	KBOX = ValueID('Kbox', 233)
	KEMP___LAURITZEN = ValueID('Kemp & Lauritzen', 366)
	KENTROX = ValueID('Kentrox', 108)
	KEYNOTE = ValueID('Keynote', 234)
	KINGSTON = ValueID('Kingston', 367)
	KINGWIN = ValueID('Kingwin', 368)
	KNURR = ValueID('Knurr', 109)
	KPN = ValueID('KPN', 369)
	KRAMER = ValueID('Kramer', 370)
	KRONE = ValueID('Krone', 371)
	KTI_NETWORKS = ValueID('KTI Networks', 235)
	LACIE = ValueID('Lacie', 499)
	LANCAST = ValueID('Lancast', 236)
	LANCOM = ValueID('Lancom', 65)
	LANCOPE = ValueID('Lancope', 237)
	LANDESK = ValueID('LANDesk', 238)
	LANEX = ValueID('Lanex', 239)
	LANIER = ValueID('Lanier', 372)
	LANTRONIX = ValueID('Lantronix', 82)
	LARSCOM = ValueID('Larscom', 240)
	LATITUDE = ValueID('Latitude', 373)
	LAYER_ZERO = ValueID('Layer Zero', 374)
	LECROY = ValueID('LeCroy', 465)
	LENOVO = ValueID('Lenovo', 241)
	LEVITON = ValueID('Leviton', 78)
	LGC_WIRELESS = ValueID('LGC Wireless', 242)
	LGX = ValueID('LGX', 243)
	LIEBERT = ValueID('Liebert', 27)
	LIGHTWAVE = ValueID('Lightwave', 375)
	LINEAGE_POWER = ValueID('Lineage Power', 376)
	LINKSYS = ValueID('Linksys', 244)
	LOGICAL_SOLUTIONS = ValueID('Logical Solutions', 245)
	LOOP_TELECOM = ValueID('Loop Telecom', 246)
	LORAIN_POWER_SYSTEMS = ValueID('Lorain Power Systems', 110)
	LSI = ValueID('LSI', 51)
	LUCENT_TECHNOLOGIES = ValueID('Lucent Technologies', 377)
	MARCONI = ValueID('Marconi', 378)
	MATRIX = ValueID('Matrix', 111)
	MAUVE = ValueID('Mauve', 379)
	MCAFEE = ValueID('McAfee', 112)
	MCDATA = ValueID('McDATA', 113)
	MCGOHAN = ValueID('McGohan', 380)
	MEDIASTAR = ValueID('Mediastar', 247)
	MEDIATRIX = ValueID('Mediatrix', 500)
	MEINBERG = ValueID('Meinberg', 541)
	MELLANOX = ValueID('Mellanox', 248)
	MENTAT = ValueID('Mentat', 501)
	MESSAGELABS = ValueID('MessageLabs', 249)
	METRODATA = ValueID('Metrodata', 250)
	MICRON = ValueID('Micron', 381)
	MICROSENS = ValueID('Microsens', 251)
	MIDDLE_ATLANTIC = ValueID('Middle Atlantic', 252)
	MILAN_TECHNOLOGY = ValueID('Milan Technology', 440)
	MINICOM = ValueID('Minicom', 502)
	MINKELS = ValueID('Minkels', 522)
	MIRACLE = ValueID('Miracle', 253)
	MIRAPOINT = ValueID('Mirapoint', 147)
	MITSUBISHI = ValueID('Mitsubishi', 435)
	MOBILE_IRON = ValueID('Mobile Iron', 382)
	MOTOROLA = ValueID('Motorola', 254)
	MRV = ValueID('MRV', 114)
	MRV_COMMUNICATIONS = ValueID('MRV Communications', 19)
	MU_DYNAMICS = ValueID('Mu Dynamics', 466)
	MULTILINK = ValueID('Multilink', 383)
	MULTITECH = ValueID('MultiTech', 115)
	MULTITECH_SYSTEMS = ValueID('Multitech Systems', 255)
	MUZAK = ValueID('Muzak', 384)
	NANAO = ValueID('Nanao', 385)
	NATIONAL = ValueID('National', 386)
	NCIRCLE = ValueID('nCircle', 116)
	NCR = ValueID('NCR', 387)
	NEC = ValueID('NEC', 388)
	NETAPP = ValueID('NetApp', 5)
	NETGEAR = ValueID('Netgear', 50)
	NETOPTICS = ValueID('NetOptics', 140)
	NETQOS = ValueID('NetQoS', 523)
	NETSCOUT = ValueID('Netscout', 136)
	NETWORK_ASSOCIATES = ValueID('Network Associates', 389)
	NETWORK_GENERAL = ValueID('Network General', 256)
	NETWORK_INSTRUMENTS = ValueID('Network Instruments', 117)
	NETWORK_INTELLIGENCE = ValueID('Network Intelligence', 257)
	NEWBRIDGE = ValueID('NewBridge', 390)
	NEWMAR = ValueID('Newmar', 391)
	NEWTON = ValueID('Newton', 392)
	NEXANS = ValueID('Nexans', 118)
	NEXSAN = ValueID('NexSan', 393)
	NGENIUS = ValueID('Ngenius', 258)
	NHP = ValueID('NHP', 394)
	NICE = ValueID('Nice', 259)
	NIMBLE_STORAGE = ValueID('Nimble Storage', 529)
	NOKIA = ValueID('NOKIA', 260)
	NORAN_TEL = ValueID('Noran Tel', 141)
	NORSTAR = ValueID('Norstar', 395)
	NORTEL_NETWORKS = ValueID('Nortel Networks', 15)
	NOTIFIER = ValueID('Notifier', 396)
	NTI = ValueID('NTI', 503)
	NTT = ValueID('NTT', 397)
	NUTANIX = ValueID('Nutanix', 456)
	OKI = ValueID('OKI', 398)
	OLSON = ValueID('Olson', 261)
	OMNITRONIX = ValueID('Omnitronix', 120)
	OMNITRON_SYSTEMS = ValueID('Omnitron Systems', 119)
	OPENGEAR = ValueID('Opengear', 155)
	OPENTEXT = ValueID('OpenText', 504)
	OPNET = ValueID('Opnet', 262)
	ORACLE = ValueID('Oracle', 399)
	ORTRONICS = ValueID('Ortronics', 24)
	OST = ValueID('OST', 400)
	OVERLAND = ValueID('Overland', 66)
	OVERTURE_NETWORKS = ValueID('Overture Networks', 263)
	PACE = ValueID('Pace', 401)
	PACKETEER = ValueID('Packeteer', 505)
	PALOALTO_NETWORKS = ValueID('PaloAlto Networks', 264)
	PANASAS = ValueID('Panasas', 22)
	PANASONIC = ValueID('Panasonic', 265)
	PANDUIT = ValueID('Panduit', 42)
	PANJA = ValueID('Panja', 402)
	PARADYNE = ValueID('PARADYNE', 121)
	PARAGON = ValueID('Paragon', 403)
	PDI = ValueID('PDI', 83)
	PEAVEY = ValueID('Peavey', 404)
	PENTAIR = ValueID('Pentair', 156)
	PERFORMANCE_5 = ValueID('Performance 5', 405)
	PERLE = ValueID('Perle', 532)
	PERMAPLUG = ValueID('Permaplug', 406)
	PHILLIPS = ValueID('Phillips', 266)
	PHONETICS = ValueID('Phonetics', 407)
	PICO = ValueID('Pico', 408)
	PIVOT3 = ValueID('Pivot3', 409)
	PLASMON = ValueID('Plasmon', 267)
	PLEXTOR = ValueID('Plextor', 506)
	POGO_LINUX = ValueID('Pogo Linux', 84)
	POLYCOM = ValueID('Polycom', 268)
	POLYTRON = ValueID('Polytron', 410)
	POWER_ONE = ValueID('Power-One', 411)
	POWERVAR = ValueID('Powervar', 412)
	PRACTICAL_PERIPHERALS = ValueID('Practical Peripherals', 413)
	PROMISE_TECHNOLOGY = ValueID('Promise Technology', 269)
	PSSC_LABS = ValueID('PSSC Labs', 524)
	PTT = ValueID('PTT', 414)
	PURESTORAGE = ValueID('PureStorage', 535)
	Q1_LABS = ValueID('Q1 Labs', 525)
	QLOGIC = ValueID('Qlogic', 507)
	QUALIS = ValueID('Qualis', 526)
	QUALISYS = ValueID('Qualisys', 270)
	QUANTUM = ValueID('Quantum', 39)
	RACAL_DATACOM = ValueID('Racal-Datacom', 271)
	RAD = ValueID('RAD', 415)
	RADIANCE = ValueID('Radiance', 416)
	RADWARE = ValueID('Radware', 71)
	RARITAN = ValueID('Raritan', 61)
	REDLINE_NETWORKS = ValueID('Redline Networks', 122)
	RELIABLE_COMMUNICATIONS = ValueID('Reliable Communications', 272)
	REXTRON = ValueID('Rextron', 417)
	RF_MOTE = ValueID('RF Mote', 123)
	RICHPAC = ValueID('RICHPAC', 418)
	RITTAL = ValueID('Rittal', 9)
	RIVERBED = ValueID('Riverbed', 41)
	ROSE = ValueID('Rose', 419)
	RSA = ValueID('RSA', 124)
	SABINE = ValueID('Sabine', 420)
	SAFENET = ValueID('SafeNet', 273)
	SAGEMCOM = ValueID('Sagemcom', 421)
	SAMSUNG = ValueID('Samsung', 274)
	SANDVINE = ValueID('Sandvine', 441)
	SCANNEX = ValueID('Scannex', 422)
	SCHLAGE = ValueID('Schlage', 44)
	SCHMID = ValueID('Schmid', 275)
	SCHROFF = ValueID('Schroff', 157)
	SCHROFFTECH = ValueID('Schrofftech', 547)
	SCIENTIFIC_ATLANTA = ValueID('Scientific Atlanta', 276)
	SDS = ValueID('SDS', 125)
	SEAGATE = ValueID('Seagate', 423)
	SECURE_COMPUTING = ValueID('Secure Computing', 40)
	SERVER_TECHNOLOGY = ValueID('Server Technology', 25)
	SEVONE = ValueID('SevOne', 527)
	SHARKRACK = ValueID('SharkRack', 11)
	SHIVA = ValueID('Shiva', 424)
	SHOREMICRO = ValueID('ShoreMicro', 277)
	SHORETEL = ValueID('ShoreTel', 467)
	SIECOR = ValueID('Siecor', 425)
	SIEMENS = ValueID('Siemens', 158)
	SIGNAMAX = ValueID('SignaMax', 508)
	SIMCLAIR = ValueID('Simclair', 426)
	SINGTEL = ValueID('SingTel', 427)
	SL_WABER = ValueID('SL-WABER', 428)
	SMC = ValueID('SMC', 77)
	SONICWALL = ValueID('SonicWALL', 278)
	SONNET_TECHNOLOGIES = ValueID('Sonnet Technologies', 530)
	SONUS_NETWORKS = ValueID('Sonus Networks', 442)
	SONY = ValueID('SONY', 429)
	SOUNDTECH = ValueID('SoundTech', 430)
	SPECTRACOMM = ValueID('SpectraComm', 126)
	SPECTRA_LOGIC = ValueID('Spectra Logic', 6)
	SPECTRUM_POWER = ValueID('Spectrum Power', 279)
	SPIRENT = ValueID('Spirent', 137)
	SPRINT = ValueID('Sprint', 280)
	STEREN = ValueID('Steren', 431)
	STK = ValueID('STK', 432)
	STRATUS = ValueID('Stratus', 542)
	STRONGMAIL = ValueID('StrongMail', 433)
	SUN_MICROSYSTEMS = ValueID('Sun Microsystems', 7)
	SUPERIOR = ValueID('Superior', 509)
	SUPERMICRO = ValueID('Supermicro', 70)
	SURECOM = ValueID('Surecom', 281)
	SUR_GARD = ValueID('Sur-Gard', 543)
	SYMANTEC = ValueID('Symantec', 510)
	SYMMETRICOM = ValueID('Symmetricom', 443)
	SYNOLOGY = ValueID('Synology', 282)
	SYSTIMAX = ValueID('Systimax', 49)
	TANDBERG = ValueID('Tandberg', 127)
	TDK = ValueID('TDK', 511)
	TDK_LAMBDA = ValueID('TDK-Lambda', 468)
	TEGILE = ValueID('Tegile', 536)
	TEKTRONIX = ValueID('Tektronix', 469)
	TELECT = ValueID('Telect', 128)
	TELEGAERTNER = ValueID('Telegaertner', 67)
	TELINDUS = ValueID('Telindus', 283)
	TELTRONICS = ValueID('Teltronics', 129)
	TENABLE = ValueID('Tenable', 531)
	TERADATA = ValueID('Teradata', 444)
	TEROS = ValueID('Teros', 130)
	THALES = ValueID('Thales', 470)
	THERMALTAKE = ValueID('ThermalTake', 284)
	THE_SIEMON_COMPANY = ValueID('The Siemon Company', 13)
	TIMING_SOLUTIONS = ValueID('Timing Solutions', 512)
	TINTRI = ValueID('Tintri', 471)
	TIPPING_POINT = ValueID('Tipping Point', 285)
	TRANSITION_NETWORKS = ValueID('Transition Networks', 513)
	TRANSMODE = ValueID('Transmode', 286)
	TREND_MICRO = ValueID('Trend Micro', 287)
	TRENDNET = ValueID('TrendNet', 514)
	TRIPP_LITE = ValueID('Tripp Lite', 131)
	TRIPWIRE = ValueID('Tripwire', 472)
	TRUSTWAVE = ValueID('Trustwave', 288)
	ULTRAK = ValueID('Ultrak', 289)
	UNIPRISE = ValueID('Uniprise', 73)
	UNISYS = ValueID('Unisys', 290)
	UNITED_POWER = ValueID('United Power', 515)
	UNITRENDS = ValueID('Unitrends', 516)
	UNIVERSAL_ELECTRIC_CORPORATION = ValueID('Universal Electric Corporation', 53)
	UNIVERSITY_SOUND = ValueID('University Sound', 132)
	UPLOGIX = ValueID('Uplogix', 291)
	UPTIME_DEVICES = ValueID('Uptime Devices', 292)
	USROBOTICS = ValueID('USRobotics', 133)
	VA = ValueID('VA', 517)
	VA_LINUX = ValueID('VA Linux', 473)
	VERARI = ValueID('Verari', 48)
	VERILINK = ValueID('Verilink', 293)
	VIASAT = ValueID('ViaSat', 518)
	VICON = ValueID('Vicon', 519)
	VIDYO = ValueID('Vidyo', 159)
	VIEWSONIC = ValueID('ViewSonic', 134)
	VIRTUAL_INSTRUMENTS = ValueID('Virtual Instruments', 445)
	VISARA = ValueID('Visara', 294)
	VISIONMAN = ValueID('Visionman', 474)
	VISUAL_NETWORKS = ValueID('Visual Networks', 295)
	VOLTAIRE = ValueID('Voltaire', 69)
	VSCOM = ValueID('Vscom', 475)
	VSS_MONITORING = ValueID('VSS Monitoring', 68)
	WATCHGUARD = ValueID('Watchguard', 296)
	WESTEL = ValueID('Westel', 297)
	WESTERN_DIGITAL = ValueID('Western Digital', 520)
	WINLAND_ELECTRONICS = ValueID('Winland Electronics', 298)
	WIREMOLD = ValueID('Wiremold', 299)
	WRIGHTLINE = ValueID('Wrightline', 76)
	WRIGHT_LINE = ValueID('Wright Line', 28)
	WTI = ValueID('WTI', 300)
	XEROX = ValueID('Xerox', 301)
	XIOTECH = ValueID('Xiotech', 302)
	ZPE_SYSTEMS = ValueID('ZPE Systems', 545)
	ZYXEL = ValueID('Zyxel', 303)


class ProjectNumber:
	DCTRACK_3_0_GA386 = ValueID('dcTrack 3.0 GA386', 1)
	DGS_PROJ1 = ValueID('DGS-PROJ1', 2)
	RN2011_0001 = ValueID('RN2011-0001', 3)
	RN2011_0002 = ValueID('RN2011-0002', 4)
	RN2012_0001 = ValueID('RN2012-0001', 5)
	RN2014_0001 = ValueID('RN2014-0001', 6)


