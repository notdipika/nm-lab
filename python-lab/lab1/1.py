import data_utils as du

data = [10, 20, 30, 40]
print("Mean:", du.mean(data))
print("Max:", du.max_value(data))
print("Min:", du.min_value(data))
print("Range:", du.data_range(data))
print("Variance:", du.variance(data))
print("Standard Deviation:", du.standard_deviation(data))
    
class DataSample:
    def __init__(self, name, values):
        self.name = name
        self.values = values

    def summary(self):
        return{
            "mean": sum(self.values)/len(self.values),
            "max": max(self.values),
            "min": min(self.values),
            "range": max(self.values) - min(self.values),
            "variance": sum((x - (sum(self.values)/len(self.values))) **2 for x in self.values) / len(self.values),
            "standard_deviation": (sum((x - (sum(self.values)/len(self.values))) **2 for x in self.values) / len(self.values))**0.5
           }
    
    def display(self):
        print(f"DatsSample: {self.name}")
        print("Values: ", self.values)
        

sample1 = DataSample("Sample1", [100, 200, 300, 400])
sample1.display()
print(sample1.summary())