import requests
import random
import numpy as np
from datetime import datetime, timedelta

def id_probs(num_ids):
    # Generate a list of probabilities for each ID
    probs = np.random.dirichlet(np.ones(num_ids),size=1)[0]

    # Normalize the probabilities
    total_prob = sum(probs)
    probs = [prob / total_prob for prob in probs]

    return probs

def generate_ids(num_names):
    # Download a list of names from a random name generator API
    response = requests.get(f'https://randomuser.me/api/?inc=name&noinfo&nat=us&results={200}')
    data = response.json()

    # Extract the first and last names from the API response
    names = []
    for person in data['results']:
        first_name = person['name']['first']
        last_name = person['name']['last']
        user_id = f"{last_name[:4]}{first_name[:2]}".lower()
        
        names.append(user_id)

    probs = id_probs(len(names))
    
    result = []
    for i in range(num_names):
        user_id = random.choices(names, weights=probs)[0]
        result.append(user_id)
    
    return result



def generate_calling_files(n):

    # Define the bias probabilities for each calling file
    bias_probs = {
        'trajectory-toolbox_1.2.2': 0.2,
        'csv-helpers-toolbox_1.4.0': 0.15,
        'maritime-toolbox_1.3.0': 0.1,
        'telecom-toolbox_1.7.1': 0.1,
        'imagery-toolbox_2.0.0': 0.1,
        'operations-toolbox_1.2.2': 0.075,
        'hexify-toolbox_0.1.2': 0.075,
        'metadata-toolbox_0.1.0': 0.05,
        'polar-toolbox_1.8.2': 0.05,
        'label-store_0.1.0': 0.05,
        'detections-warehouse_0.5.0': 0.05
    }

    # Normalize the bias probabilities
    total_bias = sum(bias_probs.values())
    for key in bias_probs:
        bias_probs[key] /= total_bias

    # Generate a list of calling files using the bias probabilities
    calling_files = []
    for i in range(n):
        calling_file = random.choices(list(bias_probs.keys()), weights=list(bias_probs.values()))[0]
        calling_files.append(calling_file)

    return calling_files

def generate_error_message():
    error_codes = ['ERR001', 'ERR002', 'ERR003', 'ERR004', 'ERR005']
    error_messages = [
        'File not found',
        'Invalid argument',
        'Connection timeout',
        'Internal server error',
        'Memory allocation failed'
    ]
    error_message = random.choice(error_messages)
    error_code = random.choice(error_codes)
    return f'{error_code}: {error_message}'


def generate_debug_message():
    source_files = ['data_processor.py', 'main.py', 'utils.py', 'config.py']
    messages = [
        'Loading data from disk...',
        'Preprocessing data...',
        'Optimizing model parameters...',
        'Saving model to disk...',
        'Generating plots...',
        'Running unit tests...'
    ]
    return f"{random.choice(source_files)}:{random.choice(messages)}"

def generate_warning_message():
    warnings = [
        "Invalid input detected",
        "Data may be truncated",
        "Potential performance issue detected",
        "Unknown event occurred",
        "Unexpected behavior observed",
        "Possible data corruption detected",
        "Warning: operation may have side effects",
        "Non-fatal error detected",
        "Inconsistent data detected",
        "Resource limit exceeded",
        "Unusual system behavior detected"
    ]
    return random.choice(warnings)
import random

def generate_info_message():
    components = [
        'Database',
        'Backend',
        'Frontend',
        'Networking',
        'Security',
        'Authentication',
        'Authorization',
        'Cache',
        'Configuration',
        'Deployment'
    ]
    actions = [
        'started',
        'stopped',
        'loaded',
        'saved',
        'deleted',
        'updated',
        'created',
        'requested',
        'generated'
    ]
    adjectives = [
        'successful',
        'failed',
        'unsuccessful',
        'completed',
        'incomplete',
        'pending',
        'finished',
        'aborted',
        'cancelled'
    ]
    component = random.choice(components)
    action = random.choice(actions)
    adjective = random.choice(adjectives)
    return f'{component} {action} {adjective}.'

def generate_calling_functions(calling_file):
    CALLING_FUNCTIONS = {
    'trajectory-toolbox_1.2.2':['FilterTool','CompressionTool','PredictionTool'],
    'csv-helpers-toolbox_1.4.0':['ParseDatesTool','ValidateLatLonTool','DMStoDDTool','FormatDatetimeTool'],
    'maritime-toolbox_1.3.0':['ParseTracksTool','DisplayTracksTool','InterpolateTool'],
    'telecom-toolbox_1.7.1':['ProcessDataTool','PatternTool','NetworkTool'],
    'imagery-toolbox_2.0.0':['CatalogueTool','SelectionTool','ImageEnhancementTool','GeoRegistrationTool'],
    'operations-toolbox_1.2.2':['GeoMappingTool','TargetTrackingTool','RiskAssessmentTool'],
    'hexify-toolbox_0.1.2':['GetH3Tool','HexCountsTool'],
    'metadata-toolbox_0.1.0':['FeatureExtractionTool', 'MetadataHarvestingTool', 'SpatialQueryTool', 'GeoTaggingTool'],
    'polar-toolbox_1.8.2':['PolarDataTool', 'IceSatTool', 'AntarcticMappingTool'],
    'label-store_0.1.0':['load_image_data', 'create_label_set', 'augment_image_data', 'save_labeled_data', 'split_train_test_data', 'generate_image_patches'],
    'detections-warehouse_0.5.0':['create_detection_database', 'add_detection', 'get_detection_by_id', 'get_all_detections', 'filter_detections_by_class', 'remove_detection_by_id']
    }
    
    functions = CALLING_FUNCTIONS[calling_file]
    probabilities = [0.25, 0.20, 0.20, 0.15, 0.10, 0.10][:len(functions)]
    probabilities = [p / sum(probabilities) for p in probabilities]

    function = random.choices(functions, weights=probabilities)[0]
    return function

def generate_level_and_mesage():

    LEVELS = ['USAGE'] * 10 + ['ERROR'] * 5 + ['WARNING', 'INFO', 'DEBUG']
    level = random.choice(LEVELS)

    if level == 'USAGE':
        message = ""
    elif level == 'ERROR':
        message = generate_error_message()
    elif level == 'WARNING':    
        message = generate_warning_message()
    elif level == 'INFO':
        message = generate_info_message()
    elif level == 'DEBUG':
        message = generate_debug_message()
    return level, message

def generate_random_timestamps(n):
    timestamps=[]
    start_date = datetime.now() - timedelta(days=60)
    end_date = datetime.now()
    while len(timestamps) < n:
        timestamp = random.uniform(start_date.timestamp(), end_date.timestamp())
        dt = datetime.fromtimestamp(timestamp)
        if dt.weekday() < 5 and 9 <= dt.hour < 17:
            timestamps.append(dt.strftime("%Y-%m-%d %H:%M:%S,%f"))

    return timestamps

def skewed_random_number(n):
    nums = []
    for i in range(n):
        # Set the shape parameter to 0.2 for a left-skewed distribution
        shape = 8
        
        # Set the scale parameter to get the average value of 30 seconds
        scale = 30 / np.random.gamma(shape, 1, 1)
        
        # Generate a random number from the gamma distribution
        rand_num = np.random.gamma(shape, scale, 1)[0]
        
        # Clip the random number to the desired range
        rand_num = np.clip(rand_num, 0.01, 1.5 * 60 * 60)

        nums.append(rand_num)
        
    return nums

def get_records(n):

    # Generate a list of user IDs
    user_ids = generate_ids(n)

    # Generate a list of calling files
    calling_files = generate_calling_files(n)

    # Generate a list of calling functions
    calling_functions = []
    for calling_file in calling_files:
        calling_functions.append(generate_calling_functions(calling_file))

    # Generate a list of runtimes
    runtimes = skewed_random_number(n)

    timestamps = generate_random_timestamps(n)

    # Generate a list of records
    records = []
    for i in range(n):
        lvl,msg = generate_level_and_mesage()
        record = {
            'level': lvl,
            'timestamp': timestamps[i],
            'user_id': user_ids[i],
            'calling_file': calling_files[i],
            'calling_function': calling_functions[i],
            'runtime': runtimes[i],
            'message': msg
        }
        records.append(record)

    return records
    



def main():
    records = get_records(1000)
    [print(r) for r in records]

if __name__ == '__main__':
    main()



