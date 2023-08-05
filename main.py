import modelCplexMIP
import datareading
import cplex
import os
import glob

# problem_name = ['Flowshop','Non-Flowshop','Hybridflowshop','Distributedflowshop','Nowaitflowshop','Setupflowshop',
# 'Tardinessflowshop','TCTflowshop','Jobshop','Flexiblejobshop','Openshop','Parallelmachine']
# modelType = ['CP','MIP']
# Solver = ['CPLEX','Groubi','Google','Xpress']


def createMoedl(filename):

    path, file_with_ext = os.path.split(filename)
    parent_path, dir_name = os.path.split(path)
    file_name, ext = os.path.splitext(file_with_ext)

    '''
    存放生成的mps文件的地址
    '''
    target_folder = 'G:\\MpsData\\'
    modelType = 'MIP'
    '''
    算例的类别，跟文件夹名字一样
    '''
    problemType = 'Hybridflowshop'
    instance = datareading.dataentry(filename, problemType)  # The OpenStack does not allow subdirectories for instances
    mdl = cplex.Cplex()
    mdl = modelCplexMIP.MIPmodel_generation(instance, mdl, problemType)

    # 求解
    # mdl.solve()
    # 写入本地
    target_folder += (dir_name+'\\'+file_name + '.mps')
    print(target_folder)
    mdl.write(target_folder)



'''
算例文件夹名称,里面都是txt文件
'''
folder_path = r"D:\PythonProject\2021.0326-master\data\Hybridflowshop"
txt_files = glob.glob(os.path.join(folder_path, '*.txt'))

# 输出所有.txt文件的完整路径
for txt_file in txt_files:
    print(txt_file)
    createMoedl(txt_file)