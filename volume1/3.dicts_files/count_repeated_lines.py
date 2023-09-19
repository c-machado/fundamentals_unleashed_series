class compareFileLines:

    def compare_content_of_lines():
        try:
            with open("/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/test_at.txt", 'r') as file1:
                lines_file_1 = file1.readlines()
            with open("/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/test_2.txt", 'r') as file2:
                lines_file_2 = file2.readlines()
                cont_same_content=0
                cont_diff_content=0
                for line_1, line_2 in zip(lines_file_1, lines_file_2): 
                       if line_1 == line_2:
                            cont_same_content+=1
                            print(f'line1 {line_1}, line_2{line_2}')
                       else:
                            cont_diff_content+=1
                            print(f'line1 {line_1}, line_2{line_2}')

                print(cont_same_content)
                print(cont_diff_content)
           
        except FileNotFoundError:
            print(f'file not found')
        except Exception as e:
            print(f'un error has occured {str(e)}')

if __name__ == "__main__":

    compareFileLines.compare_content_of_lines()