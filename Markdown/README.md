# MarkdownScript
一些辅助进行Markdown预处理的脚本，比如把所有()[]链接设置为在新标签页打开

# 如何使用
确保安装了Python 2.x 版本（推荐Python 2.7以上，不保证Python 3可以运行）

```bash
$ python --version
Python 2.7.6
```

所有脚本建议加入可执行权限

```bash
$ chmod +x ./LinksNewTab.py
```

执行

```bash
$ ./LinksNewTab.py
```

# 工具介绍

1. LinksNewTab.py
	
	`功能` :将所有当前目录下的Markdown文本中的```($a)[$b]```超链接替换为HTML形式的```<a href='$b' target='_blank'>$a</a>```，这样Markdown转换出来的链接可以在新标签页打开而不是在当前页面打开。
	
	`说明` :强迫症专用，尤其转换出来的HTML要放在iframe里面的时候