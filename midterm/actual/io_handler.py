import os


#### DO NOT MODIFY ####
class IOHandler:
    def __init__(self, input_file=None, output_file=None):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.input_file = None
        if input_file:
            self.input_file = os.path.join(dir_path, input_file)

        self.output_file = None
        if output_file:
            self.output_file = os.path.join(dir_path, output_file)

    def read(self):
        # read from file
        if self.input_file:
            with open(self.input_file, 'r') as f:
                input_lines = f.readlines()
            return input_lines

        # read from stdin
        input_lines = []
        try:
            while True:
                input_lines.append(input())
        except EOFError:
            pass
        return input_lines

    def write(self, output_str):
        # write to file
        if self.output_file:
            with open(self.output_file, 'w') as f:
                f.writelines(output_str)
            return

        # write to stdout
        print(output_str)
        return
