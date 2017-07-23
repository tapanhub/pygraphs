import csv
import sys
import os
import matplotlib.pyplot as plt

'''
	MemTotal:         109300 kB
MemFree:            5520 kB
Buffers:            1220 kB
Cached:            61592 kB
	SwapCached:            0 kB
Active:            24160 kB
Inactive:           8332 kB
Active(anon):      16400 kB
Inactive(anon):        0 kB
Active(file):       7760 kB
Inactive(file):     8332 kB
Unevictable:       46720 kB
Mlocked:               0 kB
	SwapTotal:             0 kB
	SwapFree:              0 kB
Dirty:                 0 kB
Writeback:             0 kB
AnonPages:         16420 kB
Mapped:             5284 kB
	Shmem:                 0 kB
Slab:              12668 kB
SReclaimable:       4164 kB
SUnreclaim:         8504 kB
KernelStack:         696 kB
PageTables:          792 kB
	NFS_Unstable:          0 kB
	Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:       54648 kB
Committed_AS:      36004 kB
VmallocTotal:    1048372 kB
VmallocUsed:         764 kB
VmallocChunk:    1034836 kB
MemTotal SwapCached SwapTotal SwapFree Shmem NFS_Unstable Bounce
'''

def main(argv):
	x = []
	y = []
	print argv[1]
	s=0
	a=[]
	d={}

	with open(argv[1]) as csvfile:
		z=[]
		#data = csv.reader(csvfile, delimiter=r"\s+")
		data = csvfile.readlines()
		for row in data:
			if ':' in row:
				r =  row.split()
				if r[0] == 'MemTotal:':
					if len(d) != 0:
						a.append(d)
						d={}
				d[(r[0].split(':'))[0]]=int(r[1])
						
	mem={}
	ignorelist='MemTotal SwapCached SwapTotal SwapFree Shmem NFS_Unstable Bounce'
	for key in a[0].keys():
		if key in ignorelist:
			continue
		mem[key]=[ x[key] for x in a ]
		plt.plot(range(len(mem[key])), mem[key], label=key)
		plt.title('meminfo graph')
		plt.xlabel('time')
		plt.ylabel('memory in Kbytes')
		plt.grid(True)
		plt.legend()
		plt.savefig(argv[1] + "_"+key+".png")
		plt.close()

if __name__ == '__main__':
	try:
		main(sys.argv)
	except KeyboardInterrupt:
		print 'Interrupted'
	try:
		sys.exit(0)
	except SystemExit:
		os._exit(0)
