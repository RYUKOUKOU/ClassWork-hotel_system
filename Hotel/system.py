def read_line(fjh):
    with open('data.txt', 'r') as f:
        for current_line_number, line_content in enumerate(f, 1):
            if current_line_number == fjh:
                return line_content.strip()
    return None
def save_line(fjh,info):
     with open('data.txt', 'r') as f:
        for current_line_number, line_content in enumerate(f, 1):
            if current_line_number == fjh:
                return True


def save_info(fjh,zy,xm,dh,sj):
    with open('data.txt', 'w') as f:
        content = f.read()
        print(content)

def read_info(fjh):
   info=read_line(fjh)
