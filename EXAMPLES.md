# 使用示例 Usage Examples

本文档提供程序使用的具体示例。
This document provides specific examples of how to use the program.

---

## 示例 1: 基本使用 Basic Usage

### 运行主程序 Run Main Program

```bash
python3 chinese_character.py
```

**输出 Output:**
```
╔══════════════════════════════════════════════════════════════╗
║           中文识字学习程序                                    ║
║      Chinese Character Literacy Program                     ║
║           专为老年人设计                                      ║
║         Designed for Elderly Users                          ║
╚══════════════════════════════════════════════════════════════╝

字库统计 Character Database Statistics:
  • 初级 Beginner: 16 characters
  • 中级 Intermediate: 4 characters  
  • 高级 Advanced: 4 characters
  • 总计 Total: 24 characters
```

---

## 示例 2: 交互式学习 Interactive Learning

### 启动交互式应用 Start Interactive App

```bash
python3 literacy_app.py
```

### 操作流程 Operation Flow

1. **主菜单 Main Menu**
   ```
   请选择 Please select:
     1. 学习初级字符    Learn Beginner Characters
     2. 学习中级字符    Learn Intermediate Characters
     3. 学习高级字符    Learn Advanced Characters
     4. 查看学习进度    View Progress
     5. 生成练习表      Generate Practice Sheet
     6. 查找字符        Search Character
     7. 帮助           Help
     0. 退出           Exit
   ```

2. **输入 1** 学习初级字符
   
3. **查看字符信息**
   ```
   ============================================================
   字 Character: 一  (笔画 Strokes: 1)
   拼音 Pinyin: yī
   意思 Meaning: one, 一
   级别 Level: beginner
   
   例子 Examples:
     1. 一个人 (one person)
     2. 一天 (one day)
   ============================================================
   ```

4. **导航选项 Navigation Options**
   - 输入 `n` - 下一个字符
   - 输入 `p` - 上一个字符
   - 输入 `b` - 返回主菜单

---

## 示例 3: 作为 Python 模块使用 Use as Python Module

### 导入模块 Import Module

```python
from chinese_character import CharacterDatabase, LiteracyProgram, ChineseCharacter
```

### 创建字符 Create a Character

```python
# 创建一个新字符
char = ChineseCharacter(
    char="学",
    pinyin="xué", 
    meaning="study, learn",
    strokes=8,
    level="intermediate",
    examples=["学习 (study)", "学生 (student)"]
)

# 显示字符信息
print(char.display(large_font=True))
```

**输出 Output:**
```
============================================================
字 Character: 学  (笔画 Strokes: 8)
拼音 Pinyin: xué
意思 Meaning: study, learn
级别 Level: intermediate

例子 Examples:
  1. 学习 (study)
  2. 学生 (student)
============================================================
```

### 使用数据库 Use Database

```python
# 创建数据库
db = CharacterDatabase()

# 获取统计信息
stats = db.get_statistics()
print(f"总字数 Total: {stats['total']}")
print(f"初级 Beginner: {stats['beginner']}")

# 按级别获取字符
beginner_chars = db.get_by_level('beginner')
print(f"初级字符数量: {len(beginner_chars)}")

# 查找特定字符
char = db.get_by_char('人')
if char:
    print(f"找到了: {char.char} - {char.meaning}")
```

**输出 Output:**
```
总字数 Total: 24
初级 Beginner: 16
初级字符数量: 16
找到了: 人 - person, human, 人
```

### 使用学习程序 Use Learning Program

```python
# 创建学习程序
program = LiteracyProgram(db)

# 显示欢迎信息
program.show_welcome()

# 列出初级字符
program.list_characters_by_level("beginner", large_font=True)

# 练习特定字符
program.practice_character("人")
program.practice_character("大")
program.practice_character("小")

# 查看进度
program.show_progress()

# 生成练习表
program.generate_practice_sheet("beginner", "my_practice.txt")
```

---

## 示例 4: 生成练习表 Generate Practice Sheet

### Python 代码 Python Code

```python
from chinese_character import CharacterDatabase, LiteracyProgram

db = CharacterDatabase()
program = LiteracyProgram(db)

# 生成初级练习表
program.generate_practice_sheet("beginner", "beginner_practice.txt")

# 生成中级练习表  
program.generate_practice_sheet("intermediate", "intermediate_practice.txt")

# 生成高级练习表
program.generate_practice_sheet("advanced", "advanced_practice.txt")
```

### 练习表格式 Practice Sheet Format

生成的文件包含：
- 字符信息（拼音、意思、笔画数）
- 例句
- 书写练习格（可打印）

```
1. 字 Character: 一
   拼音 Pinyin: yī
   意思 Meaning: one, 一
   笔画 Strokes: 1
   例子 Examples:
      • 一个人 (one person)
      • 一天 (one day)

   练习 Practice (write 5 times):
   一 _____ _____ _____ _____ _____

------------------------------------------------------------
```

---

## 示例 5: 自定义字符数据库 Custom Character Database

### 添加新字符 Add New Characters

```python
from chinese_character import CharacterDatabase, ChineseCharacter

# 创建数据库
db = CharacterDatabase()

# 添加新字符
new_char = ChineseCharacter(
    char="爱",
    pinyin="ài",
    meaning="love",
    strokes=10,
    level="intermediate",
    examples=["爱你 (love you)", "可爱 (cute)", "爱好 (hobby)"]
)

db.add_character(new_char)

# 保存到文件
db.save_to_file("my_characters.json")

# 从文件加载
db2 = CharacterDatabase("my_characters.json")
stats = db2.get_statistics()
print(f"加载了 {stats['total']} 个字符")
```

---

## 示例 6: 进度追踪 Progress Tracking

### 追踪学习进度 Track Learning Progress

```python
from chinese_character import CharacterDatabase, LiteracyProgram

db = CharacterDatabase()
program = LiteracyProgram(db)

# 学习一些字符
chars_to_learn = ['一', '二', '三', '人', '大']

for char in chars_to_learn:
    program.practice_character(char)
    print(f"已学习 Learned: {char}")

# 查看进度
print("\n学习进度 Learning Progress:")
program.show_progress()
```

**输出 Output:**
```
已学习 Learned: 一
已学习 Learned: 二
已学习 Learned: 三
已学习 Learned: 人
已学习 Learned: 大

学习进度 Learning Progress:
============================================================
学习进度 Learning Progress
============================================================

数据库总字数 Total characters in database: 24

初级 Beginner: 5/16 practiced
中级 Intermediate: 0/4 practiced
高级 Advanced: 0/4 practiced

总进度 Overall Progress: 5/24 (20.8%)
============================================================
```

---

## 示例 7: 批量查看字符 View Multiple Characters

### 显示所有级别的字符 Show All Levels

```python
from chinese_character import CharacterDatabase, LiteracyProgram

db = CharacterDatabase()
program = LiteracyProgram(db)

# 显示所有级别
for level in ['beginner', 'intermediate', 'advanced']:
    print(f"\n{'='*60}")
    print(f"级别 Level: {level.upper()}")
    print(f"{'='*60}\n")
    
    chars = db.get_by_level(level)
    for i, char in enumerate(chars, 1):
        print(f"{i}. {char.char} ({char.pinyin}) - {char.meaning}")
```

**输出 Output:**
```
============================================================
级别 Level: BEGINNER
============================================================

1. 一 (yī) - one, 一
2. 二 (èr) - two, 二
3. 三 (sān) - three, 三
4. 十 (shí) - ten, 十
5. 人 (rén) - person, human, 人
...
```

---

## 示例 8: 字符查找 Character Search

### 按字符查找 Search by Character

```python
from chinese_character import CharacterDatabase

db = CharacterDatabase()

# 查找字符
search_chars = ['人', '大', '学', '国']

for char_str in search_chars:
    char = db.get_by_char(char_str)
    if char:
        print(f"\n找到 Found: {char.char}")
        print(f"  拼音 Pinyin: {char.pinyin}")
        print(f"  意思 Meaning: {char.meaning}")
        print(f"  笔画 Strokes: {char.strokes}")
    else:
        print(f"\n未找到 Not found: {char_str}")
```

---

## 实用技巧 Practical Tips

### 1. 每日学习计划 Daily Learning Plan

```python
# 每天学习5个新字符
def daily_practice(day_number):
    db = CharacterDatabase()
    program = LiteracyProgram(db)
    
    all_chars = db.get_by_level('beginner')
    start_idx = (day_number - 1) * 5
    end_idx = start_idx + 5
    
    daily_chars = all_chars[start_idx:end_idx]
    
    print(f"\n第 {day_number} 天的学习内容 Day {day_number} Study Material")
    print("="*60)
    
    for char in daily_chars:
        print(char.display())
        program.practice_character(char.char)
    
    program.show_progress()

# 使用示例
daily_practice(1)  # 第一天
```

### 2. 复习功能 Review Function

```python
def review_practiced_characters(program):
    """复习已学过的字符"""
    print("\n复习时间 Review Time!")
    print("="*60)
    
    all_practiced = []
    for level, chars in program.progress.items():
        all_practiced.extend(chars)
    
    if not all_practiced:
        print("还没有学习任何字符 No characters learned yet")
        return
    
    print(f"您已经学习了 {len(all_practiced)} 个字符")
    print("You have learned", len(all_practiced), "characters\n")
    
    for char_str in all_practiced:
        char = program.database.get_by_char(char_str)
        if char:
            print(char.display())
```

### 3. 随机测试 Random Quiz

```python
import random

def quiz_character(db, level='beginner'):
    """随机测试一个字符"""
    chars = db.get_by_level(level)
    if not chars:
        print(f"No characters at {level} level")
        return
    
    char = random.choice(chars)
    
    print("\n测验 Quiz!")
    print("="*60)
    print(f"字符 Character: {char.char}")
    print("\n请回答 Please answer:")
    print(f"1. 拼音是什么？ What is the pinyin?")
    print(f"2. 意思是什么？ What is the meaning?")
    print(f"3. 有几画？ How many strokes?")
    
    input("\n按回车查看答案 Press Enter to see answer...")
    
    print(f"\n答案 Answer:")
    print(char.display())

# 使用示例
# quiz_character(db)
```

---

## 总结 Summary

这些示例展示了程序的主要功能：
These examples demonstrate the main features:

✅ 基本使用和交互式学习
✅ 作为 Python 模块使用
✅ 生成打印练习表
✅ 自定义字符数据库
✅ 进度追踪和复习
✅ 字符查找和测验

**开始您的学习之旅吧！Start your learning journey!**
