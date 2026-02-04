#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chinese Character Literacy App - Interactive CLI
中文识字应用 - 交互式命令行界面

Simple, user-friendly interface for elderly users to learn Chinese characters.
"""

import sys
from chinese_character import CharacterDatabase, LiteracyProgram


def clear_screen():
    """Clear the terminal screen."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def print_menu():
    """Display main menu with large, clear text."""
    print("\n" + "="*60)
    print("          主菜单 MAIN MENU")
    print("="*60)
    print("\n请选择 Please select:")
    print("\n  1. 学习初级字符    Learn Beginner Characters")
    print("  2. 学习中级字符    Learn Intermediate Characters")
    print("  3. 学习高级字符    Learn Advanced Characters")
    print("  4. 查看学习进度    View Progress")
    print("  5. 生成练习表      Generate Practice Sheet")
    print("  6. 查找字符        Search Character")
    print("  7. 帮助           Help")
    print("  0. 退出           Exit")
    print("\n" + "="*60)


def show_help():
    """Display help information."""
    help_text = """
╔══════════════════════════════════════════════════════════════╗
║                      帮助信息 HELP                           ║
╚══════════════════════════════════════════════════════════════╝

使用说明 Instructions:

1️⃣  学习字符 Learning Characters:
   • 选择相应级别开始学习
   • 程序会显示字符、拼音、意思和例句
   • 仔细观察每个字的笔画
   
2️⃣  练习方法 Practice Methods:
   • 跟读拼音，学习发音
   • 观察字形，记住结构
   • 看例句，理解用法
   • 多写多练，加深记忆

3️⃣  学习级别 Learning Levels:
   • 初级：最常用的基础字，如数字、家人称呼
   • 中级：日常生活常用字
   • 高级：更复杂但重要的字

4️⃣  进度追踪 Progress Tracking:
   • 系统会记录您学过的字符
   • 可随时查看学习进度
   
小贴士 Tips:
✓ 每天学习一点，不要着急
✓ 重复是学习的关键
✓ 多看多写多练习
✓ 遇到困难不要放弃

祝您学习愉快！Happy Learning!
"""
    print(help_text)
    input("\n按回车键继续... Press Enter to continue...")


def interactive_character_learning(program, level):
    """
    Interactive character learning session.
    
    Args:
        program: LiteracyProgram instance
        level: Learning level (beginner/intermediate/advanced)
    """
    characters = program.database.get_by_level(level)
    
    if not characters:
        print(f"\n该级别暂无字符 No characters available at {level} level.")
        input("\n按回车键继续... Press Enter to continue...")
        return
    
    print(f"\n{'='*60}")
    print(f"级别 Level: {level.upper()}")
    print(f"字数 Total: {len(characters)} characters")
    print(f"{'='*60}")
    print("\n说明 Instructions:")
    print("  • 输入数字查看对应字符 Enter number to view character")
    print("  • 输入 'n' 下一个 Enter 'n' for next")
    print("  • 输入 'b' 返回菜单 Enter 'b' to go back")
    print()
    
    current_index = 0
    
    while True:
        if current_index < len(characters):
            char = characters[current_index]
            print(f"\n字符 {current_index + 1}/{len(characters)}")
            print(char.display(large_font=True))
            
            # Mark as practiced
            if char.char not in program.progress[level]:
                program.progress[level].append(char.char)
        
        print("\n选项 Options: [n]下一个 Next  [p]上一个 Previous  [b]返回 Back")
        choice = input("\n您的选择 Your choice: ").strip().lower()
        
        if choice == 'n':
            if current_index < len(characters) - 1:
                current_index += 1
            else:
                print("\n已经是最后一个字符了！This is the last character!")
                input("按回车键继续... Press Enter to continue...")
        elif choice == 'p':
            if current_index > 0:
                current_index -= 1
            else:
                print("\n已经是第一个字符了！This is the first character!")
                input("按回车键继续... Press Enter to continue...")
        elif choice == 'b':
            break
        elif choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(characters):
                current_index = idx
            else:
                print("\n无效的数字！Invalid number!")
                input("按回车键继续... Press Enter to continue...")
        else:
            print("\n无效的选择！Invalid choice!")
            input("按回车键继续... Press Enter to continue...")


def search_character(program):
    """Search and display a specific character."""
    print("\n" + "="*60)
    print("          查找字符 SEARCH CHARACTER")
    print("="*60)
    
    char = input("\n请输入要查找的汉字 Enter character to search: ").strip()
    
    if not char:
        print("\n未输入字符！No character entered!")
        input("按回车键继续... Press Enter to continue...")
        return
    
    character = program.database.get_by_char(char)
    
    if character:
        print("\n找到了！Found!")
        print(character.display(large_font=True))
    else:
        print(f"\n未找到字符 '{char}'。")
        print(f"Character '{char}' not found in database.")
        print("\n该字符可能:")
        print("• 还没有添加到数据库")
        print("• 不属于常用字")
    
    input("\n按回车键继续... Press Enter to continue...")


def generate_practice_menu(program):
    """Menu for generating practice sheets."""
    print("\n" + "="*60)
    print("          生成练习表 GENERATE PRACTICE SHEET")
    print("="*60)
    
    print("\n选择级别 Select level:")
    print("  1. 初级 Beginner")
    print("  2. 中级 Intermediate")
    print("  3. 高级 Advanced")
    print("  0. 返回 Back")
    
    choice = input("\n您的选择 Your choice: ").strip()
    
    level_map = {
        '1': 'beginner',
        '2': 'intermediate',
        '3': 'advanced'
    }
    
    if choice in level_map:
        level = level_map[choice]
        filename = f"{level}_practice.txt"
        program.generate_practice_sheet(level, filename)
        print(f"\n✓ 练习表已生成！Practice sheet generated!")
        print(f"  文件名 Filename: {filename}")
    elif choice != '0':
        print("\n无效的选择！Invalid choice!")
    
    input("\n按回车键继续... Press Enter to continue...")


def main():
    """Main application loop."""
    # Initialize
    db = CharacterDatabase()
    program = LiteracyProgram(db)
    
    # Welcome screen
    clear_screen()
    program.show_welcome()
    input("\n按回车键开始... Press Enter to start...")
    
    # Main loop
    while True:
        clear_screen()
        print_menu()
        
        choice = input("\n请输入选项 Enter your choice: ").strip()
        
        if choice == '1':
            clear_screen()
            interactive_character_learning(program, 'beginner')
        elif choice == '2':
            clear_screen()
            interactive_character_learning(program, 'intermediate')
        elif choice == '3':
            clear_screen()
            interactive_character_learning(program, 'advanced')
        elif choice == '4':
            clear_screen()
            program.show_progress()
            input("\n按回车键继续... Press Enter to continue...")
        elif choice == '5':
            clear_screen()
            generate_practice_menu(program)
        elif choice == '6':
            clear_screen()
            search_character(program)
        elif choice == '7':
            clear_screen()
            show_help()
        elif choice == '0':
            clear_screen()
            print("\n" + "="*60)
            print("\n  感谢使用中文识字程序！")
            print("  Thank you for using Chinese Character Literacy Program!")
            print("\n  祝您学习进步！")
            print("  Wish you success in learning!")
            print("\n" + "="*60 + "\n")
            sys.exit(0)
        else:
            print("\n⚠ 无效的选择，请重试！")
            print("  Invalid choice, please try again!")
            input("\n按回车键继续... Press Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n程序已退出 Program exited.\n")
        sys.exit(0)
