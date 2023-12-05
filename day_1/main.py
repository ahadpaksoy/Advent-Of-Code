# impoort regex library
import re
# Define the regular expression pattern
pattern = re.compile(r'\d', re.UNICODE)
# Define calibration sum  
sum = 0
# Open the file for reading
with open('C:\\Users\\Ahad Can PAKSOY\\OneDrive\\Masaüstü\\Advent-Of-Code\\day_1\\file.txt', 'r', encoding='utf-8') as file:
    # Process each line in the file
    for line in file:
        # Use the pattern to search for matches in the current line
        matches = pattern.findall(line)
        # Trim or extract information from the matches
        regex_result = [match.lower() for match in matches]
        # Merge first digit and last digit as calibration value
        calib_val = regex_result[0] + regex_result[-1]
        
        sum += int(calib_val)
        
print(f"sum of the calibration values = {sum}")

    
