# PRegress

PRegress is a Python package for regression analysis and data visualization. It provides tools for model fitting, prediction, and various types of plots to help visualize your data and regression results.

## Features

- Model fitting and prediction with a convenient formula notation
- Various types of plots (boxplot, histogram, scatter plot, etc.)
- Integration with popular libraries like `pandas` and `statsmodels`

## Installation

You can install the package using `pip`:

```sh
pip install pregress
```

## Usage

### Importing the Package

To use the functions provided by the package, import it as follows:

```python
import pregress as pr
```

### Example Usage

Here are some examples of how to use the key functions in the package.

```python
import pandas as pd
import numpy as np

# Generating a DataFrame with random numbers
np.random.seed(42)  # For reproducibility
data = np.random.rand(100, 5)  # 100 rows, 5 columns
columns = ['Y', 'X1', 'X2', 'X3', 'X4']

df1 = pd.DataFrame(data, columns=columns)
```

#### Model Fitting and Prediction

```python
import pregress as pr

# Fit model with formula 
model = pr.fit("Y ~ X1 + X2:X3+ log(X3)", df1)

# Generate a model summary
pr.summary(model)

# Make predictions
pr.predict(model, df1)
```

#### Plotting

```python
# Generate a boxplot
pr.boxplot("Y ~ X1 + X2", df1)

# Generate a histogram
pr.hist(df1.Y)

# Multiple histograms
pr.hists("Y ~ X1 + X2 + X3+X4",data = df1)

# Scatter plot
pr.plotXY("Y ~ X1", data = df1)

# Multiple Scatter plots
pr.plots("Y ~ X1 + X2 + X3+X4",data = df1)
```

### Required Fixes

Based on current testing, the following fixes are required:

1. Ensure global scope accessibility for variables.
2. Adjust summary spacing.
3. Review file organization.
4. Provide compatibility with `scikit-learn`.
5. Implement AI-generated summaries.

## Contributing

We welcome contributions to PRegress! If you find a bug or have a feature request, please open an issue on [GitHub](https://github.com/damcgib/PRegress). You can also contribute by:

1. Forking the repository
2. Creating a new branch (`git checkout -b feature-branch`)
3. Committing your changes (`git commit -am 'Add some feature'`)
4. Pushing to the branch (`git push origin feature-branch`)
5. Creating a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

We would like to thank all contributors and users of PRegress for their support and feedback.  
