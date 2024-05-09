import pandas as pd

def load_titanic_female(filepath):
    # Pfade und Dateinamen entsprechend anpassen
    titanic_data = pd.read_csv(filepath)
    female_passengers = titanic_data[titanic_data['sex'] == 'female']
    return female_passengers

