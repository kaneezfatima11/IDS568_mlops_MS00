def test_core_imports():
    import numpy as np
    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier 
    assert True

def test_numpy_operation():
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5])
    assert arr.mean() == 3.0