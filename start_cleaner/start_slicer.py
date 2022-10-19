
def excel_slicer(filename):
    day_90 = pd.read_excel(filename)

    created_list = day_90.filter(regex='created').columns.tolist()

    return [day_90.loc[:,i:ii].columns.tolist()[6:-1] for i,ii in zip(created_list, created_list[1:])]


#not finished

def datetime_test(filename):
    day = pd.read_excel(filename)
    day_dates = day.filter(regex = 'date')
    print(type(day_dates.dtypes != 'datetime64[ns]'))

    print(day_dates.dtypes != 'datetime64[ns]')