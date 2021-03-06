from unittest import TestCase, main
from os import chdir, getcwd
from shutil import copytree, rmtree
from unittest.mock import patch

from self import main as grader_main
from lib.runner import execute
from lib.system import EXITCODE_IOERROR
from tests.utils import CaptureOutput

dst = '/tmp/sel fie'


class TestRobustness(TestCase):

    def setUp(self):
        rmtree(dst, ignore_errors=True)

    def execute_mock(self, command):
        ret_code, output, error_output = execute(command)

        self.assertNotEqual(ret_code, EXITCODE_IOERROR)

        return (ret_code, output, error_output)

    def insert_assignment_path(self, command):
        return command.replace("<assignment>", "grader/assignments/hex-literal/")

    @patch('lib.runner.execute')
    def test_path_name_with_whitespaces(self, mock):
        mock.side_effect = self.execute_mock

        copytree('..', dst)

        cwd = getcwd()

        chdir(dst)

        with CaptureOutput(), patch('lib.runner.insert_assignment_path') as assignment_path_mock:
            assignment_path_mock.side_effect = self.insert_assignment_path

            grader_main([getcwd(), 'hex-literal'])

        chdir(cwd)

        rmtree(dst)

    def tearDown(self):
        rmtree(dst, ignore_errors=True)


if __name__ == '__main__':
    main()
