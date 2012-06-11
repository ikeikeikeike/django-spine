import os
from django.core.management.base import CommandError
from subcommand.management.generate import GenerateSubCommand

class Command(GenerateSubCommand):

    help = ("General options: ")

    def usage(self, subcommand):
        usage = '%prog {0} {1} APP [options] {2}'.format(
            subcommand, self.usercommand, self.args)
        if self.help:
            return '{0}\n\n{1}'.format(usage, self.help)
        return usage

    def handle_generate(self, *args, **options):
        if not os.path.exists(os.path.join(self.app_dir, "static", "js")):
            raise CommandError(
                "Please run the below for generate static (script) root.\n\n"
                "    $ mkdir -p {0}/static/js\n".format(self.app_dir))

        src = os.path.join(self.app_dir, "static", "js", self.app_name)

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
