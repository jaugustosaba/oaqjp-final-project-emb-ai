import unittest
from emotion_detection import emotion_detector


class EmotionTestCase(unittest.TestCase):
    def test_ok(self):
        rs = emotion_detector('I am so happy I am doing this.')
        self.assertEqual('joy', rs['dominant_emotion'])


if __name__ == '__main__':
    unittest.main()