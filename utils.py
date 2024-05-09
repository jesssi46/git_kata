import pandas as pd

def load_titanic_female():
    # Pfade und Dateinamen entsprechend anpassen
    titanic_data = pd.read_csv('C:/Users/jessi/Documents/UNI/Master/2. Semester/Enterprise Architectures for Big Data/git_kata/data/titanic.csv')
    female_passengers = titanic_data[titanic_data['Sex'] == 'female']
    return female_passengers

