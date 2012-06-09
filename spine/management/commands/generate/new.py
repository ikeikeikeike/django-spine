import os
from optparse import make_option

# from django.conf import settings

from ...generate import NewCommand


class Command(NewCommand):

    help = ("General options: ")

    def handle_new(self, *args, **options):
        src = os.path.join(self.app_dir, "static", "js", self.app_name)

        self.empty_directory(os.path.join(self.app_dir, "static"))
        self.empty_directory(os.path.join(self.app_dir, "static", "js"))
        self.empty_directory(os.path.join(src))

        self.empty_directory(os.path.join(src, "models"))
        self.create_file(os.path.join(src, "models/.keep"))

        self.empty_directory(os.path.join(src, "views"))
        self.create_file(os.path.join(src, "views/.keep"))

        self.empty_directory(os.path.join(src, "controllers"))
        self.create_file(os.path.join(src, "controllers/.keep"))

        self.empty_directory(os.path.join(src, "lib"))
        self.create_file(os.path.join(src, "lib/.keep"))

        self.template("new/index.coffee", os.path.join(src, "index.coffee"))
        self.template("new/view.coffee", os.path.join(src, "lib/view.coffee"))

        self.run()
