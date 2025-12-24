def mean(lst):
    return sum(lst)/len(lst)

def max_value(lst):
    return max(lst)

def min_value(lst):
    return min(lst)

def data_range(lst):
    return max(lst) - min(lst)

def variance(lst):
    mean_val = sum(lst) / len(lst)
    return sum((x- mean_val) ** 2 for x in lst)/len(lst)

def standard_deviation(lst):
    return variance(lst)**0.5