from io_handler import IOHandler
from a1 import reverse


INPUT_FILE = 'a1.in'

#### DO NOT MODIFY ####
if __name__ == '__main__':
    ioh = IOHandler(input_file=INPUT_FILE)
    input_lines = ioh.read()
    input_data = ''.join(input_lines).strip()

    output_data = []
    for line in input_lines:
        # Problem a1
        result = reverse(line)
        output_data.append(result)

    output_str = '\n'.join(output_data)
    ioh.write(output_str)
