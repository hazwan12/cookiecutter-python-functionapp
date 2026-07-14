from {{ cookiecutter.package_name }}.sample_function import add


def test_add():
    assert add(2, 3) == 5
