import pickle
from datetime import timedelta


''' FILE SAVING '''
def save_to_file(txt, filename):
    # a supplementary code to save text to a file
    with open(filename, "w") as f:
        f.write(txt)

def load_pkl_data(filepath):
    ''' Loads a pickle object '''
    with open(filepath, 'rb') as file:
        data = pickle.load(file)
        return data
    
def save_pkl_data(data, filepath):
    with open(filepath, "wb") as file:
        pickle.dump(data, file)

''' CALCULATING '''
def get_dates(start_date, end_date):
    ''' returns a list of dates given a range '''
    return [
        start_date + timedelta(days=x) 
        for x in range((end_date - start_date).days + 1)
    ]