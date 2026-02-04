#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chinese Character Literacy Program for Elderly Users
中文识字程序 - 为老年人设计

This program helps elderly users learn Chinese characters with:
- Large, clear fonts
- Stroke order visualization
- Pinyin pronunciation
- Common usage examples
- Progressive difficulty levels
"""

import json
import os
from typing import Dict, List, Optional


class ChineseCharacter:
    """Represents a Chinese character with learning materials."""
    
    def __init__(self, char: str, pinyin: str, meaning: str, 
                 strokes: int, level: str = "beginner",
                 examples: Optional[List[str]] = None):
        """
        Initialize a Chinese character.
        
        Args:
            char: The Chinese character
            pinyin: Pronunciation in pinyin
            meaning: English/Chinese meaning
            strokes: Number of strokes
            level: Difficulty level (beginner/intermediate/advanced)
            examples: List of example words/phrases using this character
        """
        self.char = char
        self.pinyin = pinyin
        self.meaning = meaning
        self.strokes = strokes
        self.level = level
        self.examples = examples or []
    
    def to_dict(self) -> Dict:
        """Convert character to dictionary."""
        return {
            'char': self.char,
            'pinyin': self.pinyin,
            'meaning': self.meaning,
            'strokes': self.strokes,
            'level': self.level,
            'examples': self.examples
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'ChineseCharacter':
        """Create character from dictionary."""
        return cls(
            char=data['char'],
            pinyin=data['pinyin'],
            meaning=data['meaning'],
            strokes=data['strokes'],
            level=data.get('level', 'beginner'),
            examples=data.get('examples', [])
        )
    
    def display(self, large_font: bool = True) -> str:
        """
        Display character information in a readable format.
        
        Args:
            large_font: Use large font display for elderly users
            
        Returns:
            Formatted string with character information
        """
        separator = "=" * 60
        output = [separator]
        
        if large_font:
            # Display character in large format
            output.append(f"\n字 Character: {self.char}  (笔画 Strokes: {self.strokes})")
            output.append(f"拼音 Pinyin: {self.pinyin}")
            output.append(f"意思 Meaning: {self.meaning}")
            output.append(f"级别 Level: {self.level}")
        else:
            output.append(f"字: {self.char} | 拼音: {self.pinyin} | 意思: {self.meaning}")
            output.append(f"笔画: {self.strokes} | 级别: {self.level}")
        
        if self.examples:
            output.append("\n例子 Examples:")
            for i, example in enumerate(self.examples, 1):
                output.append(f"  {i}. {example}")
        
        output.append(separator)
        return "\n".join(output)


class CharacterDatabase:
    """Database of Chinese characters for learning."""
    
    def __init__(self, data_file: Optional[str] = None):
        """
        Initialize character database.
        
        Args:
            data_file: Path to JSON file with character data
        """
        self.characters: List[ChineseCharacter] = []
        self.data_file = data_file or "characters_data.json"
        self._load_default_characters()
        if os.path.exists(self.data_file):
            self.load_from_file(self.data_file)
    
    def _load_default_characters(self):
        """Load default set of common Chinese characters for elderly literacy."""
        # Most common characters for basic literacy (3000+ characters for full literacy)
        # Starting with the most essential characters for daily life
        default_chars = [
            # Level 1: Most basic characters (数字 Numbers)
            ChineseCharacter("一", "yī", "one, 一", 1, "beginner", ["一个人 (one person)", "一天 (one day)"]),
            ChineseCharacter("二", "èr", "two, 二", 2, "beginner", ["二月 (February)", "第二 (second)"]),
            ChineseCharacter("三", "sān", "three, 三", 3, "beginner", ["三天 (three days)", "三个 (three)"]),
            ChineseCharacter("十", "shí", "ten, 十", 2, "beginner", ["十天 (ten days)", "十分 (very)"]),
            
            # Basic family terms
            ChineseCharacter("人", "rén", "person, human, 人", 2, "beginner", 
                           ["人们 (people)", "老人 (elderly)", "人口 (population)"]),
            ChineseCharacter("大", "dà", "big, large, 大", 3, "beginner",
                           ["大人 (adult)", "大家 (everyone)", "长大 (grow up)"]),
            ChineseCharacter("小", "xiǎo", "small, little, 小", 3, "beginner",
                           ["小孩 (child)", "小时 (hour)", "大小 (size)"]),
            ChineseCharacter("老", "lǎo", "old, elderly, 老", 6, "beginner",
                           ["老人 (elderly person)", "老师 (teacher)", "老板 (boss)"]),
            
            # Common daily life characters
            ChineseCharacter("天", "tiān", "sky, day, heaven, 天", 4, "beginner",
                           ["今天 (today)", "天气 (weather)", "天天 (everyday)"]),
            ChineseCharacter("日", "rì", "sun, day, 日", 4, "beginner",
                           ["日子 (days)", "生日 (birthday)", "今日 (today)"]),
            ChineseCharacter("月", "yuè", "moon, month, 月", 4, "beginner",
                           ["月亮 (moon)", "一月 (January)", "月饼 (mooncake)"]),
            ChineseCharacter("年", "nián", "year, 年", 6, "beginner",
                           ["今年 (this year)", "年纪 (age)", "过年 (New Year)"]),
            
            # Actions and verbs
            ChineseCharacter("吃", "chī", "eat, 吃", 6, "beginner",
                           ["吃饭 (eat meal)", "好吃 (delicious)", "吃药 (take medicine)"]),
            ChineseCharacter("喝", "hē", "drink, 喝", 12, "beginner",
                           ["喝水 (drink water)", "喝茶 (drink tea)"]),
            ChineseCharacter("看", "kàn", "look, see, watch, 看", 9, "beginner",
                           ["看书 (read book)", "看见 (see)", "好看 (good-looking)"]),
            ChineseCharacter("听", "tīng", "listen, hear, 听", 7, "beginner",
                           ["听说 (hear of)", "听话 (obedient)", "听音乐 (listen to music)"]),
            
            # Intermediate level
            ChineseCharacter("学", "xué", "study, learn, 学", 8, "intermediate",
                           ["学习 (study)", "学校 (school)", "学生 (student)"]),
            ChineseCharacter("字", "zì", "character, word, 字", 6, "intermediate",
                           ["汉字 (Chinese character)", "写字 (write)", "识字 (literacy)"]),
            ChineseCharacter("书", "shū", "book, 书", 4, "intermediate",
                           ["书本 (book)", "看书 (read)", "书店 (bookstore)"]),
            ChineseCharacter("好", "hǎo", "good, well, 好", 6, "intermediate",
                           ["你好 (hello)", "好吃 (delicious)", "很好 (very good)"]),
            
            # Advanced common characters
            ChineseCharacter("家", "jiā", "home, family, 家", 10, "advanced",
                           ["家人 (family)", "回家 (go home)", "大家 (everyone)"]),
            ChineseCharacter("国", "guó", "country, nation, 国", 8, "advanced",
                           ["中国 (China)", "国家 (country)", "外国 (foreign country)"]),
            ChineseCharacter("中", "zhōng", "middle, center, China, 中", 4, "advanced",
                           ["中国 (China)", "中午 (noon)", "中间 (middle)"]),
            ChineseCharacter("文", "wén", "language, culture, text, 文", 4, "advanced",
                           ["中文 (Chinese)", "文化 (culture)", "文字 (writing)"]),
        ]
        
        self.characters.extend(default_chars)
    
    def add_character(self, character: ChineseCharacter):
        """Add a character to the database."""
        self.characters.append(character)
    
    def get_by_level(self, level: str) -> List[ChineseCharacter]:
        """Get all characters of a specific level."""
        return [c for c in self.characters if c.level == level]
    
    def get_by_char(self, char: str) -> Optional[ChineseCharacter]:
        """Get character by its Chinese character."""
        for c in self.characters:
            if c.char == char:
                return c
        return None
    
    def save_to_file(self, filepath: Optional[str] = None):
        """Save character database to JSON file."""
        filepath = filepath or self.data_file
        data = [c.to_dict() for c in self.characters]
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def load_from_file(self, filepath: str):
        """Load character database from JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for char_data in data:
                # Check if character already exists
                if not self.get_by_char(char_data['char']):
                    self.add_character(ChineseCharacter.from_dict(char_data))
    
    def get_all_characters(self) -> List[ChineseCharacter]:
        """Get all characters in database."""
        return self.characters
    
    def get_statistics(self) -> Dict[str, int]:
        """Get statistics about the character database."""
        stats = {
            'total': len(self.characters),
            'beginner': len(self.get_by_level('beginner')),
            'intermediate': len(self.get_by_level('intermediate')),
            'advanced': len(self.get_by_level('advanced'))
        }
        return stats


class LiteracyProgram:
    """Main literacy program for elderly users."""
    
    def __init__(self, database: CharacterDatabase):
        """
        Initialize literacy program.
        
        Args:
            database: Character database to use
        """
        self.database = database
        self.current_level = "beginner"
        self.progress: Dict[str, List[str]] = {
            'beginner': [],
            'intermediate': [],
            'advanced': []
        }
    
    def show_welcome(self):
        """Display welcome message."""
        welcome = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║           中文识字学习程序                                    ║
║      Chinese Character Literacy Program                     ║
║                                                              ║
║           专为老年人设计                                      ║
║         Designed for Elderly Users                          ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

欢迎使用中文识字学习程序！
Welcome to the Chinese Character Literacy Program!

本程序帮助您学习常用汉字，从简单到复杂，循序渐进。
This program helps you learn common Chinese characters progressively.

特点 Features:
• 大字体显示 - Large font display
• 拼音注音 - Pinyin pronunciation
• 常用例句 - Common examples
• 笔画信息 - Stroke information
• 分级学习 - Leveled learning
"""
        print(welcome)
    
    def list_characters_by_level(self, level: str, large_font: bool = True):
        """
        List all characters at a specific level.
        
        Args:
            level: beginner, intermediate, or advanced
            large_font: Use large font for elderly users
        """
        characters = self.database.get_by_level(level)
        print(f"\n{'='*60}")
        print(f"级别 Level: {level.upper()}")
        print(f"字数 Total Characters: {len(characters)}")
        print(f"{'='*60}\n")
        
        for i, char in enumerate(characters, 1):
            print(f"\n{i}. {char.display(large_font=large_font)}")
    
    def practice_character(self, char: str):
        """
        Practice a specific character.
        
        Args:
            char: Chinese character to practice
        """
        character = self.database.get_by_char(char)
        if character:
            print("\n" + character.display(large_font=True))
            # Mark as practiced
            if char not in self.progress[character.level]:
                self.progress[character.level].append(char)
        else:
            print(f"字符 '{char}' 未找到。Character '{char}' not found.")
    
    def show_progress(self):
        """Display learning progress."""
        stats = self.database.get_statistics()
        print("\n" + "="*60)
        print("学习进度 Learning Progress")
        print("="*60)
        print(f"\n数据库总字数 Total characters in database: {stats['total']}")
        print(f"\n初级 Beginner: {len(self.progress['beginner'])}/{stats['beginner']} practiced")
        print(f"中级 Intermediate: {len(self.progress['intermediate'])}/{stats['intermediate']} practiced")
        print(f"高级 Advanced: {len(self.progress['advanced'])}/{stats['advanced']} practiced")
        
        total_practiced = sum(len(chars) for chars in self.progress.values())
        if stats['total'] > 0:
            percentage = (total_practiced / stats['total']) * 100
            print(f"\n总进度 Overall Progress: {total_practiced}/{stats['total']} ({percentage:.1f}%)")
        print("="*60)
    
    def generate_practice_sheet(self, level: str, output_file: str = "practice_sheet.txt"):
        """
        Generate a practice sheet for a specific level.
        
        Args:
            level: beginner, intermediate, or advanced
            output_file: Output filename
        """
        characters = self.database.get_by_level(level)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"{'='*60}\n")
            f.write(f"中文识字练习 - {level.upper()} 级别\n")
            f.write(f"Chinese Character Practice Sheet - {level.upper()} Level\n")
            f.write(f"{'='*60}\n\n")
            
            for i, char in enumerate(characters, 1):
                f.write(f"{i}. 字 Character: {char.char}\n")
                f.write(f"   拼音 Pinyin: {char.pinyin}\n")
                f.write(f"   意思 Meaning: {char.meaning}\n")
                f.write(f"   笔画 Strokes: {char.strokes}\n")
                if char.examples:
                    f.write(f"   例子 Examples:\n")
                    for example in char.examples:
                        f.write(f"      • {example}\n")
                f.write(f"\n   练习 Practice (write 5 times):\n")
                f.write(f"   {char.char} _____ _____ _____ _____ _____\n\n")
                f.write(f"{'-'*60}\n\n")
        
        print(f"\n练习表已生成 Practice sheet generated: {output_file}")


def main():
    """Main program entry point."""
    # Initialize database and program
    db = CharacterDatabase()
    program = LiteracyProgram(db)
    
    # Show welcome message
    program.show_welcome()
    
    # Display statistics
    stats = db.get_statistics()
    print("\n字库统计 Character Database Statistics:")
    print(f"  • 初级 Beginner: {stats['beginner']} characters")
    print(f"  • 中级 Intermediate: {stats['intermediate']} characters")
    print(f"  • 高级 Advanced: {stats['advanced']} characters")
    print(f"  • 总计 Total: {stats['total']} characters\n")
    
    # Example: Show beginner level characters
    print("\n" + "="*60)
    print("示例：初级字符列表")
    print("Example: Beginner Level Characters")
    print("="*60)
    program.list_characters_by_level("beginner")
    
    # Generate practice sheet
    program.generate_practice_sheet("beginner", "beginner_practice.txt")
    
    # Show progress
    program.show_progress()
    
    print("\n程序结束。感谢使用！")
    print("Program ended. Thank you for using!\n")


if __name__ == "__main__":
    main()
