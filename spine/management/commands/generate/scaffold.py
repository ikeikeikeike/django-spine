import os
# from optparse import make_option

from ...generate import ScaffoldCommand


class Command(ScaffoldCommand):

    help = ("General options: ")

    def handle_scaffold(self, *args, **options):
        src = os.path.join(self.app_dir, "static", "js", self.app_name)

        self.template("model/model.coffee", os.path.join(
            src, "models", "{0}.{1}".format(self.class_name, "coffee")))
        self.template("scaffold/controller.coffee", os.path.join(
            src, "controllers",
            "{0}.{1}".format(self.inflect.pluralize(self.class_name), "coffee")))

        pluralize = self.inflect.pluralize(self.app_name)
        self.empty_directory(os.path.join(src, "views", pluralize))
        self.template("scaffold/edit.jst", os.path.join(src, "views", pluralize, "edit.jst.eco"))
        self.template("scaffold/index.jst", os.path.join(src, "views", pluralize, "index.jst.eco"))
        self.template("scaffold/new.jst", os.path.join(src, "views", pluralize, "new.jst.eco"))
        self.template("scaffold/show.jst", os.path.join(src, "views", pluralize, "show.jst.eco"))

        self.run()
