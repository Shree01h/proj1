from folder1.file1 import abc, helper

def test_abc():
    assert abc() == "ABC value"

def test_helper():
    assert helper() == 100
