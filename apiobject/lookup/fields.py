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


class PartStatus:
	BROKEN = ValueID('Broken', 2447)
	LOST = ValueID('Lost', 2448)
	IN_STOCK = ValueID('In Stock', 2463)
	IN_USE = ValueID('In Use', 2464)
	ARCHIVED = ValueID('Archived', 2465)


class Location:
	ACDC = ValueID('ACDC', 41)
	DC_FL_RO = ValueID('DC > FL > RO', 39)
	DGS_CHANGECONTROL = ValueID('DGS-CHANGECONTROL', 40)
	RBAC0 = ValueID('RBAC0', 35)
	RBAC1 = ValueID('RBAC1', 18)
	SITE_A = ValueID('SITE A', 1)
	SITE_B = ValueID('SITE B', 2)
	SITE_C = ValueID('SITE C', 7)
	SITE_COLO = ValueID('SITE COLO', 8)
	SITE_IDF = ValueID('SITE IDF', 6)


