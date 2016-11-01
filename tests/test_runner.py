from djudge.clang import Clang


def test_runner():
    assert Clang.compile('''
#include <iostream>
int main()
{
  std::cout << "Hello World!" << std::endl;
  return 0;
}
    ''').run(stdout='Hello World!\n') is True


def test_runner_with_wrong_stdout():
    assert Clang.compile('''
#include <iostream>
int main()
{
  std::cout << "Bye World!" << std::endl;
  return 0;
}
    ''').run(stdout='Hello World!\n') is False
