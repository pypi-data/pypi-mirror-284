# Module for loading Distributed Acoustic Sensing (DAS) data. SILIXA / OPTASENSE

Python: If you want to get started quickly, have a look at the [examples](#example-python-script).


## Install dependencies
If you want to use pip for installing, you can just execute *install_dependencies.sh*.
Otherwise, have a look into install_dependencies.sh and install the listed packages yourself.


## Use as python module
### API


#### Recommended: simplest interface
```python
def load_array(t_start:datetime, t_end:datetime, channel_start:int, channel_end:int) -> NP.ndarray:
```

```
Loads data and returns it as a numpy array. 
Args:
    t_start (datetime): datetime object which defines the start of the data to load.
    t_end (datetime): datetime object which defines the end of the data to load.
    channel_start (int): The starting index of sensor in the data (inclusive).
    channel_end (int): The ending index of sensors in the data (exclusive).
Returns:
    A 2d-numpy-array containing the data.
    The first axis corresponds to the time, the second, to the channel
 ```


#### More detailed interface
```python
def load_array(t_start:datetime, t_end:datetime, t_step:int, channel_start:int, channel_end:int, channel_step:int) -> NP.ndarray:
```

``` Loading data into numpy array.
Returns nothing, the data can be accessed by accessing the data field of this instance.
Warning: using a different value then 1 for t_step or channel_step can result in a high cpu-usage.
        Consider using multithreaded=True in the constructor and a high amount of workers if needed.
Constraints: 
    t_start has to be less or equal t_end, 
    same for channel_start and channel_end.
    t_step and channel_step have to be greater then 0
Args:
    t_start (datetime): datetime object which defines the start of the data to load.
    t_end (datetime): datetime object which defines the end of the data to load.
    t_step (int): If you, for example only want to load the data of every fourth timestep use t_end=4
    channel_start (int): The starting index of sensor in the data (inclusive).
    channel_end (int): The ending index of sensors in the data (exclusive).
    channel_step (int): Like t_step, but for the sensor position.
Returns:
    A 2d-numpy-array containing the data.
    The first axis corresponds to the time, the second, to the channel
```

### Lower level interfaces
There are also lower level interfaces in the module.
For example, the above interfaces also exist with POSIX timestamps in milliseconds instead of datetime objects. These timestamps have exactly the same resolution as the time axis of the resulting array.


### Example python-script

[example.py](example.py)


## Use as command line interface

Example call (make sure that the current working directory is not inside idas2numpy):
```python -m idas2numpy "SILIXA" ~/iDAS/work/2024-05-10-desy/ 2024-05-10T10:01:00 2024-05-10T10:02:00 10 0 1000 10 default
```

For more information:
```python -m idas2numpy -h
```
