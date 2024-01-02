import matplotlib.pyplot as plt

def read_file_to_list(filename:str)->list:
    """Reads a text file with line-seperated data and returns a list assembling them

    Args:
        filename (str): name of the file

    Returns:
        list: list of data (read top down) 
    """
    with open(filename, 'r') as fp:
        data_list=fp.readlines()
    return [float(i) for i in data_list] # convert items into float and return

def main():
    FILE_NAME='databank.dat'
    plt.plot(read_file_to_list(filename=FILE_NAME))
    plt.show()

if __name__ =='__main__':
    main()