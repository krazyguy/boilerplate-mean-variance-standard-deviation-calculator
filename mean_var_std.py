import numpy as np

def calculate(list):
    

    #throw error if list size not equal to 9
    if len(list)!=9:
        raise ValueError("List must contain nine numbers.")

    
    
    n_array=np.array(list).reshape(3,3)
        
    result = {}
    result['mean'] = [n_array.mean(axis=0).tolist(), n_array.mean(axis=1).tolist(), n_array.mean()]
    result['variance'] = [n_array.var(axis=0).tolist(), n_array.var(axis=1).tolist(), n_array.var()]
    result['standard deviation'] = [n_array.std(axis=0).tolist(), n_array.std(axis=1).tolist(), n_array.std()]
    result['min'] = [n_array.min(axis=0).tolist(), n_array.min(axis=1).tolist(), n_array.min()]
    result['max'] = [n_array.max(axis=0).tolist(), n_array.max(axis=1).tolist(), n_array.max()]
    result['sum'] = [n_array.sum(axis=0).tolist(), n_array.sum(axis=1).tolist(), n_array.sum()]


    return result



