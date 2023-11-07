with open('RaceBenchData/temp.txt', 'r') as infile, open('RaceBenchData/list.txt', 'w') as outfile:
    current_line = 1  # Initialize the current line counter

    for line in infile:
        # Check if the current line is within the specified range
        if 71 <= current_line <= 75:
            print(line.strip())
            outfile.write(line)  # Write the line to the output file
        current_line += 1  # Increment the current line counter
