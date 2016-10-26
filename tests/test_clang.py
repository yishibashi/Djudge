import pytest

from djudge.clang import Clang
from djudge.exceptions import CompileError


def test_compile():
    Clang.compile('int main() {return 0;}')


def test_compile_with_wrong_code():
    with pytest.raises(CompileError):
        Clang.compile('clang')
