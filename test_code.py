from src.data.clean_data import clean_data

def test_clean_data():
    palabra = clean_data()
    assert palabra == 'melo'