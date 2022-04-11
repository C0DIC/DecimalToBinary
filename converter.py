import os, time


class Converter:


    def __init__(self):
        self.input_data    = None
        self.output_data   = None

        self.os_type       = os.name


    def starter(self):
        print('Write number in decimal system: ', end = '')

    
    def main(self):

        if self.os_type == 'nt':
            os.system('cls')
        else:
            os.system('clear')

        self.starter()

        self.output_data = self.converter(input(""))

        if self.output_data is None:
            pass
        else:
            print(f"{self.input_data} in decimal system is {self.output_data}")


    def converter(self, input_data) -> int:
        self.input_data = input_data

        try:
            new_input_data = int(self.input_data)

            output_data = []

            while (new_input_data / 2)!= 0:
                output_data.append(new_input_data % 2)
                new_input_data = new_input_data // 2

            output_data = output_data[::-1]
            new_output_data = ""

            for x in output_data:
                new_output_data += str(x)

            return new_output_data 
        except (TypeError, ValueError):
            print("Input data can not be converted to integer, please try again")
            time.sleep(2)
            self.main()

cv = Converter()
cv.main()