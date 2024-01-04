with open('tau.txt', 'r') as f:
    lines = f.readlines()
lines = [line.replace(' ', '') for line in lines]
lines = [line.replace('\n', '') for line in lines]
with open('tau.txt', 'w') as f:
    f.writelines(lines)