# Copyright 2026 duanmeihua
# Licensed under the Apache License, Version 2.0
# Version: 1.0.0

__version__ = "1.0.0"

import sys, os, time, random, fitz
from googletrans import Translator

def main():
    print(f"=== Lester PDF Translator v{__version__} ===")
    if len(sys.argv) < 3:
        print("用法: python trans.py <输入PDF> <输出TXT>")
        return
    
    input_pdf, output_txt = sys.argv[1], sys.argv[2]
    translator = Translator()
    
    if sys.platform == "win32": os.system('chcp 65001 > nul')

    start_page = 0
    if os.path.exists(output_txt):
        with open(output_txt, 'r', encoding='utf-8') as f:
            for line in reversed(f.readlines()):
                if "--- Page " in line:
                    try:
                        start_page = int(line.split("--- Page ")[1].split(" ---")[0])
                        break
                    except: continue

    doc = fitz.open(input_pdf)
    for i in range(start_page, len(doc)):
        try:
            text = doc.load_page(i).get_text()
            if text.strip():
                res = translator.translate(text, dest='zh-cn').text
                with open(output_txt, 'a', encoding='utf-8') as f:
                    f.write(f"\n\n--- Page {i+1} ---\n\n{res}")
                print(f"进度: {i+1}/{len(doc)}")
            time.sleep(random.uniform(2, 5))
            if (i + 1) % 30 == 0: time.sleep(60)
        except Exception as e:
            print(f"错误: {e}")
            time.sleep(10)

if __name__ == "__main__":
    main()
