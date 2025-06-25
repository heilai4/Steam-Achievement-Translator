import asyncio
from googletrans import Translator as GT

async def translate_file(input_path):
    results = []
    async with GT() as translator:
        with open(input_path, "r", encoding="utf8") as f:
            lines = [line.strip() for line in f if line.strip()]
        translations = await translator.translate(lines, dest="zh-cn")
        # translate 支持批量翻译，返回列表
        for tr in translations:
            results.append(tr.text)
    return results

def translate_sync(input_path):
    return asyncio.run(translate_file(input_path))
def translate_and_save():
    """读取成就文件，翻译并保存到新文件"""
    input_file = "chengjiu.txt"
    output_file = "fanyi.txt"
    
    translated_lines = translate_sync(input_file)
    
    with open(output_file, "w", encoding="utf8") as f:
        for line in translated_lines:
            f.write(line + "\n")
    
    print(f"翻译完成，结果已保存到 {output_file}")

