from src.data.clean_data import clean_data

def clean_data_test():
    palabra = clean_data()
    assert palabra == 'melo'