import tempfile
import subprocess

from djudge.exceptions import CompileError
from djudge.runner import Runner


class Clang:
    @staticmethod
    def compile(code: str) -> Runner:
        with tempfile.NamedTemporaryFile(suffix='.cpp', delete=False) as src:
            src.write(code.encode())
            src.close()

            try:
                subprocess.run(['clang++', '-std=c++14', '-O2', src.name], timeout=60, check=True)
            except subprocess.CalledProcessError as e:
                raise CompileError(e.stderr)
