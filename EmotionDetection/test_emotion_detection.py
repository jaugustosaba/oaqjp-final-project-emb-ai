import unittest
from emotion_detection import emotion_detector


class EmotionTestCase(unittest.TestCase):
    def test_joy(self):
        rs = emotion_detector('I am glad this happened')
        self.assertEqual('joy', rs['dominant_emotion'])

    def test_anger(self):
        rs = emotion_detector('I am really mad about this')
        self.assertEqual('anger', rs['dominant_emotion'])

    def test_disgust(self):
        rs = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual('disgust', rs['dominant_emotion'])

    def test_sadness(self):
        rs = emotion_detector('I am so sad about this')
        self.assertEqual('sadness', rs['dominant_emotion'])

    def test_fear(self):
        rs = emotion_detector('I am really afraid that this will happen')
        self.assertEqual('fear', rs['dominant_emotion'])


if __name__ == '__main__':
    unittest.main()