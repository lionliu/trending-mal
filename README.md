# What is trending in MyAnimeList

This is a project for the Data Science course from UFPE [(IF697)](https://profluciano.github.io/cd/)

## Dataset

We extracted the animes ID's from [this](https://www.kaggle.com/marlesson/myanimelist-dataset-animes-profiles-reviews) dataset from Kaggle and ran multiple requests with the [Jikan API](https://jikan.moe) to get more useful data not present in the original dataset.

The extracted data can be downloaded [here](http://cin.ufpe.br/~llm2/newAnime.zip)

## Notebooks

The notebooks are in Portuguese for academic reasons.

1. myAnimeListAnalysis: Preprocessing, exploratory data analysis, statistical hypothesis testing, and clustering
2. myAnimeListRegressions: Hyperparameter tuning for four regressors from sklearn and some tries to reduce the variance
3. auto-sklearn: Ran autosklearn in the dataset to function as a baseline comparison for the regressors above.

The hyperparameter tuning was made using wandb. The project can be founded [here](https://wandb.ai/ds-gtsa-llm2/trending-mal)

## Members:

* Gabriel Teixeira: <gtsa@cin.ufpe.br>
* Leão Liu: <llm2@cin.ufpe.br>