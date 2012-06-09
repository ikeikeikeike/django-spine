import re
from django.core.management.base import CommandError
from subcommand.management.generate import GenerateSubCommand

fields_ptn = re.compile("^-")


class NewCommand(GenerateSubCommand):

    def handle_generate(self, *args, **options):
        self.handle_new(*args, **options)

    def handle_new(self, *args, **options):
        raise NotImplementedError()


class ScaffoldCommand(GenerateSubCommand):

    def usage(self, subcommand):
        usage = '%prog {0} {1} NAME field1 field2 [options] {2}'.format(
            subcommand, self.usercommand, self.args)
        if self.help:
            return '{0}\n\n{1}'.format(usage, self.help)
        return usage

    def handle_generate(self, *args, **options):
        try:
            class_name = args[1]
        except IndexError:
            raise CommandError("You must provide an class_name.")
        self.class_name = class_name

        self.fields = [arg for arg in args[2:] if not fields_ptn.match(arg)]
        self.handle_scaffold(*args, **options)

    def handle_scaffold(self, *args, **options):
        raise NotImplementedError()


class ControllerCommand(GenerateSubCommand):

    def usage(self, subcommand):
        usage = '%prog {0} {1} NAME [options] {2}'.format(
            subcommand, self.usercommand, self.args)
        if self.help:
            return '{0}\n\n{1}'.format(usage, self.help)
        return usage

    def handle_generate(self, *args, **options):
        try:
            class_name = args[1]
        except IndexError:
            raise CommandError("You must provide an class_name.")
        self.class_name = class_name

        self.handle_controller(*args, **options)

    def handle_controller(self, *args, **options):
        raise NotImplementedError()


class ModelCommand(GenerateSubCommand):

    def usage(self, subcommand):
        usage = '%prog {0} {1} NAME field1 field2 [options] {2}'.format(
            subcommand, self.usercommand, self.args)
        if self.help:
            return '{0}\n\n{1}'.format(usage, self.help)
        return usage

    def handle_generate(self, *args, **options):
        try:
            class_name = args[1]
        except IndexError:
            raise CommandError("You must provide an class_name.")
        self.class_name = class_name

        self.fields = [arg for arg in args[2:] if not fields_ptn.match(arg)]
        self.handle_model(*args, **options)

    def handle_model(self, *args, **options):
        raise NotImplementedError()
