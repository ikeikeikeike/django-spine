import os
from optparse import make_option

from ...generate import ControllerCommand


class Command(ControllerCommand):

    help = ("General options: ")

    def handle_controller(self, *args, **options):
        pluralize = self.inflect.pluralize(self.class_name)
        src = os.path.join(self.app_dir, "static", "js", self.app_name)

        self.template("controller/controller.coffee", os.path.join(
            src, "controllers", "{0}.{1}".format(pluralize, "coffee")))

        self.run()
