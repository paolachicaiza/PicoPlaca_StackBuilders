## Coding Exercise
Write a "Pico y Placa" predictor. The inputs should be a license plate number (the full number, not the last digit), a date (as a String), and a time. The program should return whether or not that car can be on the road. You may use any input and output method you prefer. 

## Solution
### Explanation

The implementation contains four Classes: Vehicle, Validator, InputData, and Parser, also there is a class called Car that is inherited from Vehicle.

In the Validator class, there is the method "is_driving_allowed" that determines if any vehicle can circulate or not, this method returns a boolean parameter, True for "Driving allowed" and False for "Driving NOT allowed"

Using a dictionary, the project classifies the days as workdays and weekends, also there is a list of all holidays in Ecuador for this year. With respect to the shift hours for circulating, the program creates a specific period of time to restrict the circulation. The program analyzes if the plate is allowed to circulate on a specific date and hour.

The input of data for checking contains must the following structure:
plate,date(d-m-y),hour(24 hours format - h:m)
Example:
PDW-3265,27-04-2022,18:30
XDC-3565,01-01-2022,08:37

The main.py must have the name of the file that contains the data, the file can have one or more vehicles for checking. Finally, the project shows the following results:

PDW-3265 on 27-04-2022 at 18:30: Driving NOT allowed
XDC-3565 on 01-01-2022 at 08:37: Driving allowed


### Clone 
git clone https://github.com/paolachicaiza/PicoPlaca_StackBuilders

### Execute program
python ./src/main.py

## Run Unit Test
python -m unittest discover -s ./tests -p '*.py'