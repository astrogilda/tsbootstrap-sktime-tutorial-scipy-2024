Welcome to the "Enhancing Predictive Analytics with tsbootstrap and sktime" workshop at scipy 2024
============================================

This tutorial is designed for data scientists, analysts, and researchers interested in advanced time series analysis and forecasting techniques. We'll explore cutting-edge methods for enhancing uncertainty quantification and prediction accuracy in time series data, using state-of-the-art tools like [tsbootstrap](www.github.com/astrogilda/tsbootstrap) and [sktime](www.github.com/sktime/sktime).

Throughout this 4-hour session, we'll cover:

1. Fundamentals of modern time series analysis and bootstrapping methods
2. Advanced forecasting techniques and their practical applications across various domains
3. Innovative approaches to uncertainty quantification and probabilistic forecasting
4. Hands-on exercises using leading-edge tools to solve real-world time series challenges

By the end of this tutorial, you'll have gained insights into the latest developments in time series analysis and forecasting, and acquired practical skills to apply these advanced methods to your own data-driven projects.


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tsbootstrap-sktime-tutorial-scipy-2024/main?filepath=notebooks) [![!discord](https://img.shields.io/static/v1?logo=discord&label=discord&message=chat&color=lightgreen)](https://discord.com/invite/54ACzaFsn7) [![!slack](https://img.shields.io/static/v1?logo=linkedin&label=LinkedIn&message=news&color=lightblue)](https://www.linkedin.com/in/sankalp-gilda/)

## :rocket: How to get started

In the tutorial, we will move through notebooks section by section.

You have different options how to run the tutorial notebooks:

* Run the notebooks on your machine. [Clone] this repository, get [conda], install the required packages in an environment, and open the notebooks with that environment. For detail instructions, see below.
* or, use python venv, and/or an editable install of this repo as a package. Instructions below.

[clone]: https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository
[conda]: https://docs.conda.io/en/latest/

## Outline

| | Title | Description | Code |
| ---- | ---------------------------- | ------------------------------------------------------------ | ---- |
| 1 | General Introduction to tsbootstrap and sktime | An overview of time series analysis, bootstrapping methods, and their significance. Introduction to tsbootstrap and sktime, their features, and capabilities. | TBD |
| 2 | Time Series Forecasting and Uncertainty Quantification | Exploration of sktime's forecasting models and their integration with tsbootstrap. Hands-on exercise applying sktime models for forecasting with uncertainty quantification. Introduction to probabilistic forecasting. | TBD |
| 3 | Time Series Bootstrapping | Detailed exploration of tsbootstrap's bootstrapping methods (Block, Residual, Sieve, etc.). Hands-on exercise implementing Block Bootstrap on sample time series data. Advanced bootstrapping methods with illustrative examples. | TBD |
| 4 | Metrics, Evaluation, and Backtesting | Overview of model performance evaluation techniques. Hands-on exercise on creating probabilistic forecasts and evaluating model performance. Introduction to backtesting methodologies. | TBD |
| 5 | Advanced Model Building | Real-world case studies demonstrating the application of tsbootstrap and sktime. Discussion on future trends and directions in time series analysis. Introduction to the community ecosystem and how to contribute to tsbootstrap and sktime's development. | TBD |



## :wave: How to contribute

If you're interested in contributing to `tsbootstrap` or `sktime`, you can find out more how to get involved [here](https://github.com/astrogilda/tsbootstrap/blob/main/CONTRIBUTING.md) and  [here](https://www.sktime.net/en/latest/get_involved.html).

Any contributions are welcome, not just code!

## Installation instructions for local use

To run the notebooks locally, you will need:

* a local repository clone
* a python environment with required packages installed

### Cloning the repository

To clone the repository locally:

`git clone https://github.com/astrogilda/tsbootstrap-sktime-tutorial-scipy-2024`

### Using conda env

1. Create a Python virtual environment using Conda
`conda create -y -n tsbootstrap_sktime python=3.10`
2. Activate your Conda environment
`conda activate tsbootstrap_sktime`
3. Install pip in your Conda environment (if not already installed)
`conda install -y pip`
4. Install required packages from requirements.txt using pip
`pip install -r requirements.txt`
5. If using Jupyter, make the environment available in Jupyter
`python -m ipykernel install --user --name=tsbootstrap_sktime`


### Using python venv

1. Create a python virtual environment:
`python -m venv tsbootstrap_sktime`
2. Activate your environment:
 - `source tsbootstrap_sktime/bin/activate` for Linux
 - `tsbootstrap_sktime/Scripts/activate` for Windows
3. Install the requirements:
`pip install -r requirements.txt`
4. If using jupyter: make the environment available in jupyter:
`python -m ipykernel install --user --name=tsbootstrap_sktime`
