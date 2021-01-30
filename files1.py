# **** Working with files *** #
# file-> particular sequence type in which each line is considered as string in that sequence.
file_path="D:\\DS\\mailSample.txt"
fl=open(file_path) # print(file) ->wont give any out wrt contents of file.
# When a file opened, it will be opened with a last addon 'EOF' line. So when we read/iterate through the lines, the file will get closed as it read the final 'EOF'.
no_of_lines=0
r=fl.read()
print(len(r))
print(r[:5])
for line in fl:
    no_of_lines+=1
    if line.startswith('From:'):
        print(line)
print(f'Line count: {no_of_lines}')


