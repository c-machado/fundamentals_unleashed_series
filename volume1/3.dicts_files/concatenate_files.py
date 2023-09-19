class ConcatenateFiles:

    def concat_files():
        with open("/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/test_at.txt", 'r') as file1:
            data_file1 = file1.read()
            
        with open("/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/test_2.txt", 'r') as file2:
            data_file2 = file2.read()
        
        data_file1 += "\n"
        data_file1 += data_file2

        with open ('/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/file3.txt', 'w') as file3:
            file3.write(data_file1)

    def concat_txt_files():
        try:
             with open("/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/test_at.txt", 'r') as file1:
                data_file1 = file1.read()
            
             with open("/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/test_2.txt", 'r') as file2:
                data_file2 = file2.read()

             with open ('/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/file3.txt', 'w') as file3:
                file3.write(data_file1)
                file3.write(data_file2)

            #  print(f'ConcatenateFiles{}')
        except FileNotFoundError:
            print(f'file not found')
        except Exception as e:
            print(f'un error has occured {str(e)}')

if __name__ == "__main__":


    ConcatenateFiles.concat_txt_files()