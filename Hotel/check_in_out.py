
from system import read_info,save_info

def check_in(fjh,zy,xm,dh,sj):
    room_data = read_info(fjh)
    if room_data[0] == 'True':
        return 'Error1'
    else:
        if save_info(fjh,zy,xm,dh,sj):
            return 'Check in'
        else:
            return 'Error2'

def check_out(fjh):
    room_data = read_info(fjh)
    if room_data[0] == 'False':
        return 'Error3'
    else:
        save_info(fjh,'False','','','')
        return 'Check out'

# print(check_in(2, 'True', 'AAA', '09012345678', '2023-12-14 18:17:01.501492'))
# print(check_out(2))
# check_in(1, True, 'AAA', '09012345678', '2023-12-14 18:17:01.501492')
# check_out(1, False, 'None', '0', '0')
