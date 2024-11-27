class CountryInfo:
    def __init__(self, name, pop, gdp, area, inflation):
        self.name = name
        self.population = pop
        self.gdp = gdp
        self.area = area
        self.inflation = inflation

    def per_capita_gdp(self):
        return self.gdp / self.population
    
    def population_density(self):
        return self.population / self.area
    
    def predicted_gdp(self, years):
        return self.gdp * ((1 + self.inflation) ** years)

    def compare(self, other):
        if other.population > self.population:
            print(f"{other.name} has a higher population than {self.name}")
        else:
            print(f"{self.name} has a higher population than {other.name}")

        if other.population_density() > self.population_density():
            print(f"{other.name} has a higher population density than {self.name}")
        else:
            print(f"{self.name} has a higher population density than {other.name}")

        if other.predicted_gdp(10) > self.predicted_gdp(10):
            print(f"{other.name} will have a higher GDP than {self.name} in 10 years")
        else:
            print(f"{self.name} will have a higher GDP than {other.name} in 10 years")

c1 = CountryInfo("a", 10000, 1000000, 1000, 0.1)
c2 = CountryInfo("b", 1000, 500000, 20, 1)
c3 = CountryInfo("c", 20000, 2581010, 20000, 0.2)

c1.compare(c2)
c1.compare(c3)
c2.compare(c3)
