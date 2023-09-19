class ReadFile:

    def read_txt_file():
        try:
            with open("/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/test_at.txt", 'r') as file:
                lines = file.readlines()
                # for i, line in enumerate(lines):
                #     if i%2 == 0:
                #         line.strip()
                #         print(line)
                odd_line = [line.strip() for i, line in enumerate(lines) if i%2 == 0]
                print(odd_line)
        except FileNotFoundError:
            print(f'file not found {file}')
        except Exception as e:
            print(f'un error has occured {str(e)}')

if __name__ == "__main__":

    ReadFile.read_txt_file()
