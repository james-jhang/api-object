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


class ProjectNumber:
	DCTRACK_3_0_GA386 = ValueID('dcTrack 3.0 GA386', 1)
	DGS_PROJ1 = ValueID('DGS-PROJ1', 2)
	RN2011_0001 = ValueID('RN2011-0001', 3)
	RN2011_0002 = ValueID('RN2011-0002', 4)
	RN2012_0001 = ValueID('RN2012-0001', 5)
	RN2014_0001 = ValueID('RN2014-0001', 6)


