# 📚 Update BibTeX Citation Keys in LaTeX Files ✨

Managing citations in academic writing can be a tedious task 😫, especially when updating references to match new BibTeX entries. This script automates the process 🤖 of updating citation keys in LaTeX `.tex` files, ensuring that your references are always up-to-date with the latest BibTeX entries. By using fuzzy string matching 🔍, it accurately matches old citation keys to new ones based on paper titles, saving researchers valuable time and effort! 🎉

在学术写作中管理引用可能是一项繁琐的任务 😫,尤其是在更改了Bibtex文件并改变了原来的引用键之后。该脚本自动化了在 LaTeX `.tex` 文件中更新引用键的过程 🤖,确保您的引用始终与最新的 BibTeX 条目保持一致。通过使用模糊字符串匹配 🔍,它可以根据论文标题准确地将旧引用键匹配到新的引用键,从而为研究人员节省宝贵的时间和精力!🎉

⚠️ **WARNING:** Create a backup of your paper latex file before running the script! (x3) ⚠️
⚠️ **注意:** 运行脚本前务必备份你的论文latex文件!(x3) ⚠️

## 🛠️ Requirements

- Python 3.x 🐍
- `fuzzywuzzy` library 🔧
- `bibtexparser` library 📖

You can install the required libraries using pip: 💻
```sh
pip install fuzzywuzzy bibtexparser
```

## 🚀 Usage

1. **Clone the repository:** 📥
```sh
git clone https://github.com/Xueheng-Li/updateBibTexKey.git
cd updateBibTexKey
```

2. **Set the paths to your files:** ⚙️
```python
# Configure your paths here! 🎯
old_bibs = [
'path/to/old_bib1.bib',
'path/to/old_bib2.bib',
]
new_bib = 'path/to/new_bib.bib'
tex_file_to_update = 'path/to/tex_file.tex'
```

3. **Run the script:** 🏃
```sh
python update_bib.py
```

4. **Check the output:** ✅

## 🔧 Functions

- 📖 `load_bib_entries()`: Loads BibTeX entries
- 🔄 `create_key_mapping()`: Creates citation key mappings
- 📚 `create_key_mapping_multi()`: Handles multiple BibTeX files
- ✏️ `update_tex_file()`: Updates your LaTeX files
- 📊 `print_change_report()`: Shows what changed
- 🎯 `main()`: Runs everything!

## 📝 Notes

- 🎯 Uses fuzzy matching for accurate title comparison
- ⚖️ Default matching threshold is 90%
- 🛠️ Feel free to customize the script!

---

# 中文说明 🇨🇳

该脚本根据新的 BibTeX 条目更新 LaTeX `.tex` 文件中的引用键。它使用模糊字符串匹配旧引用键和新引用键，基于论文的标题进行匹配。

## 要求

- Python 3.x
- `fuzzywuzzy` 库
- `bibtexparser` 库

您可以使用 pip 安装所需的库：

```sh
pip install fuzzywuzzy bibtexparser
```

## 使用方法

1. **克隆仓库：**

   从 GitHub 克隆仓库：

   ```sh
   git clone https://github.com/Xueheng-Li/updateBibTexKey.git
   cd updateBibTexKey
   ```

2. **设置文件路径：**

   编辑脚本开头的路径设置，指定旧的 BibTeX 文件、新的 BibTeX 文件和要更新的 LaTeX 文件的路径。

   ```python
   # old_bibs 是旧的 bib 文件，new_bib 是新的 bib 文件，tex_file_to_update 是要更新的 tex 文件
   old_bibs = [
       'path/to/old_bib1.bib',
       'path/to/old_bib2.bib',
   ]
   new_bib = 'path/to/new_bib.bib'
   tex_file_to_update = 'path/to/tex_file.tex'
   ```

3. **运行脚本：**

   使用 Python 执行脚本：

   ```sh
   python update_bib.py
   ```

4. **检查输出：**

   脚本将创建原始 `.tex` 文件的备份，扩展名为 `.bak`，并更新原始 `.tex` 文件中的引用。它还会打印更改报告。

## 函数

- `load_bib_entries(bib_file)`: 从文件加载 BibTeX 条目并返回标题到键的字典。
- `create_key_mapping(old_bib, new_bib, bar=90)`: 基于论文标题在旧引用键和新引用键之间创建映射。
- `create_key_mapping_multi(old_bibs, new_bib, bar=90)`: 从多个旧 BibTeX 文件到新引用键创建映射。
- `update_tex_file(tex_file, key_mapping)`: 使用备份更新 LaTeX 文件中的引用。
- `print_change_report(mapping, changes, show_detail=False)`: 打印引用键更改的详细报告。
- `main(old_bibs, new_bib, tex_file_to_update)`: 运行更新过程的主函数。

## 注意事项

- 该脚本使用模糊字符串匹配在旧的和新的 BibTeX 条目之间找到最佳匹配的标题。
- `create_key_mapping` 和 `create_key_mapping_multi` 函数中的 `bar` 参数设置模糊匹配比率的阈值（默认是 90%）。

请根据您的具体用例自由修改脚本。

Remember to backup your files before running! 💾 祝您使用愉快! 🎉
