
# Family Tree using Graphviz and Python

Description : This project aims to provide a Python script that allows users to build and visualize family trees. The script takes input from a CSV file and generates a Graphviz DOT file, representing the family tree structure. The generated DOT file can be processed using Graphviz software to obtain a graphical representation of the family tree.







## Usage/Examples

1. Generate the Family Tree CSV File: Use the provided script generateFamilyTreeCSV.py  to create the initial CSV file that defines the family tree structure. Customize the CSV file by specifying individuals' names and their relationships.

2. Build a Family Tree: Run the Python script generateFamilyTreeDOT.py, providing the path to the edited CSV file as an input.

3. Visualize the Family Tree: Install Graphviz software or open https://dreampuf.github.io/GraphvizOnline/ link  and use it to render the DOT file and generate an image representing the family tree.


## List of files



| No | file name                | Description                |
| :--| :------------------------| :------------------------- |
|  1 | [generateFamilyTreeDOT.py](./generateFamilyTreeDOT.py)| python file that creates dot file |
|  2 | [generateFamilyTreeCSV.py](./generateFamilyTreeCSV.py) | python file that creates input csv file| 
| 3  | [family_tree.csv](./family_tree.csv) | input family tree file|
|4| [family_tree.dot](./family_tree.dot)| dot output file created by script|
|5| [family_tree.png](./family_tree.png)| output familytree image|


## Appendix

You can provide your own input file, but please ensure that it is in CSV format and contains the required information mentioned in the original input file mentioned above.

