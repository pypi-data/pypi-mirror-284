# hudutils/hudutils.py

import json
import time, sys, os

def flatten_json(json_data, parent_key='', sep='.'):
    items = []
    for k, v in json_data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_json(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                items.extend(flatten_json({f"{new_key}[{i}]": item}, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)



def filename_with_rollover(file_path='hud.log', opts = ['year','month','day']):
    
    file_path = os.path.join(file_path)
    file_name = os.path.basename(file_path)
    dir_name = os.path.dirname(file_path)
    

    """
    
    HELP:
    filename     = text.txt
    new_filename = filename_with_rollover(filename, opts = ['year','month','day'])
    
    
    """

    allowed = ['year','month','day','hour','mins','sec']
    name    = ''
    schema  = ''
    localtime = time.localtime(time.time())
    timer   = {}

    timer['year']  = str(localtime.tm_year)
    timer['month'] = str(localtime.tm_mon)
    timer['day']   = str(localtime.tm_mday)
    timer['hour']  = str(localtime.tm_hour)
    timer['mins']  = str(localtime.tm_min)
    timer['sec']   = str(localtime.tm_sec)

    for n in opts:
        if n not in allowed:
            print ("""
            
            The filename_with_rollover function must contain 
            one of the following:
            ['year','month','day','hour','mins','sec']
            
            """)
            sys.exit()
        else:
            name   = name+timer[n]
            schema = schema+n+'_'        
    filen_ = name + '_' + file_name
    
    new_file_path = os.path.join(dir_name, filen_)
    
    return new_file_path

