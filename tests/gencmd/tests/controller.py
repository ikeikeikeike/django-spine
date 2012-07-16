from spine.management.commands.generate import controller
from .base import TestSpineBase


class TestSpineController(TestSpineBase):

    def setUp(self):
        super(TestSpineController, self).setUp()
        self.new_setUp()

    def tearDown(self):
        super(TestSpineController, self).tearDown()
        self.new_tearDown()

    def test_exit(self):
        command = controller.Command()
        self.assertRaises(
            SystemExit,
            command.execute,
            "ExceptionTest",
#            stdout=self.stdout,
#            stderr=self.stderr
        )

    def test_controller(self):
        command = controller.Command()
        self.assertRaises(
            SystemExit,
            command.execute,
            "gencmd", "classname",
#            stdout=self.stdout,
#            stderr=self.stderr
        )



