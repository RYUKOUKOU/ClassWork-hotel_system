
from system import read_info,save_info

def check_in(fjh,zy,xm,dh,sj):
    save_info(fjh,zy,xm,dh,sj)

def check_out(fjh,zy,xm,dh,sj):
    save_info(fjh,zy,xm,dh,sj)

check_in(1, True, 'AAA', '09012345678', '2023-12-14 18:17:01.501492')
check_out(1, False, 'None', '0', '0')