from dateutil import parser
 
def get_safe_meta_data(meta_data_name):
    safe_meta = ''
    meta_data_value = document.get_meta_data_value(meta_data_name)
    if len(meta_data_value) > 0:
        safe_meta = meta_data_value[-1]
    return safe_meta
 
def get_modified_date(): 
    str_date = get_safe_meta_data('raw.version.createdate')
    #str_date: 2019-02-28 15:14:26Z
 
    date_date = parser.parse(str_date, fuzzy=True)
    #date_date:2019-02-28 15:14:26+00:00
 
    document.add_meta_data({'date':date_date})
 
get_modified_date()