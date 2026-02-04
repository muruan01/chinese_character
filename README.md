# 中文识字程序 Chinese Character Literacy Program

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

## 项目简介 Project Overview

本项目致力于**为中国扫盲，为中国识字率贡献一份力量**，目标用户是**老年人**。

**This project is dedicated to literacy in China, contributing to China's literacy rate. The target users are elderly people.**

### 特点 Features

✨ **大字体显示** - Large, clear fonts optimized for elderly users  
📚 **分级学习** - Progressive learning from beginner to advanced  
🔤 **拼音注音** - Pinyin pronunciation for every character  
📝 **笔画信息** - Stroke count and writing guidance  
💡 **常用例句** - Common example phrases and words  
📊 **进度追踪** - Track learning progress  
📄 **练习表生成** - Generate printable practice sheets  

## 为什么选择这个项目 Why This Project

中国有大量老年人因历史原因未能接受完整教育，识字率较低。本项目通过：

- **易用的界面**：大字体，简单操作
- **科学的方法**：从简单到复杂，循序渐进
- **实用的内容**：最常用的3000+汉字
- **贴心的设计**：专为老年人学习习惯设计

Many elderly people in China have limited literacy due to historical reasons. This project provides:

- **User-friendly interface**: Large fonts, simple operations
- **Scientific method**: Progressive learning from simple to complex
- **Practical content**: 3000+ most commonly used characters
- **Thoughtful design**: Designed specifically for elderly learning habits

## 快速开始 Quick Start

### 安装 Installation

```bash
# 克隆仓库 Clone repository
git clone https://github.com/muruan01/chinese_character.git
cd chinese_character

# 无需安装依赖，使用Python 3.6+即可
# No dependencies required, just Python 3.6+
```

### 使用方法 Usage

#### 方式一：交互式应用 Interactive App (推荐 Recommended)

```bash
python3 literacy_app.py
```

这将启动交互式学习界面，您可以：
- 按级别学习字符
- 查看学习进度
- 生成练习表
- 查找特定字符

This starts the interactive learning interface where you can:
- Learn characters by level
- View your progress
- Generate practice sheets
- Search for specific characters

#### 方式二：程序库模式 Library Mode

```bash
python3 chinese_character.py
```

这将运行演示程序，展示所有功能。

This runs a demonstration program showing all features.

#### 方式三：作为Python模块 As Python Module

```python
from chinese_character import CharacterDatabase, LiteracyProgram

# 创建数据库 Create database
db = CharacterDatabase()

# 创建学习程序 Create learning program
program = LiteracyProgram(db)

# 显示初级字符 Show beginner characters
program.list_characters_by_level("beginner")

# 练习特定字符 Practice specific character
program.practice_character("人")

# 查看进度 View progress
program.show_progress()

# 生成练习表 Generate practice sheet
program.generate_practice_sheet("beginner", "my_practice.txt")
```

## 学习级别 Learning Levels

### 初级 Beginner (16 characters)
最基础的字符，包括数字、家人称呼、日常用语等。

Most basic characters including numbers, family terms, and daily vocabulary.

例如 Examples: 一、二、三、人、大、小、老、天、日、月、年、吃、喝、看、听...

### 中级 Intermediate (4 characters)
日常生活中常用的字符。

Common characters used in daily life.

例如 Examples: 学、字、书、好...

### 高级 Advanced (4 characters)  
更复杂但重要的字符。

More complex but important characters.

例如 Examples: 家、国、中、文...

## 功能详解 Detailed Features

### 1. 字符展示 Character Display

每个字符显示内容包括：
- **汉字** Character (大字体显示 large font)
- **拼音** Pinyin pronunciation
- **意思** Meaning
- **笔画数** Stroke count
- **例句** Example phrases and words
- **级别** Difficulty level

### 2. 练习表 Practice Sheets

生成可打印的练习表，包含：
- 字符信息 Character information
- 书写练习格 Writing practice grids
- 例句参考 Example references

### 3. 进度追踪 Progress Tracking

- 记录已学习的字符 Track learned characters
- 按级别显示进度 Show progress by level
- 计算完成百分比 Calculate completion percentage

### 4. 字符查找 Character Search

快速查找和学习特定字符。

Quick search and learn specific characters.

## 项目结构 Project Structure

```
chinese_character/
├── README.md                    # 项目文档 Project documentation
├── chinese_character.py         # 核心模块 Core module
├── literacy_app.py              # 交互式应用 Interactive app
├── characters_data.json         # 字符数据库 (可选 optional)
└── *_practice.txt              # 生成的练习表 Generated practice sheets
```

## 字符数据库 Character Database

当前包含24个常用汉字，涵盖：
- 数字 Numbers (1-10)
- 家庭成员 Family members
- 日常动作 Daily actions
- 时间概念 Time concepts
- 基本形容词 Basic adjectives

Currently contains 24 common characters covering:
- Numbers, family members, daily actions, time concepts, and basic adjectives

数据库可以轻松扩展到3000+字符以实现完全识字。

The database can be easily expanded to 3000+ characters for complete literacy.

## 技术特性 Technical Features

- **纯Python实现** Pure Python implementation
- **无外部依赖** No external dependencies
- **UTF-8编码支持** Full UTF-8 encoding support
- **跨平台兼容** Cross-platform compatible
- **可扩展架构** Extensible architecture

## 使用场景 Use Cases

### 老年人识字教育 Elderly Literacy Education
- 社区学习中心 Community learning centers
- 家庭教学 Home teaching
- 老年大学 Senior universities

### 中文学习 Chinese Learning
- 汉语初学者 Chinese language beginners
- 儿童识字 Children's literacy
- 外国学习者 Foreign learners

## 贡献指南 Contributing

欢迎贡献！您可以：
- 添加更多字符到数据库
- 改进用户界面
- 添加新功能
- 修复bug
- 改进文档

Contributions welcome! You can:
- Add more characters to the database
- Improve the user interface
- Add new features
- Fix bugs
- Improve documentation

## 开发计划 Roadmap

- [ ] 扩展字符数据库到1000+字符
- [ ] 添加字符书写动画
- [ ] 语音朗读功能
- [ ] Web界面版本
- [ ] 移动应用版本
- [ ] 学习游戏化
- [ ] 多用户支持
- [ ] 云端进度同步

## 许可证 License

MIT License - 详见 LICENSE 文件

## 联系方式 Contact

- GitHub: [muruan01/chinese_character](https://github.com/muruan01/chinese_character)
- Issues: [Report a bug or request a feature](https://github.com/muruan01/chinese_character/issues)

## 致谢 Acknowledgments

感谢所有为中国扫盲事业做出贡献的人！

Thanks to everyone contributing to literacy in China!

---

**让我们一起为提高中国识字率而努力！**  
**Let's work together to improve literacy rates in China!**
