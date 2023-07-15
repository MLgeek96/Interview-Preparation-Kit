import pytest
from leetcode.problem_sets.Q68_text_justification import fullJustify

print(fullJustify.__doc__)

def test_fullJustify():
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    assert fullJustify(words, maxWidth) == [
                                            "This    is    an",
                                            "example  of text",
                                            "justification.  "
                                            ]

    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    assert fullJustify(words, maxWidth) == [
                                            "What   must   be",
                                            "acknowledgment  ",
                                            "shall be        "
                                            ]

    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    assert fullJustify(words, maxWidth) == [
                                            "Science  is  what we",
                                            "understand      well",
                                            "enough to explain to",
                                            "a  computer.  Art is",
                                            "everything  else  we",
                                            "do                  "
                                            ]

    words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
    maxWidth = 16
    assert fullJustify(words, maxWidth) == [
                                            "ask   not   what",
                                            "your country can",
                                            "do  for  you ask",
                                            "what  you can do",
                                            "for your country"
                                            ]

    words = ["Listen","to","many,","speak","to","a","few."]
    maxWidth = 6
    assert fullJustify(words, maxWidth) == [
                                            "Listen",
                                            "to    ",
                                            "many, ",
                                            "speak ",
                                            "to   a",
                                            "few.  "
                                            ]
