import os
import geopandas as gpd

def prepend_line(file_name, var_name):
    """ Insert given string as a new line at the beginning of a file """
    line= 'var ' + var_name + ' = '
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    # open original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write given line to the dummy file
        write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)
    
    
def export_js(geodf, file_name, var_name):
    try:
        geodf.to_file(file_name, driver='GeoJSON')
        print('GeoDataFrame exported withouth issues')
    except Exception as e:
        print('GeoDataFrame export failed.')
        print(e)
    try:
        prepend_line(file_name, var_name)
        print('Line inserted correctly')
    except Exception as e:
        print('Line inserction failed.')
        print(e)