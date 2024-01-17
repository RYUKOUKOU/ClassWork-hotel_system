from system import read_info 
def ql(room_id):
    data,data1,data2,data3 = read_info(room_id)
    if data == 'False':
        return 'mzr',0
    else:
        return 'qqql',1
    
def yes(response):
    if response.lower() == 'yes':
        return 'ただいま伺いします。'
    elif response.lower() == 'no':
        return 'ゆっくり休んでくださいます。'
    else:
        return 'ひとがいないですか？' 