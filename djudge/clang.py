import tempfile
import subprocess

from djudge.exceptions import CompileError
from djudge.runner import Runner


class Clang:
    @staticmethod
    def compile(code: str) -> Runner:
        with tempfile.NamedTemporaryFile(suffix='.cpp') as src, tempfile.NamedTemporaryFile(delete=False) as cmd:
            src.write(code.encode())
            src.flush()  # ToDo: how to delete src file after compiling?

            try:
                subprocess.run(['clang++', '-std=c++14', '-O2', '-o', cmd.name, src.name], timeout=60, check=True)
                return Runner(cmd.name)
            except subprocess.CalledProcessError as e:
                raise CompileError(e.stderr)
