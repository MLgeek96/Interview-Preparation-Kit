from typing import List

def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    """
    Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

    You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

    Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

    For the last line of text, it should be left-justified, and no extra space is inserted between words.

    Note:

    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.

    Example 1:
    Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
    Output:
    [
    "This    is    an",
    "example  of text",
    "justification.  "
    ]

    Example 2:
    Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
    Output:
    [
    "What   must   be",
    "acknowledgment  ",
    "shall be        "
    ]
    Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
    Note that the second line is also left-justified because it contains only one word.

    Example 3:
    Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
    Output:
    [
    "Science  is  what we",
    "understand      well",
    "enough to explain to",
    "a  computer.  Art is",
    "everything  else  we",
    "do                  "
    ]

    Constraints:
    • 1 <= words.length <= 300
    • 1 <= words[i].length <= 20
    • words[i] consists of only English letters and symbols.
    • 1 <= maxWidth <= 100
    • words[i].length <= maxWidth
    """
    assert 1 <= len(words) <= 300
    for word in words:
        assert 1 <= len(word) <= 20
        assert len(word) <= maxWidth
    assert 1 <= maxWidth <= 100

    def insert_spaces(line, words_amount, space_difference):
        if words_amount == 1:
            line[0] = line[0].ljust(space_difference+len(line[0]))
            return

        spaces = space_difference // (words_amount - 1)
        spaces_remainder = space_difference % (words_amount - 1)

        for index in range(words_amount - 1):
            if index < spaces_remainder:
                line[index] += ' ' * (spaces + 1)
            else:
                line[index] += ' ' * spaces

    length, cur_line, result = 0, [], []
    for word in words:
        words_amount = len(cur_line)
        if length + len(word) + words_amount > maxWidth:
            space_difference = maxWidth - length
            insert_spaces(cur_line, words_amount, space_difference)
            result.append(''.join(cur_line))
            
            length = 0
            cur_line = []
        
        cur_line.append(word)
        length += len(word)

    last_line = ' '.join(cur_line).ljust(maxWidth)
    result.append(last_line)
    return result

    # rowList = list()
    # n = 0
    # while n < len(words):
    #     charCount = 0
    #     word = ""
    #     while charCount <= maxWidth:
    #         if n >= len(words) or charCount + len(words[n]) > maxWidth:
    #             break
    #         charCount += len(words[n]) + 1
    #         word += words[n] + " "
    #         n += 1
    #     rowList.append(word.rstrip())

    # def sortText(words, maxWidth):
    #     for rowIdx in range(len(words)):
    #         if rowIdx == len(words) - 1:
    #             words[rowIdx] = words[rowIdx].ljust(maxWidth)
    #         else:
    #             wordList = words[rowIdx].split(" ")
    #             charLength = sum(len(word) for word in wordList)
    #             if len(wordList) != 1:
    #                 minSpacesBetweenWords = (maxWidth - charLength) // (len(wordList) - 1)
    #                 spacesRemainder = (maxWidth - charLength) % (len(wordList) - 1)
    #                 resultStr = ""
    #                 for i in range(len(wordList) - 1):
    #                     resultStr += wordList[i]
    #                     if i < spacesRemainder:
    #                         resultStr += " " * (minSpacesBetweenWords + 1)
    #                     else:
    #                         resultStr += " " * minSpacesBetweenWords
    #                 words[rowIdx] = resultStr + wordList[-1]
    #             else:
    #                 words[rowIdx] = words[rowIdx].ljust(maxWidth)                 

    #     return words

    # return sortText(rowList, maxWidth)
