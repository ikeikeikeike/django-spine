import re
import os
import eco

from django.core.exceptions import SuspiciousOperation
from pipeline.compilers import (
    CompilerBase,
    CompilerError
)


class EcoCompiler(CompilerBase):
    output_extension = 'js'

    def match_file(self, filename, **kwargs):
        return filename.endswith('.eco')

    def compile_file(self, infile, outfile, outdated=False, force=False, **kwargs):
        if not outdated and not force:
            return
        str_ = u'(function() {{\n  this.JST || (this.JST = {{}});\n  this.JST["{0}"] = {1};\n \n}}).call(this);  '

        content = self.read_file(self._storage_path(infile))
        compiled_content = str_.format(self._template_name(infile), eco.compile(content))
        self.save_file(self._storage_path(outfile), compiled_content)

    def _template_name(self, infile):
        p = infile.split("/")[::-1]
        return os.path.join(p[3], p[2], p[1], p[0].split(".")[0])

    def _storage_path(self, infile):
        try:
            if self.storage.exists(infile) is False:
                raise CompilerError(infile)
            return infile
        except SuspiciousOperation:
            return re.sub("^.+{0}".format(self.storage.base_url), "", infile)