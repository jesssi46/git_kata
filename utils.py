import pandas as pd

def load_titanic_men(filepath):
    # Pfade und Dateinamen entsprechend anpassen
    titanic_data = pd.read_csv(filepath)
    men_passengers = titanic_data[titanic_data['sex'] == 'male']
    return men_passengers

