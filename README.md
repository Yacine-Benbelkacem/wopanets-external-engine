
# wopanet-external-engine


Plugin for wopanets tool to analyze AFDX networks' end to end delays, backlogs, and links loads.




## Features

- The switching technique is hard-coded as "cut-through".

- The service curves are hard-coded as C(t) curves (fifo buffers).


## Usage

From  WoPANets GUI :

- Put the content of this repo into ~/Documents/WoPANets/external/

-  Launch WoPANets

- Tools > Custom Analysis > Calculation : ExternCalcul > engine_main.py


From command line : 

```
python3 engine_main.py ./input/<afdx_file_name>.xml
```

#### Warning : 

The input units shall be as follow : 

- Capacity : bits per second 
- Latency : microseconds
- Period : milliseconds
- Deadline : milliseconds




## Demo/Results


![App Screenshot](./diagrams/backlogs_distribution.png)




## Authors

- [@Yacine BEN BELKACEM](https://github.com/Yacine-Benbelkacem)

