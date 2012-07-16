import os
from spine.management.commands.generate import new
from .base import TestSpineBase


class TestSpineNew(TestSpineBase):

    def test_exit(self):
        """ exception test """
        command = new.Command()
        self.assertRaises(
            SystemExit,
            command.execute,
            "ExceptionTest",
#            stdout=self.stdout,
#            stderr=self.stderr
        )

    def test_new(self):
        self.new_setUp()

        self.assertTrue(os.path.exists(os.path.join(self.app_dir, "static")))
        self.assertTrue(os.path.exists(os.path.join(self.app_dir, "static", "js")))

        src = os.path.join(self.app_dir, "static", "js", "gencmd")

#        self.assertTrue(os.path.exists(src))
#
#        self.assertTrue(os.path.exists(os.path.join(src, "models")))
#        self.assertTrue(os.path.exists(os.path.join(src, "models/.keep")))
#
#        self.assertTrue(os.path.exists(os.path.join(src, "views")))
#        self.assertTrue(os.path.exists(os.path.join(src, "views/.keep")))
#
#        self.assertTrue(os.path.exists(os.path.join(src, "controllers")))
#        self.assertTrue(os.path.exists(os.path.join(src, "controllers/.keep")))
#
#        self.assertTrue(os.path.exists(os.path.join(src, "lib")))
#        self.assertTrue(os.path.exists(os.path.join(src, "lib/.keep")))
#
#        self.assertTrue(os.path.exists(os.path.join(src, "index.coffee")))
#        self.assertTrue(os.path.exists(os.path.join(src, "lib/view.coffee")))

        self.new_tearDown()


