# Weightipy

Weightipy is a cut down version of [Quantipy3](https://github.com/Quantipy/quantipy3) for weighting people data using the RIM (iterative raking) algorithm.

### Changes from Quantipy
- Removed all quantipy overhead. Weightipy supports the latest versions of Pandas and Numpy and is tested for Python 3.7, 3.8, 3.9, 3.10 and 3.11.
- Weightipy runs up to 6 times faster than Quantipy, depending on the dataset.
- Rim class will not generate reports like Quantipy did, unless the parameter verbose is set to True on the Rim constructor.

## Installation

`pip install weightipy`

or

`python3 -m pip install weightipy`

#### Create a virtual envirionment

If you want to create a virtual environment when using Weightipy:

conda
```python
conda create -n envwp python=3
```

with venv
```python
python -m venv [your_env_name]
 ```

## 5-minutes to Weightipy

**Get started**

Assuming we have the variables `gender` and `agecat` we can weight the dataset like this:

```Python
import weightipy as wp

targets = {
    "agecat": {"18-24": 5.0, "25-34": 30.0, "35-49": 26.0, "50-64": 19.0, "65+": 20.0},
    "gender": {"Male": 49, "Female": 51}
}
scheme = wp.scheme_from_dict(targets)

df_weighted = wp.weight_dataframe(
    df=my_df,
    scheme=scheme,
    weight_column="weights"
)
efficiency = wp.weighting_efficiency(df_weighted["weights"])
```

In case we are working with census data, which also includes a region variable and we would
like to weight the data by age and gender in each region, we can use the `scheme_from_df` function:
```Python
import weightipy as wp
import pandas as pd

df_data = pd.read_csv("data_to_weight.csv")
df_census = pd.read_csv("census_data.csv")

scheme = wp.scheme_from_df(
    df=df_census,
    cols_weighting=["agecat", "gender"],
    col_filter="region",
    col_freq="freq"
)
df_weighted = wp.weight_dataframe(
    df=d,
    scheme=scheme,
    weight_column="weights"
)
efficiency = wp.weighting_efficiency(df_weighted["weights"])
```

Or by using the underlying functions that will give more access to the weighting process, we
can use the Rim and WeightEngine classes directly:
```Python
import weightipy as wp

# in this example, agecat and gender are int dtype

age_targets = {'agecat':{1:5.0, 2:30.0, 3:26.0, 4:19.0, 5:20.0}}
gender_targets = {'gender':{0:49, 1:51}}
scheme = wp.Rim('gender_and_age')
scheme.set_targets(targets=[age_targets, gender_targets])

my_df["identity"] = range(len(my_df))
engine = wp.WeightEngine(data=df)
engine.add_scheme(scheme=scheme, key="identity", verbose=False)
engine.run()
df_weighted = engine.dataframe()
col_weights = f"weights_{scheme.name}"

efficiency = wp.weighting_efficiency(df_weighted[col_weights])

print(engine.get_report())

Weight variable       weights_gender_and_age
Weight group                  _default_name_
Weight filter                           None
Total: unweighted                 582.000000
Total: weighted                   582.000000
Weighting efficiency               60.009826
Iterations required                14.000000
Mean weight factor                  1.000000
Minimum weight factor               0.465818
Maximum weight factor               6.187700
Weight factor ratio                13.283522
```

For more references on the underlying classes, refer to the Quantipy 
[documentation](https://quantipy.readthedocs.io/en/staging-develop/sites/lib_doc/weights/02_rim.html#using-the-rim-class)

Overview of functions to get started:

| Function             | Description                                                                                                                                                                                                                                  |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| weight_dataframe     | Weights data by scheme, returns modified dataframe with new weight column.                                                                                                                                                                   |
| weighting_efficiency | Takes weights and returns efficiency of weighting. See: https://quantipy.readthedocs.io/en/staging-develop/sites/lib_doc/weights/03_diags.html#the-weighting-efficiency                                                                      |
| scheme_from_dict     | Turns a dict of dicts into a Rim scheme. Keys of the dict are column names and the values are distributions. These are normalized.                                                                                                           |
| scheme_from_df       | Creates a Rim scheme from a dataframe from specified weighting columns and frequency column. Useful when working with census data.                                                                                                           |
| Rim class            | Useful for creation of more complex weighting schemas. For example when weighting subregions or groups, which require filters. See: https://quantipy.readthedocs.io/en/staging-develop/sites/lib_doc/weights/02_rim.html#using-the-rim-class |
| WeightEngine class   | Useful for more specialised manipulation of the weighting process                                                                                                                                                                            |

## Planned features
- More utility functions to simplify the weighting process
- More performance improvements, in order to better support batch weighting of many datasets
- Support for multithreaded weighting (possibly using Polars)
- Rewrite of the API to be less oriented towards how Quantipy worked and more in line with simple weighting needs
- Far future: Support for more weighting algorithms


# Contributing

The test suite for Weightipy can be run with the command

`python3 -m pytest tests`

But when developing a specific aspect of Weightipy, it might be quicker to run (e.g. for the Rim class)

`python3 -m unittest tests.test_rim`

We welcome volunteers and supporters. Please include a test case with any pull request, especially those that run calculations.

# Quantipy

#### Origins
- Quantipy was concieved of and instigated by Gary Nelson: http://www.datasmoothie.com


### Contributors on Quantipy
- Alexander Buchhammer, Alasdair Eaglestone, James Griffiths, Kerstin Müller : https://yougov.co.uk
- Datasmoothie’s Birgir Hrafn Sigurðsson and [Geir Freysson](http://www.twitter.com/@geirfreysson): http://www.datasmoothie.com
