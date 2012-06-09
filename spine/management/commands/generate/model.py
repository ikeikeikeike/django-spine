import os
from optparse import make_option

from ...generate import ModelCommand


class Command(ModelCommand):

    help = ("General options: ")

    def handle_model(self, *args, **options):
        src = os.path.join(self.app_dir, "static", "js", self.app_name)

        self.template("model/model.coffee", os.path.join(
            src, "models", "{0}.{1}".format(self.class_name, "coffee")))

        self.run()
