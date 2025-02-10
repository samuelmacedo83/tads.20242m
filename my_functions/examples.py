import pandas as pd

def create_example() -> pd.DataFrame:
    """ Create a dataframe example.

    Returns:
        pd.DataFrame: Names and scores.
    """
    tabela = pd.DataFrame({
        'Nome': ['Renata', 'Anderson', 'Paulo'],
        'Nota1': [10, 5, 9],
        'Nota2': [7, 3, 9 ]  
    })

    return tabela