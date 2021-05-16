import os
# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)
#
#
# if __name__ == '__main__':
#     unittest.main()

high_score_disk = open("high_score.txt", "r+")
file_size = os.path.getsize("high_score.txt")
if file_size == 0:
    high_score_disk.write(str("0"))
str_high_score = high_score_disk.read()
high_score = str(str_high_score)

print(high_score_disk)
print(file_size)
print(str_high_score)
print(high_score)
