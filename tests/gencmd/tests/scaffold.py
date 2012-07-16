from spine.management.commands.generate import scaffold
from .base import TestSpineBase


class TestSpineScaffold(TestSpineBase):

    def setUp(self):
        super(TestSpineScaffold, self).setUp()
        self.new_setUp()

    def tearDown(self):
        super(TestSpineScaffold, self).tearDown()
        self.new_tearDown()

    def test_exit(self):
        command = scaffold.Command()
        self.assertRaises(
            SystemExit,
            command.execute,
            "ExceptionTest",
#            stdout=self.stdout,
#            stderr=self.stderr
        )

    def test_scaffold(self):
        command = scaffold.Command()
        self.assertRaises(
            SystemExit,
            command.execute,
            "gencmd", "classname",
#            stdout=self.stdout,
#            stderr=self.stderr
        )




