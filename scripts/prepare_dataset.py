# prepare_dataset.py
import sys
import os

# ✅ Add project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.exceptions import DataLoadError

logger = get_logger(__name__)

def prepare_data(input_csv, output_dir='data', test_size=0.2, random_state=42):
    try:
        # Load dataset
        df = pd.read_csv(input_csv)
        logger.info(f"✅ Loaded dataset with shape: {df.shape}")

        if 'airline_sentiment' not in df.columns or 'text' not in df.columns:
            raise DataLoadError("Required columns not found in dataset.")

        df = df[['text', 'airline_sentiment']]
        df.columns = ['text', 'label']
        df['label'] = df['label'].str.lower()

        df = df[df['label'].isin(['positive', 'neutral', 'negative'])]

        train_df, test_df = train_test_split(df, test_size=test_size, random_state=random_state)

        os.makedirs(output_dir, exist_ok=True)
        train_df.to_csv(os.path.join(output_dir, 'train.csv'), index=False)
        test_df.to_csv(os.path.join(output_dir, 'test.csv'), index=False)

        logger.info("✅ train.csv and test.csv successfully saved to 'data/' directory.")
    except Exception as e:
        logger.error(f"❌ Failed to prepare dataset: {str(e)}")
        raise DataLoadError(str(e))

if __name__ == "__main__":
    input_csv_path = "data/Tweets.csv"
    prepare_data(input_csv_path)
