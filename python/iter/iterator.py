"""Realisation of class-container Sentence and iterator SentenceIterator for it
"""
import re


class SentenceIterator:
    """
    Class-iterator
    """
    def __init__(self, words):
        self.words = words

    def _gen_word(self):
        if self.words:
            return self.words.pop(0)
        raise StopIteration

    def __next__(self):
        return self._gen_word()

    def __iter__(self):
        return self


class MultipleSentencesError(Exception):
    """
    Class-exception for multiple-sentence error
    """
    def __init__(self, text):
        super().__init__(self)
        self.txt = text


class Stringable:
    """
    Class-descriptor for variable text
    """
    def __init__(self):
        self.name = ''

    def __set__(self, instance, value):
        pattern = r'[A-z А-я 1-9]+[\.\.\.|\.|!|\?]'
        if not isinstance(value, str):
            raise TypeError(
                print(f"'{value[:20]}...' not a string")
            )
        if len(re.findall(pattern, value)) > 1:
            raise MultipleSentencesError(
                print(f"'{value[:20]}...' should consist of only one sentence")
            )
        if value[-1] not in '!.?':
            raise ValueError(
                print(f"'{value[:20]}...' not an ended sentence")
            )
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)


class Sentence:
    """
    Class container for iterator
    """
    text = Stringable()

    def __init__(self, text: str):
        self.text = text.replace('\n', '')

    def __repr__(self):
        return f"<Sentence(words={len(self.words)}, " \
               f"other_chars={len(self.other_chars)})>"

    def __iter__(self):
        return SentenceIterator(self.words)

    def __getitem__(self, index):
        sl_list = self.words[index]
        if isinstance(index, int):
            sent = ''.join(sl_list)
        else:
            sent = ' '.join(sl_list)
        return sent

    def _words(self):
        pattern = r'[\w\d]+|[\.?!,;:-]'
        lst = re.findall(pattern, self.text)
        return (word for word in lst)

    @property
    def words(self):
        """
        return a list of words from generator
        :return: list[str]
        """
        pattern = r'[A-zА-я]+'
        words = [word for word in self._words() if re.match(pattern, word)]
        return words

    @property
    def other_chars(self):
        """
        Return a list of other symbols from generator
        :return: list[str]
        """
        pattern = r'[^A-zА-я]'
        chars = [word for word in self._words() if re.match(pattern, word)]
        return chars


TEXT = r"""В 1800-х годах, в те времена, когда не было еще ни железных,
ни шоссейных дорог, ни газового, ни стеаринового света, ни пружинных низких
диванов, ни мебели без лаку, ни разочарованных юношей со стеклышками,
ни либеральных философов-женщин, ни милых дам-камелий, которых так много
развелось в наше время, – в те наивные времена, когда из Москвы, выезжая в
Петербург в повозке или карете, брали с собой целую кухню домашнего
приготовления, ехали восемь суток по мягкой, пыльной или грязной дороге и
верили в пожарские котлеты, в валдайские колокольчики и бублики, – когда в
длинные осенние вечера нагорали сальные свечи, освещая семейные кружки из
двадцати и тридцати человек, на балах в канделябры вставлялись восковые и
спермацетовые свечи, когда мебель ставили симметрично, когда наши отцы были
еще молоды не одним отсутствием морщин и седых волос, а стрелялись за женщин
и из другого угла комнаты бросались поднимать нечаянно и не нечаянно
уроненные платочки, наши матери носили коротенькие талии и огромные рукава и
решали семейные дела выниманием билетиков, когда прелестные дамы-камелии
прятались от дневного света, – в наивные времена масонских лож, мартинистов,
тугендбунда, во времена Милорадовичей, Давыдовых, Пушкиных, – в губернском
городе К был съезд помещиков, и кончались дворянские выборы."""

# Your code has been rated at 10.00/10 (previous run: 9.86/10, +0.14)

sentence = Sentence(TEXT)
# print(sentence._words(), '\n')
# >> <generator object Sentence._words.<locals>.<genexpr> at 0x1029d37b0>
print(sentence.text, '\n')
# >> В 1800-х годах, в те времена, когда не было еще ни железных, ни ...
print(sentence, '\n')
# <Sentence(words=178, other_chars=40)>
print(sentence.words, '\n')
# >> ['В', 'х', 'годах', 'в', 'те', 'времена', 'когда', 'не', 'было', 'еще',...
print(sentence.other_chars, '\n')
# >> ['1800', '-', ',', ',', ',', ',', ',', ',', ',', ',', ',', '-', ',',...
print(sentence[4:16], '\n')
# >> те времена когда не было еще ни железных ни шоссейных дорог ни
for s in sentence:
    print(s)
# >> В
# >> х
# >> годах
# >> в
# >> те
# >> ...
# >> выборы
print()
print(sentence[50], '\n')
# >> когда
