


class Question:
    counter = 0
    questions_list = []

    def __init__(self, question_sentence = "", answer = "", point_worth = 0, type_of_question = ""):
        self.question_sentence = question_sentence
        self.answer = answer
        self.point_worth = point_worth
        self.type_of_question = type_of_question
        self.question_id = Question.counter
        Question.counter += 1
        Question.questions_list.append(self)


question0 = Question("How is this character pronounced?   あ", "a", 1, "pronounciation")
question1 = Question("How is this character pronounced?   は", "ha", 1, "pronounciation")
question2 = Question("How is this character pronounced?   て", "te", 1, "pronounciation")
question3 = Question("How is this character pronounced?   ろ", "ro", 1, "pronounciation")
question4 = Question("How is this character pronounced?   ほ", "ho", 1, "pronounciation")
question5 = Question("How is this character pronounced?   い", "i", 1, "pronounciation")
question6 = Question("How is this character pronounced?   り", "ri", 1, "pronounciation")
question7 = Question("How is this character pronounced?   ふ", "fu", 1, "pronounciation")
question8 = Question("How is this character pronounced?   め", "me", 1, "pronounciation")
question9 = Question("How is this character pronounced?   く", "ku", 1, "pronounciation")

question10 = Question("Which character's pronounciation is this?   ha", "は", 1, "hiragana")
question11 = Question("Which character's pronounciation is this?   ke", "け", 1, "hiragana")
question12 = Question("Which character's pronounciation is this?   he", "へ", 1, "hiragana")
question13 = Question("Which character's pronounciation is this?   ka", "か", 1, "hiragana")
question14 = Question("Which character's pronounciation is this?   ko", "こ", 1, "hiragana")
question15 = Question("Which character's pronounciation is this?   wo", "を", 1, "hiragana")
question16 = Question("Which character's pronounciation is this?   wa", "わ", 1, "hiragana")
question17 = Question("Which character's pronounciation is this?   n", "ん", 1, "hiragana")
question18 = Question("Which character's pronounciation is this?   mu", "む", 1, "hiragana")
question19 = Question("Which character's pronounciation is this?   mo", "も", 1, "hiragana")


question20 = Question("Which character's pronounciation is this?   tsu", "ツ", 1, "katakana")
question21 = Question("Which character's pronounciation is this?   na", "ナ", 1, "katakana")
question22 = Question("Which character's pronounciation is this?   nu", "ヌ", 1, "katakana")
question23 = Question("Which character's pronounciation is this?   n", "ン", 1, "katakana")
question24 = Question("Which character's pronounciation is this?   i", "イ", 1, "katakana")
question25 = Question("Which character's pronounciation is this?   hi", "ヒ", 1, "katakana")
question26 = Question("Which character's pronounciation is this?   su", "ス", 1, "katakana")
question27 = Question("Which character's pronounciation is this?   re", "レ", 1, "katakana")
question28 = Question("Which character's pronounciation is this?   fu", "フ", 1, "katakana")
question29 = Question("Which character's pronounciation is this?   o", "オ", 1, "katakana")


