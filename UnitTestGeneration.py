import sys
import myAI
import re
class UnitTestGeneration():
    def __init__(self,sourceFileName='./testAIByPackage.py',unittestModelName="unittest",targetFileName="./testAIByPackage.test.py") -> None:
        pass
        self.sourceFile = sourceFileName
        self.targetFile = targetFileName
        self.unittestModel = unittestModelName
    
    def generateUnitTestFromScratch(self):
        # 读取整个文件内容
        with open(self.sourceFile, 'r') as file:
            sourceCode = file.read()
        unit_test_code_mes = f'{sourceCode}，请使用{self.unittestModel}库为这段python代码生成单元测试，请只返回可执行代码，不要返回其他无关内容'
        generate_unit_test_ai = myAI.myAI()
        uMes = {"role": "user", "content": unit_test_code_mes}
        
        generate_unit_test_ai.setUserMes(uMes)
        unit_test_code_res = generate_unit_test_ai.getAIresponse().content
        pattern = r'^```(?:python)?\n([\s\S]*?)\n```$'

        # 提取并返回代码部分
        match = re.search(pattern, unit_test_code_res)
        unit_test_code_resToFile = ""
        if match:
            unit_test_code_resToFile = match.group(1)
        else:
            unit_test_code_resToFile = unit_test_code_res
            
    
        aiStr_get_expla = f'{unit_test_code_resToFile}，请为这段代码生成行间注释,请只返回可执行代码，不要返回非代码内容'
        uMes_get_expla = {"role": "user", "content": f"{aiStr_get_expla}"}
        generate_unit_test_ai.setUserMes(uMes_get_expla)
        res_get_expla = generate_unit_test_ai.getAIresponse().content
        match = re.search(pattern, res_get_expla)
        code_and_expla_ToFile = ""
        if match:
            code_and_expla_ToFile = match.group(1)
        else:
            code_and_expla_ToFile = res_get_expla
        with open(f'{self.targetFile}', 'w',encoding='utf-8') as file:
            file.write(code_and_expla_ToFile)

    def generateUnitTestAndUpdate(self):
        # 读取整个文件内容
        with open(self.sourceFile, 'r') as file:
            sourceCode = file.read()
        with open(self.targetFile,'r') as file:
            existTestCode = file.read()
        unit_test_code_mes = f'{sourceCode}，请使用{self.unittestModel}库为这段python代码生成单元测试，{existTestCode}这是已有的单元测试内容，请在此基础上更新，请只返回可执行代码，请只返回更新的内容，不要返回原有内容,不要返回其他无关内容'
        generate_unit_test_ai = myAI.myAI()
        uMes = {"role": "user", "content": unit_test_code_mes}
        
        generate_unit_test_ai.setUserMes(uMes)
        unit_test_code_res = generate_unit_test_ai.getAIresponse().content
        pattern = r'^```(?:python)?\n([\s\S]*?)\n```$'

        # 提取并返回代码部分
        match = re.search(pattern, unit_test_code_res)
        unit_test_code_resToFile = ""
        if match:
            unit_test_code_resToFile = match.group(1)
        else:
            unit_test_code_resToFile = unit_test_code_res
            
    
        aiStr_get_expla = f'{unit_test_code_resToFile}，请为这段代码生成行间注释,请只返回可执行代码，不要返回非代码内容'
        uMes_get_expla = {"role": "user", "content": f"{aiStr_get_expla}"}
        generate_unit_test_ai.setUserMes(uMes_get_expla)
        res_get_expla = generate_unit_test_ai.getAIresponse().content
        match = re.search(pattern, res_get_expla)
        code_and_expla_ToFile = ""
        if match:
            code_and_expla_ToFile = match.group(1)
        else:
            code_and_expla_ToFile = res_get_expla
        with open(f'{self.targetFile}', 'w',encoding='utf-8') as file:
            file.write(code_and_expla_ToFile)
