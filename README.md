# Large-PDF-Translator 🚀
![Version](https://img.shields.io/badge/version-1.0.0-blue) ![License](https://img.shields.io/badge/license-Apache%202.0-green) ![Python](https://img.shields.io/badge/python-3.x-orange)

**专门为超长 PDF（1000+ 页）设计的稳健型自动化翻译工具。**

### 🌟 项目背景
本项目诞生于翻译一本 **1604 页** 著作的实战需求。针对大型 PDF 在翻译过程中常见的 Google 接口限流、网络中断、以及 Windows CMD 环境下的中文乱码问题进行了深度优化。

### ✨ 核心功能
- **断点续传**：程序意外中断？没关系，重启后自动检测 `--- Page X ---` 标记并从上一页无缝继续。
- **环境自适应**：自动强制开启 UTF-8 编码，彻底解决 Windows 终端下的方框乱码。
- **稳健请求策略**：内置随机延迟与深度休息模式（每 30 页休眠 60s），尊重 API 频率限制，确保持续稳定运行。
- **分卷处理**：配套提供 `split.py`，轻松将长文本按需切分，方便导入云端编辑器。

### 📦 安装与使用

1. **克隆仓库或下载脚本**
2. **安装必要依赖**：
   ```bash
   pip install PyMuPDF googletrans==4.0.0-rc1
3. **运行翻译程序：
   python trans.py source.pdf output.txt
4. **(可选) 分割翻译结果
   python split.py output.txt 801

   ⚖️ 开源协议
本项目采用 Apache License 2.0。请在法律允许的范围内使用，并尊重原著版权。

Developed with ❤️ on a ThinkPad T550.
