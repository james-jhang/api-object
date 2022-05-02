import pytest
# from apiobject.lookup.modelFields import *
from apiobject.lookup.fields import AssignmentLevel, Class, SoltType
from apiobject.part.part import PartsManagement
from apiobject.part.part_class import PartClass, PartClassDAO
from apiobject.part.part_model import PartModel, PartModelDAO
# from apiobject.lookup.subtabs import *
# from apiobject.part.part import *
# from apiobject.item.item import *
from apiobject.user.user import Administrator


@pytest.fixture
def admin():
    host = '192.168.1.18'
    admin = Administrator(host, 'admin', 'Lab1321*')
    admin.login()
    yield admin

class TestPart:

    def test_part_class(self, admin):
        parts_management = PartsManagement(user=admin)
        parts_management.enable_parts_management()
        dao = PartClassDAO(user=admin)
        part_class = dao.create(
            class_label='Test Part Class',
            assignment_level=AssignmentLevel.DATA_PANEL_PORT,
            classes=[Class.CABINET]
        )
        assert part_class.class_label == 'Test Part Class'
        assert part_class.assignment_level == AssignmentLevel.DATA_PANEL_PORT.value
        assert part_class.classes == [Class.CABINET.value]

        # teardown
        dao.delete(part_class)
        parts_management.disable_parts_management()

    def test_part_model(self, admin):
        parts_management = PartsManagement(user=admin)
        parts_management.enable_parts_management()
        part_class_dao = PartClassDAO(user=admin)
        part_class = part_class_dao.create(
            class_label='Test Part Class',
            assignment_level=AssignmentLevel.DATA_PANEL_PORT,
            classes=[Class.CABINET]
        )
        part_model_dao = PartModelDAO(user=admin)
        part_model = part_model_dao.create(
            'Test Part Class',
            '3Com',
            'Test Part',
            'TEST_123',
            SoltType.CPU_SOCKET
        )
        assert part_model.make == '3Com'
        assert part_model.name == 'Test Part'
        assert part_model._class == 'Test Part Class'
        assert part_model.part_number == 'TEST_123'
        assert part_model.slot_type == SoltType.CPU_SOCKET.value

        # teardown
        part_model_dao.delete(part_model)
        part_class_dao.delete(part_class)
        parts_management.disable_parts_management()

    # def test_part_model_with_image(self, admin):
    #     parts_management = PartsManagement(user=admin)
    #     parts_management.enable_parts_management()
    #     part_class = PartClass(user=admin)
    #     part_class.create(
    #         class_label='Test Part Class',
    #         assignment_level=AssignmentLevel.DATA_PANEL_PORT,
    #         classes=[Class.CABINET]
    #     )
    #     part_model = PartModel(user=admin)
    #     image = Image(user=admin)
    #     image.upload(".\\tests\\1.PNG")
    #     part_model.create(part_class, '3Com', 'Test Part', 'TEST_123', SoltType.CPU_SOCKET, image=image)

    #     # teardown
    #     part_model.delete()
    #     part_class.delete()
    #     parts_management.disable_parts_management()

    # def test_part(self, admin):
    #     parts_management = PartsManagement(user=admin)
    #     parts_management.enable_parts_management()
    #     part_class = PartClass(user=admin)
    #     part_class.create(
    #         class_label='Test Part Class',
    #         assignment_level=AssignmentLevel.DATA_PANEL_PORT,
    #         classes=[Class.CABINET]
    #     )
    #     part_model = PartModel(user=admin)
    #     part_model.create(part_class, '3Com', 'Test Part Model', 'TEST_456', SoltType.CPU_SOCKET)

    #     part = Part(user=admin)
    #     part.create(
    #         part_model, '911 Enable', 'Test Part', PartStatus.IN_STOCK, Location.ACDC, TrackingType.COLLECTIVELY,
    #         8, 2, 7
    #     )

    #     # teardown
    #     part.delete()
    #     part_model.delete()
    #     part_class.delete()
    #     parts_management.disable_parts_management()

    # def test_part_custom_field(self, admin):
    #     parts_management = PartsManagement(user=admin)
    #     parts_management.enable_parts_management()
    #     part_custom_field = CustomField(user=admin)
    #     part_custom_field.create('Test Custom Field', 'Part', PartClassField.DAUGHTER_BOARD, CustomFieldDataType.TEXT, True)

    #     # teardown
    #     part_custom_field.delete()
    #     parts_management.disable_parts_management()

    # def test_part_subtab(self, admin):
    #     parts_management = PartsManagement(user=admin)
    #     parts_management.enable_parts_management()
    #     panel = Panel(user=admin)
    #     panel.create(Subtabs.CUSTOM_FIELDS_PART, 'Test Panel')

    #     # teardown
    #     panel.delete()
    #     parts_management.disable_parts_management()

    # def test_part_assign_item(self, admin):
    #     parts_management = PartsManagement(user=admin)
    #     parts_management.enable_parts_management()
    #     part_class = PartClass(user=admin)
    #     part_class.get("CPU")
    #     part_model = PartModel(user=admin)
    #     part_model.create(part_class, '3Com', 'Test Part Model', 'TEST_456', SoltType.CPU_SOCKET)

    #     part = Part(user=admin)
    #     part.create(
    #         part_model, '911 Enable', 'Test Part', PartStatus.IN_STOCK, Location.SITE_A, TrackingType.COLLECTIVELY,
    #         8, 2, 7
    #     )
    #     item = Item(user=admin)
    #     item.create(item_name='Test Item', make=Make.HP, model=Model.BLADE_SYSTEM_C7000, status=ItemStatus.PLANNED, location=Location.SITE_A)
    #     part.assign_to_item(item, quantity='1', reason='reason', tracking_number='123')

    #     #teardown
    #     part.unassign_from_item(item)
    #     item.delete()
    #     part.delete()
    #     part_model.delete()
    #     parts_management.enable_parts_management()
