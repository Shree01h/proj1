from folder1.file1 import abc, helper

def process_data():
    """This function uses file1's abc function"""
    result = abc()
    return f"Processed: {result}"

def calculate():
    return helper() * 2
