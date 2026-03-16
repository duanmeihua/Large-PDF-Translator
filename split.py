# Copyright 2026 duanmeihua
# Licensed under the Apache License, Version 2.0
import sys, os

def main():
    if len(sys.argv) < 3:
        print("用法: python split.py <源文件> <分割页码>")
        return
    
    src, page_num = sys.argv[1], sys.argv[2]
    marker = f"--- Page {page_num} ---"
    
    if not os.path.exists(src): return
    
    with open(src, 'r', encoding='utf-8') as f:
        content = f.read()

    if marker in content:
        parts = content.split(marker)
        name, ext = os.path.splitext(src)
        with open(f"{name}_P1{ext}", 'w', encoding='utf-8') as f1: f1.write(parts[0])
        with open(f"{name}_P2{ext}", 'w', encoding='utf-8') as f2: f2.write(marker + parts[1])
        print("分割完成！")