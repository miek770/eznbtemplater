from pkg.pkg import main


def test_main_hello():
    assert main("Michel") == "Hello Michel!"
