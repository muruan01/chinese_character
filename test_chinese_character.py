#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for Chinese Character Literacy Program
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from chinese_character import ChineseCharacter, CharacterDatabase, LiteracyProgram


def test_character_creation():
    """Test creating a Chinese character."""
    char = ChineseCharacter("人", "rén", "person", 2, "beginner", ["人们 (people)"])
    assert char.char == "人"
    assert char.pinyin == "rén"
    assert char.meaning == "person"
    assert char.strokes == 2
    assert char.level == "beginner"
    assert len(char.examples) == 1
    print("✓ Character creation test passed")


def test_character_display():
    """Test character display."""
    char = ChineseCharacter("一", "yī", "one", 1, "beginner", ["一天 (one day)"])
    display = char.display(large_font=True)
    assert "一" in display
    assert "yī" in display
    assert "one" in display
    assert "一天 (one day)" in display
    print("✓ Character display test passed")


def test_character_to_dict():
    """Test converting character to dictionary."""
    char = ChineseCharacter("二", "èr", "two", 2, "beginner")
    char_dict = char.to_dict()
    assert char_dict['char'] == "二"
    assert char_dict['pinyin'] == "èr"
    assert char_dict['strokes'] == 2
    print("✓ Character to dict test passed")


def test_character_from_dict():
    """Test creating character from dictionary."""
    data = {
        'char': '三',
        'pinyin': 'sān',
        'meaning': 'three',
        'strokes': 3,
        'level': 'beginner',
        'examples': ['三天 (three days)']
    }
    char = ChineseCharacter.from_dict(data)
    assert char.char == '三'
    assert char.pinyin == 'sān'
    assert char.meaning == 'three'
    print("✓ Character from dict test passed")


def test_database_creation():
    """Test creating character database."""
    db = CharacterDatabase()
    assert len(db.characters) > 0
    stats = db.get_statistics()
    assert stats['total'] > 0
    assert stats['beginner'] > 0
    print(f"✓ Database creation test passed (total: {stats['total']} characters)")


def test_database_get_by_level():
    """Test getting characters by level."""
    db = CharacterDatabase()
    beginner_chars = db.get_by_level('beginner')
    assert len(beginner_chars) > 0
    for char in beginner_chars:
        assert char.level == 'beginner'
    print(f"✓ Get by level test passed ({len(beginner_chars)} beginner chars)")


def test_database_get_by_char():
    """Test getting character by its Chinese character."""
    db = CharacterDatabase()
    char = db.get_by_char('人')
    assert char is not None
    assert char.char == '人'
    assert char.pinyin == 'rén'
    print("✓ Get by char test passed")


def test_literacy_program():
    """Test literacy program."""
    db = CharacterDatabase()
    program = LiteracyProgram(db)
    assert program.database == db
    assert program.current_level == "beginner"
    print("✓ Literacy program test passed")


def test_progress_tracking():
    """Test progress tracking."""
    db = CharacterDatabase()
    program = LiteracyProgram(db)
    
    # Initially no progress
    stats = db.get_statistics()
    assert len(program.progress['beginner']) == 0
    
    # Practice a character
    program.practice_character('人')
    assert '人' in program.progress['beginner']
    
    print("✓ Progress tracking test passed")


def test_practice_sheet_generation():
    """Test practice sheet generation."""
    db = CharacterDatabase()
    program = LiteracyProgram(db)
    
    # Generate practice sheet
    output_file = "/tmp/test_practice.txt"
    program.generate_practice_sheet('beginner', output_file)
    
    # Check file was created
    assert os.path.exists(output_file)
    
    # Check content
    with open(output_file, 'r', encoding='utf-8') as f:
        content = f.read()
        assert 'beginner' in content.lower()
        assert '练习 Practice' in content
    
    # Clean up
    os.remove(output_file)
    print("✓ Practice sheet generation test passed")


def test_character_search():
    """Test character search functionality."""
    db = CharacterDatabase()
    
    # Search for existing character
    char = db.get_by_char('一')
    assert char is not None
    assert char.char == '一'
    
    # Search for non-existing character
    char = db.get_by_char('龘')
    assert char is None
    
    print("✓ Character search test passed")


def run_all_tests():
    """Run all tests."""
    print("\n" + "="*60)
    print("Running Chinese Character Literacy Program Tests")
    print("="*60 + "\n")
    
    tests = [
        test_character_creation,
        test_character_display,
        test_character_to_dict,
        test_character_from_dict,
        test_database_creation,
        test_database_get_by_level,
        test_database_get_by_char,
        test_literacy_program,
        test_progress_tracking,
        test_practice_sheet_generation,
        test_character_search,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} error: {e}")
            failed += 1
    
    print("\n" + "="*60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("="*60 + "\n")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
