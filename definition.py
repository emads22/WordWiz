import pandas as pd
from config import DATA_FILE


class Definition:
    """
    A class to retrieve definitions for a given term from a DataFrame.
    """

    # Assuming DATA_FILE is a global variable representing the path to the CSV file
    df = pd.read_csv(DATA_FILE)

    def __init__(self, term: str) -> None:
        """
        Initializes the Definition object with the given term.

        Parameters:
        - term (str): The term for which definitions will be retrieved.
        """
        self.term = term

    def get(self) -> list:
        """
        Retrieves definitions for the given term.

        Returns:
        - list: A list of definitions for the term.
        """
        # Filter the DataFrame to get definitions for the given term
        definitions = self.df.loc[self.df['word']
                                  == self.term]['definition'].tolist()
        return definitions
