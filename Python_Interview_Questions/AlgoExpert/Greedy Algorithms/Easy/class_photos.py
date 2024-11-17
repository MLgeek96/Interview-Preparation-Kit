from typing import List

def classPhotos(redShirtHeights: List[int], blueShirtHeights: List[int]):
    """
    It's photo day at the local school, and you're the photographer assigned to take class photos. The class that you'll be photographing has an even number of students, and all these students are wearing red or blue shirts. In fact, exactly half of the class is wearing red shirts, and the other half is wearing blue shirts. You're responsible for arranging the students in two rows before taking the photh. Each row should contain the same number of the students and should adhere to the following guidelines:
    1. All students wearing red shirts must be in the same row.
    2. All students wearing blue shirts must be in the same row.
    3. Each studnet in the back row must be strictly taller than the student directly in front of them in the front row.

    You're given two input arrays: one containing the heights of all the students with red shirts and another one containing the heights of all the students with blue shirts. These arrays will always have the same length, and each height will be a positive integer. Write a function that returns whether or not a class photo that follows the stated guidelines can be taken.

    Note: you can assume that each class has at least 2 students.

    Sample Input:
    ```
    redShirtHeights = [5, 8, 1, 3, 4]
    blueShirtHeights = [6, 9, 2, 4, 5]
    ```

    Sample Output:
    ```
    true // Place all students with blue shirts in the back row
    ```

    Hints:
    1. Start by determining which row will have the students wearing blue shirts and which row will have the students wearing red shirts. Once you know this, how can you determine if it's possible to take the photo?
    2. The shirt color of the tallest student will determine which students need to be placed in the back row. The tallest student can't be placed in the front row because there's no student taller than them who can be placed behind them.
    3. Once you know which students should be placed in each row, you can simply check if each student in the back row can be paired with a student in the front row who is shorter than them. If you can't find a satisfactory pairing for every student in the back row, then you can't take the photo.
    4. Sort each input array in descending order, then determine which students will be in the front and back rows following Hint #2. After this, simply loop through your sorted input arrays, and check if the current tallest student in the back row is taller than the current tallest student in the front row. If you find that the current tallest student (one that has yet to be placed) in the back row isn't taller than the current tallest student in the front row, then the photo can't be taken.

    Optimal Space & Time Complexity
    O(nlog(n)) time | O(1) space - where n is the number of students
    """
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    shirtColorInFirstRow = "RED" if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"
    for idx in range(len(redShirtHeights)):
        redShirtHeight = redShirtHeights[idx]
        blueShirtHeight = blueShirtHeights[idx]

        if shirtColorInFirstRow == "RED":
            if redShirtHeight >= blueShirtHeight:
                return False 
        else:
            if blueShirtHeight >= redShirtHeight:
                return False 

    return True

if __name__ == "__main__":
    redShirtHeights = [5, 8, 1, 3, 4]
    blueShirtHeights = [6, 9, 2, 4, 5]
    assert classPhotos(redShirtHeights, blueShirtHeights) is True

    redShirtHeights = [6, 9, 2, 4, 5]
    blueShirtHeights = [5, 8, 1, 3, 4]
    assert classPhotos(redShirtHeights, blueShirtHeights) is True

    redShirtHeights = [6, 9, 2, 4, 5, 1]
    blueShirtHeights = [5, 8, 1, 3, 4, 9]
    assert classPhotos(redShirtHeights, blueShirtHeights) is False

    redShirtHeights = [6]
    blueShirtHeights = [6]
    assert classPhotos(redShirtHeights, blueShirtHeights) is False

    redShirtHeights = [126]
    blueShirtHeights = [125]
    assert classPhotos(redShirtHeights, blueShirtHeights) is True

    redShirtHeights = [1, 2, 3, 4, 5]
    blueShirtHeights = [2, 3, 4, 5, 6]
    assert classPhotos(redShirtHeights, blueShirtHeights) is True

    redShirtHeights = [1, 1, 1, 1, 1, 1, 1, 1]
    blueShirtHeights = [5, 6, 7, 2, 3, 1, 2, 3]
    assert classPhotos(redShirtHeights, blueShirtHeights) is False

    redShirtHeights = [1, 1, 1, 1, 1, 1, 1, 1]
    blueShirtHeights = [2, 2, 2, 2, 2, 2, 2, 2]
    assert classPhotos(redShirtHeights, blueShirtHeights) is True

    redShirtHeights = [125]
    blueShirtHeights = [126]
    assert classPhotos(redShirtHeights, blueShirtHeights) is True

    redShirtHeights = [19, 2, 4, 6, 2, 3, 1, 1, 4]
    blueShirtHeights = [21, 5, 4, 4, 4, 4, 4, 4, 4]
    assert classPhotos(redShirtHeights, blueShirtHeights) is False

    redShirtHeights = [19, 19, 21, 1, 1, 1, 1, 1]
    blueShirtHeights = [20, 5, 4, 4, 4, 4, 4, 4]
    assert classPhotos(redShirtHeights, blueShirtHeights) is False

    redShirtHeights = [3, 5, 6, 8, 2]
    blueShirtHeights = [2, 4, 7, 5, 1]
    assert classPhotos(redShirtHeights, blueShirtHeights) is True

    redShirtHeights = [3, 5, 6, 8, 2, 1]
    blueShirtHeights = [2, 4, 7, 5, 1, 6]
    assert classPhotos(redShirtHeights, blueShirtHeights) is False

    redShirtHeights = [4, 5]
    blueShirtHeights = [5, 4]
    assert classPhotos(redShirtHeights, blueShirtHeights) is False

    redShirtHeights = [5, 6]
    blueShirtHeights = [5, 4]
    assert classPhotos(redShirtHeights, blueShirtHeights) is True