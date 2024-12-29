import pandas as pd
import dvc.api

class DataLoader:
    """Classe responsável por carregar os dados."""
    def __init__(self, data_path: str):
        self.data_path = data_path

    def load_data(self) -> pd.DataFrame:
        """Carrega os dados usando DVC."""
        data_url = dvc.api.get_url(self.data_path)
        return pd.read_csv(data_url)
