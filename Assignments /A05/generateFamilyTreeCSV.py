import pandas as pd
import numpy as np
import random

# Initial people data
people_data = {'id': list(range(1, 51)),
    'first_name': ['Curry', 'Jessica', 'Tracey', 'Bobine', 'Andreana', 'Daryle', 'Putnam', 'Arabel', 'Anet', 'Arvy', 'Carmella', 'Nikolas', 'Pavla', 'Lucilia', 'Baryram', 'Adi', 'Shane', 'Oliviero', 'Hallie', 'Rose', 'Misti', 'Noel', 'Melina', 'Robb', 'Corella', 'Fanechka', 'Granville', 'Casar', 'Rayshell', 'Nicoli', 'Felizio', 'Amery', 'Joey', 'Bryn', 'Samuel', 'Shirley', 'Roshelle', 'Mufi', 'Brennan', 'Linnell', 'Noellyn', 'Roy', 'Darill', 'Verile', 'Bernadina', 'Miran', 'Marc', 'Vincenty', 'Fowler', 'Gordie'],
    'last_name': ['Andrat', 'Colpus', 'Libero', 'Gioan', 'Fontes', 'Fermor', 'Bensley', 'Southcott', 'Matijasevic', 'Tash', 'Leese', 'Ilyasov', 'Errichelli', 'Alty', 'Brixey', 'Risbrough', 'Beggs', 'Klulik', 'Shales', 'Favey', 'Scarrott', 'Matzen', 'Audas', 'Parratt', 'Martynikhin', 'Weatherhill', 'Fiorentino', 'Massen', 'Syms', 'MacLice', 'Loiterton', 'Proffer', 'Paoli', 'Pentland', 'Burtonshaw', 'Navarre', 'Ingleston', 'Finey', 'Ortega', 'Hunstone', 'Perotti', 'Deeley', 'Dumbrall', 'Degue', 'Alyokhin', 'Woodruff', 'Goslin', 'Lowcock', 'Sparkes', 'Newbatt'],
    'gender': ['Male', 'Female', 'Female', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Female', 'Female', 'Female', 'Female', 'Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Female', 'Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female', 'Female', 'Male', 'Male', 'Male', 'Male']}

# Add initial None values for mother_id, father_id, spouse_id
people_data['mother_id'] = [None]*50
people_data['father_id'] = [None]*50
people_data['spouse_id'] = [None]*50

# Clans
clans = ['Abe', 'Akira', 'Aoki', 'Ashenfire', 'Ashenmourn', 'Blacksteel', 'Blackthistle', 'Bladeflame', 'Bloodmoon', 'Bloodrune', 'Chiba', 'Darkfire', 'Dragonbane', 'Dragonfire', 'Dreadstorm', 'Dreadthorn']

# Function to assign clans
def assign_clans(df, clans):
    df['clan'] = np.random.choice(clans, size=len(df))
    return df

# Function to assign birth years to initial data
def assign_birth_years(df, start_year, end_year):
    df['birthYear'] = np.random.randint(start_year, end_year, size=len(df))
    return df

# Function to assign death years to initial data
def assign_death_years(df, end_year):
    df['deathYear'] = df['birthYear'].apply(lambda x: np.random.randint(x, end_year))
    return df

# Function to form couples in initial data
def form_couples(df, num_couples):
    potential_partners = df[df.spouse_id.isna()].copy()
    males = potential_partners[potential_partners.gender == 'Male']
    females = potential_partners[potential_partners.gender == 'Female']
    for i in range(min(num_couples, min(len(males), len(females)))):
        male_id = males.iloc[i]['id']
        female_id = females.iloc[i]['id']
        df.loc[df.id == male_id, 'spouse_id'] = female_id
        df.loc[df.id == female_id, 'spouse_id'] = male_id
    return df

# Function to generate children
def generate_children(df, start_id, num_generations, start_year, end_year):
    for gen in range(num_generations):
        children = []
        for i, row in df.iterrows():
            if pd.notnull(row.spouse_id) and row['gender'] == 'Female': # Check if the person is married and is female
                num_children = np.random.randint(0,2) # Number of children for the couple
                for _ in range(num_children):
                    child = {}
                    child['id'] = start_id
                    child['first_name'] = np.random.choice(df['first_name']) # Child's name taken from given names
                    child['last_name'] = row['last_name'] # Child takes the mother's last name
                    child['gender'] = np.random.choice(['Male', 'Female'])
                    child['birthYear'] = np.random.randint(start_year, end_year) # Birth year is within the generation's range
                    child['deathYear'] = np.random.randint(child['birthYear'], end_year + gen * 20) # Death year is after birth year and before present year
                    child['mother_id'] = row['id']
                    child['father_id'] = row['spouse_id']
                    child['spouse_id'] = None
                    child['clan'] = row['clan'] # Child is assigned the clan of the parents
                    children.append(child)
                    start_id += 1
        children_df = pd.DataFrame(children)
        df = pd.concat([df, children_df], ignore_index=True) # Append children dataframe to main dataframe
        df = form_couples(df, int(len(df) / 10)) # Form couples for the next generation (10% of the population forms couples)
        
        # Update the range of birth years for the next generation
        start_year = end_year
        end_year += 20
        
    return df


# Create DataFrame from initial data
df = pd.DataFrame(people_data)

# Assign clans to initial data
df = assign_clans(df, clans)

# Assign birth years to initial data
df = assign_birth_years(df, start_year=1750, end_year=1770)

# Assign death years to initial data
df = assign_death_years(df, end_year=1820)

# Form couples in initial data
df = form_couples(df, num_couples=1)

# Generate children for 8 generations
df = generate_children(df, start_id=51, num_generations=7, start_year=1770, end_year=1790)

# Save the DataFrame to a CSV file
df.to_csv('family_tree.csv', index=False)


