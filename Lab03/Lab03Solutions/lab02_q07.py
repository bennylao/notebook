import sys
arg_list = sys.argv
no_args = len(sys.argv)



def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

not_readable_files  = []
for i in range(1,no_args):
    try:
        line_count = file_len(arg_list[i])
        print(arg_list[i], line_count)
    except:
        not_readable_files.append(arg_list[i])


print('The following file(s) are not readable: ', not_readable_files)
