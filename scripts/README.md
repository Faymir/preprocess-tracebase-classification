# Script for tracebase files preprocessing


1. `preprocess_device.py` script to extract informations from tracebase (incomplete) folder of a specific device, process it and generate a filein the preprocessed directory
    + Usage
        ```
        python scripts/preprocess_device.py device_name 0
        ```
        `device_name` is the name of the device (Refrigerator, Washingmacchine ...)
        `0` is the threshold of the device: the value corresponding of it cosumption when it is in idle mode. *Put zero if you don' t know what it means* 
2. `generate_training_data.py` scripts that generate a file `test_stats.csv` dans le dossier `training` for all devices that have been preprocessed and that have their files in the `preprocessed/new/` directory
    + Usage
        ```
        python scripts/generate_training_data.py 200
        ```
        `200` the maximal number of data per device to extract to the training file  
3. `generate_test_data.py` this one generate new data for testing the classification model prediction accuracy
    + Usage
        I have to update this code. Not usefull actually
4. `calculate_average.py` a helper script to check the prediction accuracy
    + Usage
        ```
        python calculate_average.py
        ```
5. `old_preprocess_device.py` the previous file processiing script that not calculate statistic values, but only print them.
    + Usage
        ```
        python scripts/old_preprocess_device.py device_name 0
        ```
        `device_name` is the name of the device (Refrigerator, Washingmacchine ...)
        `0` is the threshold of the device: the value corresponding of it cosumption when it is in idle mode. *Put zero if you don' t know what it means*