
def slicer(day):
    '''
    finds the column 'created' and uses that to split forms
    '''

    created_list = day.filter(regex='created').columns.tolist()

    return [day.loc[:,i:ii].columns.tolist()[:-1] for i,ii in zip(created_list, created_list[1:])]


#not finished

# def datetime_test(filename):
#     day = pd.read_excel(filename)
#     day_dates = day.filter(regex = 'date')
#     print(type(day_dates.dtypes != 'datetime64[ns]'))

#     print(day_dates.dtypes != 'datetime64[ns]')