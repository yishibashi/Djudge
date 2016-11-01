import os
import subprocess

from djudge.exceptions import RunnerError


class Runner:
    def __init__(self, cmd: str, delete=True, timeout=None, memory=None):
        if not os.path.isfile(cmd):
            raise ValueError('cmd {:s} must be file.'.format(cmd))

        self._cmd = cmd
        self.delete = delete
        self.timeout = timeout
        self.memory = memory  # ToDo: memory limit

    def __exit__(self):
        if self.delete:
            # ToDo: Catch exception if the file is not found.
            os.remove(self._cmd)

    def run(self, stdin='', stdout='') -> bool:
        try:
            result = subprocess.run([self._cmd], timeout=self.timeout, stdout=subprocess.PIPE, input=stdin, universal_newlines=True)
            return result.stdout == stdout
        except subprocess.TimeoutExpired:
            raise RunnerError('execution time is over limit > {:d}'.format(self.timeout))
        except Exception as e:
            # ToDo: check another exceptions that subprocess raises
            raise e
