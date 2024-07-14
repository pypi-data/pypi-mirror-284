import unittest
from spam_classifier import SpamClassifier

class TestSpamClassifier(unittest.TestCase):
    def setUp(self):
        self.classifier = SpamClassifier()

    def test_predict_spam(self):
        message = "Подпишись на мой телеграм канал!"
        result = self.classifier.predict_message(message)
        self.assertEqual(result, 'spam')

    def test_predict_not_spam(self):
        message = "Привет, как дела?"
        result = self.classifier.predict_message(message)
        self.assertEqual(result, 'not_spam')

if __name__ == '__main__':
    unittest.main()
