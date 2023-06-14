import pandas as pd
from graphviz import Digraph
import random
import numpy as np

def clan_color_mapping(clans):
    # Generate unique random colors for each clan
    colors = ["#"+''.join([random.choice('0123456789ABCDEF') for _ in range(6)]) for _ in range(len(clans))]
    return dict(zip(clans, colors))

def create_family_tree(file_path):
    # Read the family tree data
    df = pd.read_csv(file_path)

    # Create a Digraph object
    g = Digraph('G', filename='family_tree.dot', node_attr={'shape': 'plaintext'})

    clan_colors = clan_color_mapping(df['clan'].unique())

    # Add nodes
    for _, row in df.iterrows():
        # Create label
        label = "<<table><tr><td>{}</td><td bgcolor='{}'>Born: {}</td></tr><tr><td colspan='2'>Died: {}</td></tr><tr><td colspan='2'>Age: {}</td></tr><tr><td colspan='2'>Clan: {}</td></tr></table>>".format(
            row['first_name'] + " " + row['last_name'],
            clan_colors[row['clan']],
            row['birthYear'],
            row['deathYear'],
            row['deathYear'] - row['birthYear'],
            row['clan']
        )


        g.node(str(row['id']), label=label)

    # Add edges
    for _, row in df.iterrows():
        if pd.notnull(row['mother_id']):
            g.edge(str(int(row['mother_id'])), str(row['id']),label='Born')
        if pd.notnull(row['father_id']):
            g.edge(str(int(row['father_id'])), str(row['id']),label='Born')
        if pd.notnull(row['spouse_id']):
            g.edge(str(row['id']), str(int(row['spouse_id'])), label='Married')

    # Save the .dot file
    g.save()

create_family_tree('family_tree.csv')
