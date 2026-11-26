# Google Stock Price Prediction — LSTM Study

A learning repository exploring historical Google stock-price data, preprocessing, visualization, and the foundations of LSTM-based time-series forecasting.

## Repository contents

- `Stocks_code.ipynb` — notebook with the currently committed data-loading, preprocessing, and visualization steps.
- `stocks_code.py` — Python version of the starter preprocessing workflow.
- `Stock Price Prediction.docx` — project report/documentation.
- `Stock Price Prediction_synopsis.pdf` — project synopsis.
- `Stock_price _prediction.pptx` — presentation.

## Current implementation status

The committed notebook and Python script currently demonstrate loading the Google training CSV, selecting the opening-price column, and plotting the series. The complete model-training, evaluation, and prediction workflow is not present in these two code files yet.

The notebook expects a file named `Google_Stock_Price_Train.csv`, which is not currently included in this repository. Add the dataset locally before running the notebook.

## Run the starter workflow

Install the required packages:

```bash
python -m pip install numpy pandas matplotlib
```

Place `Google_Stock_Price_Train.csv` beside the notebook/script, then run:

```bash
python stocks_code.py
```

Or open `Stocks_code.ipynb` in Jupyter Notebook or Google Colab.

## Source acknowledgement

This repository is a study/portfolio adaptation of material from the original [Final-Year Machine Learning Stock Price Prediction project](https://github.com/Vatshayan/Final-Year-Machine-Learning-Stock-Price-Prediction-Project). The source reference is retained to acknowledge the origin of the adapted material.

## Important note

This is an educational time-series project, not financial advice or a reliable trading signal. Historical prices do not guarantee future performance.
