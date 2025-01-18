import json
import pickle
import sklearn
import numpy  as np
__data_columns= None
__locations = None
__model=None

def get_estimate_price(location,sqft,bath,bhk):
    try:
      loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x  = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)
    
    
def get_location_names():
    # load_sevaed_artifacts()
    print("get_location_names function")
    return __locations
def load_sevaed_artifacts():
    print("loading saved artifacts...strat")
    global __data_columns
    global __locations
    global __model
    with open("server/artifacts/columns.json","r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
        

    with open("server/artifacts/bangluoure_home_prices_model.pickle","rb") as f:
        print(f,"@this is a model file")
        __model = pickle.load(f)

    print("load_sevaed_artifacts loading")
    
if __name__ == '__main__':
    load_sevaed_artifacts()
    # get_location_names()
