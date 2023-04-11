#!/usr/bin/env python3

import subprocess
import math

# Get the battery information using acpi
acpi_output = subprocess.check_output(['acpi', '-b'])
acpi_formatted = acpi_output.decode('utf-8').split()[3].replace(',', '')
battery_percentage = int(acpi_output.decode('utf-8').split()[3].replace('%,', ''))

# Calculate the length of the progress bar
bar_length = 40
filled_length = math.ceil(bar_length * battery_percentage / 100)

# Create the progress bar string
bar = '[' + '=' * filled_length + ' ' * (bar_length - filled_length) + ']'

# Print the battery information
print(f'{bar} {battery_percentage}%')
