<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<p align="center"><img src="docs/logo.png" alt="logo" width="100%" height="100%"></p>

| Overview | |
|---|---|
| **Open Source** |  [![BSD 3-clause](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://github.com/ActurialCapital/blocks/blob/main/LICENSE) |
| **Code** |  [![!pypi](https://img.shields.io/pypi/v/python-blocks?color=orange)](https://pypi.org/project/python-blocks/) [![!python-versions](https://img.shields.io/pypi/pyversions/python-blocks)](https://www.python.org/) |
| **CI/CD** | [![!codecov](https://img.shields.io/codecov/c/github/ActurialCapital/blocks?label=codecov&logo=codecov)](https://codecov.io/gh/ActurialCapital/blocks) |
| **Downloads** | ![PyPI - Downloads](https://img.shields.io/pypi/dw/python-blocks) ![PyPI - Downloads](https://img.shields.io/pypi/dm/python-blocks) [![Downloads](https://static.pepy.tech/personalized-badge/python-blocks?period=total&units=international_system&left_color=grey&right_color=blue&left_text=cumulative%20(pypi))](https://pepy.tech/project/python-blocks) |


<br>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
        <ul>
            <li><a href="#introduction">Introduction</a></li>
        </ul>
        <ul>
            <li><a href="#built-with">Built With</a></li>
        </ul>
    </li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#testing">Testing</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

### Introduction

`blocks` is a package designed to extend the functionality of `scikit-learn` by providing additional blocks for creating custom pipelines, easy-to-use base transformers, and useful decorators. This package aims to simplify the process of building and managing machine learning workflows in Python.

The current version of the package offers:

* **Custom Pipelines**: Easily create and manage custom pipelines
* **Base Transformers and Samplers**: A collection of base transformers and samplers to streamline feature transformation
* **Decorators**: Handy decorators to simplify repetitive tasks

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

* `scikit-learn = "^1.5.0"`
* `imbalanced-learn = "^0.12.3"`
* `pandas = "^2.2.2"`
* `numpy = "^1.26.4"`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Installation

The easiest way to install `blocks` is via `PyPI`:

```sh
pip install python-blocks
```

Or via `poetry`:

```sh
poetry add python-blocks
```

## Testing

To run the test suite after installation, follow these steps from the source directory. First, install `pytest` version 8.2.2:

```
pip install pytest==8.2.2
```

Then run `pytest` as follow:

```
pytest tests
```

Alternatively, if you are using `poetry`, execute:

```
poetry run pytest
```

For more information, visit our [Codecov](https://app.codecov.io/gh/ActurialCapital/blocks) page.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Getting Started

### Pipeline

* Callback function that logs information in between each intermediate step
* Access particular named step data
* Inherites from `imblearn` pipeline, which works with both transformers and samplers

#### Dataset

```python
>>> from sklearn.datasets import make_regression
>>> X, y = make_regression(n_samples=1000, n_features=10, random_state=42)
```

#### Model with both recorded and logged callbacks 

```python
>>> from sklearn.preprocessing import StandardScaler
>>> from sklearn.linear_model import LinearRegression
>>> from sklego.meta import EstimatorTransformer
>>> from blocks import BlockPipeline, custom_log_callback
>>> 
>>> pipe = BlockPipeline([
...   ("scaler", StandardScaler()),
...   ("regression", EstimatorTransformer(LinearRegression()))
... ],
...   record="scaler",
...   log_callback=custom_log_callback
... )
```

#### Logs

```python
>>> pipe.fit(df, y)
# [custom_log_callback:78] - [scaler][StandardScaler()] shape=(1000, 10) time=0s
```

#### Records

```python
>>> predicted = pipe.transform(df)
>>> pipe.name_record
# 'scaler'
>>> pipe.record
# array([[ ...
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

we also recommend to have a look at `project-template`.
> `project-template` is a template project for `scikit-learn` compatible extensions. It aids development of estimators that can be used in `scikit-learn` pipelines and (hyper)parameter search, while facilitating testing (including some API compliance), documentation, open source development, packaging, and continuous integration.

Refer to the [Official Documentation](https://contrib.scikit-learn.org/project-template) to modify the template for your own scikit-learn contribution.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the BSD-3 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

