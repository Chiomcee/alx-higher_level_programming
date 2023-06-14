#!/usr/bin/env python3
"""
After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

import sys

# Initialize the variables to store the metrics
total_file_size = 0
status_code_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

try:
    # Read from stdin line by line and compute the metrics
    for line in sys.stdin:
        # Parse the line to extract the file size and status code
        parts = line.split()
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        # Update the metrics
        total_file_size += file_size
        status_code_count[status_code] += 1
        line_count += 1

        # Print the metrics every 10 lines
        if line_count % 10 == 0:
            print(f'Total file size: File size: {total_file_size}')

            for code in sorted(status_code_count.keys()):
                if status_code_count[code] > 0:
                    print(f'{code}: {status_code_count[code]}')

# Handle keyboard interruption (CTRL + C) and print the final metrics
except KeyboardInterrupt:
    print(f'Total file size: File size: {total_file_size}')

    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f'{code}: {status_code_count[code]}')
