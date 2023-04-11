# BatteryLevel
A Python script that displays the current battery level as a progress bar using the `acpi` command. The script calculates the length of the progress bar based on the current battery percentage, and prints the progress bar and battery percentage to the console.

`python batteryLevel.py `
`[======================================  ] 93%`

# Requirements

This script requires the acpi command to be installed on your system. acpi is usually available in the package repositories of most Linux distributions.
Installation

    Download the batteryLevel.py script to your computer.
    Open a terminal and navigate to the directory where you downloaded the script.
    Make the script executable by running the command chmod +x batteryLevel.py.

# Usage

To display the current battery level as a progress bar, run the batteryLevel.py script from a terminal by typing:


bash

`python ./PATH/TO/batteryLevel.py`


The script will display the battery level as a progress bar with a length of 40 characters. The progress bar will be filled based on the current battery percentage, and the percentage will be displayed to the right of the progress bar.

# License

This script is released under the MIT license. Feel free to use, modify, and distribute the script as you see fit.
