from diff_generator.scripts.gendiff import generate_diff
import os


def test_generate_diff():
    f = open(os.path.abspath('diff_generator/tests/fixtures/diff12.txt'), 'r')
    text = f.read()
    assert generate_diff(
        os.path.abspath('diff_generator/tests/fixtures/file1.json'),
        os.path.abspath('diff_generator/tests/fixtures/file2.json')
    ) + '\n' == text
    f.close()
