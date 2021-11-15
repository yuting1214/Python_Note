file_loc = os.path.normpath(r'C:\Users\l501l\Desktop\Financial_proj\data\休市日\raw_data')
file_path = [file_loc + '\\' + file for file in os.listdir(file_loc)]
df = pd.concat(map(pd.read_csv, file_path), ignore_index = True)
