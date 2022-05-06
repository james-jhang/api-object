import pytest
from apiobject.custom_field import CustomFieldDAO
# from apiobject.lookup.modelFields import *
from apiobject.lookup.fields import *
from apiobject.part import PartsManagement
from apiobject.part.part import Part, PartDAO
from apiobject.part.part_class import PartClass, PartClassDAO
from apiobject.part.part_model import PartModel, PartModelDAO
# from apiobject.lookup.subtabs import *
# from apiobject.part.part import *
# from apiobject.item.item import *
from apiobject.user.user import Administrator

from .utils import compare, certificate


@pytest.fixture
def admin():
    admin = Administrator(*certificate())
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

    def test_part_model_with_image(self, admin):
        parts_management = PartsManagement(user=admin)
        parts_management.enable_parts_management()
        part_class_dao = PartClassDAO(user=admin)
        part_class = part_class_dao.create(
            class_label='Test Part Class',
            assignment_level=AssignmentLevel.DATA_PANEL_PORT,
            classes=[Class.CABINET]
        )
        part_model_dao = PartModelDAO(user=admin)
        image_url = part_model_dao.upload(".\\tests\\1.PNG")

        part_model = part_model_dao.create(
            'Test Part Class',
            '3Com',
            'Test Part',
            'TEST_123',
            SoltType.CPU_SOCKET,
            image=image_url
        )

        assert f'{part_model.id}_part.PNG'.lower() in part_model.image.lower()

        # teardown
        part_model_dao.delete(part_model)
        part_class_dao.delete(part_class)
        parts_management.disable_parts_management()

    def test_part(self, admin):
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
            'TEST_456',
            SoltType.CPU_SOCKET
        )

        part_dao = PartDAO(user=admin)
        part = part_dao.create(
            part_model.name,
            part_model.make,
            PartStatus.IN_STOCK,
            'SITE A',
            TrackingType.COLLECTIVELY,
            batch_number=8,
            count_in_stock=7,
            count_in_use=2,
        )

        assert part.make == part_model.make
        assert part.model == part_model.name
        assert part.part_number == part_model.part_number
        assert part.count_in_stock == 7
        assert part.count_in_use == 2
        assert part.status == PartStatus.IN_STOCK.value
        assert part.location == 'SITE A'
        assert part.tracking_type == TrackingType.COLLECTIVELY.value
        assert part.threshold == 0

        # teardown
        part_dao.delete(part)
        part_model_dao.delete(part_model)
        part_class_dao.delete(part_class)
        parts_management.disable_parts_management()

    def test_part_custom_field(self, admin):
        parts_management = PartsManagement(user=admin)
        parts_management.enable_parts_management()
        custom_field_dao = CustomFieldDAO(user=admin)
        custom_field = custom_field_dao.create_custom_field(
            label='Test Custom Field',
            appliesTo=[SubtabType.PART, SubtabType.ITEM],
            fieldType=CustomFieldDataType.TEXT,
            classes=[Class.DATA_PANEL],
            subclasses=[Subclass.BLADE],
            partClasses=[PartClassField.DAUGHTER_BOARD],
            applyToModels=True
        )

        assert custom_field.label == 'Test Custom Field'
        assert custom_field._type.lower() == CustomFieldDataType.TEXT.value.lower()
        compare(custom_field.apply_to, [SubtabType.PART.value, SubtabType.ITEM.value])
        compare(custom_field.classes, [Class.DATA_PANEL.value])
        compare(custom_field.subclasses, [Subclass.BLADE.value])
        compare(custom_field.part_classes, [PartClassField.DAUGHTER_BOARD.value])
        assert custom_field.apply_to_models == True

        # teardown
        custom_field_dao.delete_custom_field(custom_field)
        parts_management.disable_parts_management()

    def test_part_subtab(self, admin):
        parts_management = PartsManagement(user=admin)
        parts_management.enable_parts_management()
        custom_field_dao = CustomFieldDAO(user=admin)
        panel = custom_field_dao.create_panel(
            'Custom Fields',
            'Part',
            'Test Panel'
        )
        assert panel.name == 'Test Panel'
        assert panel.width == 2
        assert panel.height == 3

        # # teardown
        custom_field_dao.delete_panel(panel)
        parts_management.disable_parts_management()

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
