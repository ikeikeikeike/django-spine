import os
import eco
from pipeline.compilers import CompilerBase


class EcoCompiler(CompilerBase):
    output_extension = 'js'

    def match_file(self, filename, **kwargs):
        return filename.endswith('.eco')

    def compile_file(self, content, path, **kwargs):
        p = path.split("/")[::-1]
        return u'(function() {\n  this.JST || (this.JST = {});\n  \
                this.JST["%s"] = %s;\n \n}).call(this);  ' % (
                    os.path.join(p[3], p[2], p[1], p[0].split(".")[0]), eco.compile(content)
                )
