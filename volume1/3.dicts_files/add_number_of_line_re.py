class numberLines:

    def insert_number_lines():
        try:
            with open("/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/test_at.txt", 'r') as file1:
                lines = file1.readlines()
                line_with_number = ['line '+str(i+1)+'. ' + line.strip() for i, line in enumerate(lines)]
                
            with open ('/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/file4.txt', 'w') as file4:
                for line in line_with_number:
                    print(line)
                    file4.writelines(line)
        except FileNotFoundError:
            print(f'file not found')
        except Exception as e:
            print(f'un error has occured {str(e)}')

if __name__ == "__main__":
    numberLines.insert_number_lines()