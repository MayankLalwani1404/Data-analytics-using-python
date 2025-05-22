import numpy as np

def calculate():
    user_input = input("Enter 9 numbers separated by space: ")  
    user_input = user_input.split()
    if len(user_input) == 9:
        print("List of numbers:", user_input)
        arr = np.array(user_input, dtype=float).reshape(3, 3)
        print(arr)
        dict = {
            'mean': [np.mean(arr, axis=0). tolist(), np.mean(arr, axis=1). tolist() , np.mean(arr)],
            'var': [np.var(arr, axis=0). tolist() , np.var(arr, axis=1). tolist() , np.var(arr)],
            'std': [np.std(arr, axis=0). tolist() , np.std(arr, axis=1). tolist() , np.std(arr)],
            'max': [np.max(arr, axis=0). tolist() , np.max(arr, axis=1).  tolist() , np.max(arr)],
            'min': [np.min(arr, axis=0).  tolist() , np.min(arr, axis=1).  tolist() , np.min(arr)],
            'sum': [np.sum(arr, axis=0). tolist() , np.sum(arr, axis=1). tolist() , np.sum(arr)]
        }
        print(dict)
    else:
        print("List must contain nine numbers.")
calculate()