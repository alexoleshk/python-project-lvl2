from gendiff.scripts.gendiff import generate_diff
import os


def test_generate_diff():
    f = open(os.path.abspath('tests/fixtures/diff12.txt'), 'r')
    text = f.read()
    assert generate_diff(
        os.path.abspath('tests/fixtures/file1.json'),
        os.path.abspath('tests/fixtures/file2.json')
    ) == text
    f.close()
