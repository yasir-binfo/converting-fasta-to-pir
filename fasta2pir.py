
import glob

files = glob.glob('*.fasta')

for file in files:
    with open(file,'r') as f:
    
        l = f.readlines()
    
        n = ''
    
        out =  file.split('.')[0] + '_pir.pir'
    
        for x in range(len(l)):
        
            if '>' in l[x]:
                    if n != '':
                        n_list = list(n)
                        n_list[-1] = '*'
                        n_list.append('\n')
                        n = ''.join(n_list)
                
                    s =  l[x].split()[0][1:]
                
                    p = '>P1;' + s + '\n' + 'sequence:' + s + '::::::::' + '\n'
                
                    l[x] = p
                
            n += l[x]

n_list = list(n)
n_list[-1] = '*'
n_list.append('\n')
n = ''.join(n_list)
with open(out,'w') as w:
    w.write(n)
        
        
