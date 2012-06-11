import os
from django.core.management.base import CommandError
from subcommand.management.generate import GenerateSubCommand


class Command(GenerateSubCommand):

    help = ("General options: ")

    def usage(self, subcommand):
        usage = '%prog {0} {1} APP NAME [options] {2}'.format(
            subcommand, self.usercommand, self.args)
        if self.help:
            return '{0}\n\n{1}'.format(usage, self.help)
        return usage

    def handle_generate(self, *args, **options):
        src = os.path.join(self.app_dir, "static", "js", self.app_name)
        if not self.class_name:
            raise CommandError("You must provide an class_name.")
        if not os.path.exists(src):
            raise CommandError(
                "Please run the `{0}:new` command before this command.".format(self.package))

        pluralize = self.inflect.pluralize(self.class_name)
        self.template("controller/controller.coffee", os.path.join(
            src, "controllers", "{0}.{1}".format(pluralize, "coffee")))

        self.run()
