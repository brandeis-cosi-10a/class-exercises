# Country data

Write a class in [code.py](code.py) to hold statistics about countries of the world. The class will also have the ability to 
compute some secondary statistics, and compare statistics from different countries.

# Requirements:

1. Define class named `CountryInfo`
2. A `CountryInfo` instance must be initialized with these pieces of data:
   * A name (`str`)
   * A population (`int`)
   * A GDP (`int`)
   * An area in square miles (`int`)
   * An annual inflation rate (`float`)
3. Define the following methods on `CountryInfo`:
   * `per_capita_gdp()`: Compute and return the GDP per person (`GDP / population`)
   * `population_density()`: Compute and return the population density (`population / area`)
   * `predicted_gdp(years)`: Predict and return the country's GDP in `years` years. Use the inflation rate and the compound interest formula: `(GDP * (1 + inflation_rate)^years)`
   * `compare(other_country)`: Compare this country to `other_country` by printing:
      * Which country has a higher population
      * Which country has a higher population density
      * Which country will have a larger GDP in 10 years
4. Create some `CountryInfo` instances and use these methods to print out statistics about the countries, and compare two countries.