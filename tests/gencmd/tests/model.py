from spine.management.commands.generate import model
from .base import TestSpineBase


class TestSpineModel(TestSpineBase):

    def setUp(self):
        super(TestSpineModel, self).setUp()
        self.new_setUp()

    def tearDown(self):
        super(TestSpineModel, self).tearDown()
        self.new_tearDown()

    def test_exit(self):
        command = model.Command()
        self.assertRaises(
            SystemExit,
            command.execute,
            "ExceptionTest",
#            stdout=self.stdout,
#            stderr=self.stderr
        )

    def test_model(self):
        command = model.Command()
        self.assertRaises(
            SystemExit,
            command.execute,
            "gencmd", "classname",
#            stdout=self.stdout,
#            stderr=self.stderr
        )




