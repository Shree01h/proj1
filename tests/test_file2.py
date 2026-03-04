from folder1.file2 import process_data, calculate

def test_process_data():
    assert "ABC value" in process_data()

def test_calculate():
    assert calculate() == 200
