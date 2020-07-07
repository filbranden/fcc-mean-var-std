import numpy as np

def calculate(nums):
    if len(nums) != 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(nums)
    arr = arr.reshape((3, 3))
    funcs = {
        "mean": np.mean,
        "variance": np.var,
        "standard deviation": np.std,
        "max": np.amax,
        "min": np.min,
        "sum": np.sum,
    }
    calculations = {
        name: [
            list(fn(arr, axis=0)),
            list(fn(arr, axis=1)),
            fn(arr),
        ]
        for name, fn in funcs.items()
    }
    return calculations
