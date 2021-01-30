file_path="D:\\DS\\test.txt"
fl=open(file_path)
out=0
count=0
for line in fl:
    if not line.startswith("X"):
        continue
    ind=line.find('0.')
    count += 1
    out=out+float((line[ind:]).strip())# Each line in a file ends with new line(\n). So striping the whitespaces.
print(out/count)