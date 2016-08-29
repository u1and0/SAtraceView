import glob
import param
param=param.param()
path=[path_trace,path_png,path_robo]=[param['path_trace'], param['path_png'], param['path_robo']]

co_trace=glob.glob(path_trace+'*')
co_robo=glob.glob(path_robo+'*')

sl_trace=[i[-19:-4] for i in co_trace]
sl_robo=[i[-19:-4] for i in co_robo]




set_trace=set(sl_trace)
set_robo=set(sl_robo)

print('trace directory\n',len(sl_trace))
print('robocopy directory\n',len(sl_robo))
print(sorted(list(set_robo.difference(set_trace))))
