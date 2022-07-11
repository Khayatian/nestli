# nestli
*nestli* is the virtual sister of the NEST demonstrator at Empa. It is a co-simulation environment for benchmarking the performance of building automation and control systems. In its core, *nestli* is a calibrated EnergyPlus model of the UMAR living lab. see: https://www.empa.ch/web/nest/urban-mining

![Picture1](https://user-images.githubusercontent.com/27851066/169803496-275ed8fc-7d1b-42e6-a0a7-f27f7dc456c5.png)

The calibrated EnergyPlus model is wrapped into a fucntional mock-up unit using the EnergyPlusToFMU tool. see: https://simulationresearch.lbl.gov/fmu/EnergyPlus/export/

The model is calibrated on measurements that are collected at 1-minute intervals, and thus, runs at the same temporal resolution. The HVAC system can be controlled by overriding the setpoint temperature in each room. It is also possible to evaluate the robustness of a controller by manipulating weather conditions or the building operation.

![Picture3](https://user-images.githubusercontent.com/27851066/177743252-245372b8-5d8f-46c5-a06d-f375e4154ec1.png)

## Installation
#### Energyplus
1. Install Energyplus 9.3.0
2. Add it to your PATH

#### Python
1. Install python version 3.8 or higher.
2. Create a virtual environment: ```python -m venv path/to/env/dtpy-venv```
3. Activate the environment.
4. Clone the repository onto you machine
5. cd to the directory where you cloned it into
6. Install the package with: ```pip install -e . ``` This will install the dtpy package according to setup.py.

## Usage
A simple example of how to use the package is given in the **example** folder. Just run the file dtpy_example_run.py where the config example_config.yml specifies all the parameters.

## Contact
Fazel Khayatian, Urban Energy Systems Laboratory, Empa.
https://www.empa.ch/web/khfa
