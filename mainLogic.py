import sys
from UnitTestGeneration import UnitTestGeneration
import os
def getParam(par_args):
    
    par_args=['--path=myAI.py',"--lib=unittest"]
    par_args_useful = {}
    if isinstance(par_args, list):
        for arg in par_args:
            if "path" in arg:
                # 找到等号的位置
                j = arg.index("=") + 1
                # 提取等号后面的内容
                path_value = arg[j:]
                par_args_useful['path'] = path_value
            elif "lib" in arg:
                # 处理lib的情况 (可以根据需求实现)
                j = arg.index("=") + 1
                lib_value = arg[j:]
                par_args_useful["lib"] = lib_value
            else:
                # 处理其他参数的情况 (可以根据需求实现)
                return None
        return par_args_useful
    else:
        return None
def check_file_exists(filename):
    # 获取当前项目的根目录
    current_directory = os.getcwd()
    # 拼接完整的文件路径
    file_path = os.path.join(current_directory, filename)
    
    # 检查文件是否存在
    if os.path.exists(file_path):
       
        return True
    else:
    
        return False
def add_test_to_filename(filename):
        # 分离文件名和后缀
        name, extension = filename.rsplit('.', 1)
        # 构造新的文件名
        new_filename = f"{name}.test.{extension}"
        return new_filename
def __main__():
    parameters = getParam(sys.argv) 
    sourcePath = ''
    testLib = ""

    if isinstance(parameters,dict):
        sourcePath = parameters['path']
        testLib = parameters['lib']
    else:
        print('请按照格式：--path=sourcefiledirectory --lib=unittestlib 输入参数')
    targetFile = add_test_to_filename(sourcePath)
    unitTest_generate = UnitTestGeneration(sourcePath,testLib,targetFile)
    
    if check_file_exists(targetFile):
        unitTest_generate.generateUnitTestAndUpdate()
    else:
        unitTest_generate.generateUnitTestFromScratch()
    
__main__()
