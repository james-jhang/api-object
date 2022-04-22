import pytest

from apiobject.lookup.fields import *
from apiobject.part.part import PartClass, PartModel, Part, Image
from apiobject.user.user import Administrator

@pytest.fixture
def admin():
    host = '192.168.1.18'
    admin = Administrator(host, 'admin', 'Lab1321*')
    admin.login()
    yield admin

class TestPart:

    def test_part_class(self, admin):
        part_class = PartClass(user=admin)
        part_class.create(
            class_label='Test Part Class',
            assignment_level=AssignmentLevel.DATA_PANEL_PORT,
            classes=[Class.CABINET]
        )
        assert part_class.label == 'Test Part Class'
        assert part_class.assignableTo == AssignmentLevel.DATA_PANEL_PORT.pair()
        assert part_class.classesForAssociation == [Class.CABINET.pair()]

        # teardown
        part_class.delete()

    def test_part_model(self, admin):
        part_class = PartClass(user=admin)
        part_class.create(
            class_label='Test Part Class',
            assignment_level=AssignmentLevel.DATA_PANEL_PORT,
            classes=[Class.CABINET]
        )
        part_model = PartModel(user=admin)
        part_model.create(part_class, '3Com', 'Test Part', 'TEST_123', SoltType.CPU_SOCKET)
        #TODO assert

        # teardown
        part_model.delete()
        part_class.delete()

    def test_part_model_with_image(self, admin):
        part_class = PartClass(user=admin)
        part_class.create(
            class_label='Test Part Class',
            assignment_level=AssignmentLevel.DATA_PANEL_PORT,
            classes=[Class.CABINET]
        )
        part_model = PartModel(user=admin)
        image = Image(user=admin)
        image.upload("C:\\Users\\ssl\\Desktop\\1.PNG")
        part_model.create(part_class, '3Com', 'Test Part', 'TEST_123', SoltType.CPU_SOCKET, image=image)

        # teardown
        part_model.delete()
        part_class.delete()

    def test_part(self, admin):
        part_class = PartClass(user=admin)
        part_class.create(
            class_label='Test Part Class',
            assignment_level=AssignmentLevel.DATA_PANEL_PORT,
            classes=[Class.CABINET]
        )
        part_model = PartModel(user=admin)
        part_model.create(part_class, '3Com', 'Test Part Model', 'TEST_456', SoltType.CPU_SOCKET)
        
        part = Part(user=admin)
        part.create(
            part_model, '911 Enable', 'Test Part', PartStatus.IN_STOCK, Location.ACDC, TrackingType.COLLECTIVELY, 
            8, 2, 7
        )

        # teardown
        part.delete()
        part_model.delete()
        part_class.delete()