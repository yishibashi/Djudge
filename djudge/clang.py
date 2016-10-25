import tempfile

from djudge.exceptions import CompileError
from djudge.runner import Runner


class Clang:
    @staticmethod
    def compile(code: str) -> Runner:
        with tempfile.NamedTemporaryFile(suffix='.cpp') as src:
            src.write(code)
            print(src.name)

        raise CompileError("""dummy.cpp:5:25: error: expected ';' after expression
  std::cout << std::endl
                        ^
                        ;
1 error generated.""")
