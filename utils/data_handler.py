
def slicer(df):
    '''
    finds the column 'created' and uses that to split forms
    '''
    created_list = df.filter(regex='created').columns.tolist()
    return [df.loc[:,i:ii].columns.tolist()[1:-1] for i,ii in zip(created_list, created_list[1:])]

def dropper(df):
    c_drop = df.filter(regex = 'modified').columns #selects modified_by as well
    return df.drop(columns = c_drop)

df = pd.read_csv("0.88/browser_data.csv")

def convert_df(df):
    return df.to_csv().encode('utf-8')




#not finished

# def datetime_test(filename):
#     day = pd.read_excel(filename)
#     day_dates = day.filter(regex = 'date')
#     print(type(day_dates.dtypes != 'datetime64[ns]'))

#     print(day_dates.dtypes != 'datetime64[ns]')