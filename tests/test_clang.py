from djudge.clang import Clang


def test_compile():
    Clang.compile('int main() {return 0;}')