# Simulations app

Dash app with simulations to test the Central Limit Theorem (CTL) and the Law of Large Numbers (LLN).

## Description

The user can choose the size of the random sample ($n$) and the probability ($p$). Then, a thousand random samples of size $n$ are created with each observation distributed $Bernoulli(p)$. For each random sample, we compute the mean sample. 

Finally, we plot the distribution of the mean sample.

## Getting Started

After cloning the repository, run the following command to create a conda environment:
```shell
git env create -f environment.yml
```

Run the following command to start the app
```shell
cd ~\Simulations\Dev # Make sure the Dev folder is your current working directory
python app.py
```