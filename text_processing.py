#######################
# Test Processing I   #
#######################

"""
NLP에서 흔히하는 전처리는 소문자 변환, 앞뒤 필요없는 띄어쓰기를 제거하는 등의 텍스트 정규화 (text normalization)입니다. 
이번 숙제에서는 텍스트 처리 방법을 파이썬으로 배워보겠습니다.
"""


def normalize(input_string):
    """
     인풋으로 받는 스트링에서 정규화된 스트링을 반환함
     아래의 요건들을 충족시켜야함
    * 모든 단어들은 소문자로 되어야함
    * 띄어쓰기는 한칸으로 되어야함
    * 앞뒤 필요없는 띄어쓰기는 제거해야함

         Parameters:
             input_string (string): 영어로 된 대문자, 소문자, 띄어쓰기, 문장부호, 숫자로 이루어진 string
             ex - "This is an example.", "   EXTRA   SPACE   "

         Returns:
             normalized_string (string): 위 요건을 충족시킨 정규회된 string
             ex - 'this is an example.'

         Examples:
             >>> import text_processing as tp
             >>> input_string1 = "This is an example."
             >>> tp.normalize(input_string1)
             'this is an example.'
             >>> input_string2 = "   EXTRA   SPACE   "
             >>> tp.normalize(input_string2)
             'extra space'
    """

    # 모든 단어는 소문자로 변환 
    small_string = input_string.lower()
    
    # 시퀀스 순방향으로 체크하며 가장 앞 공백 제거 
    forward_check = []
    flag = False

    for i in small_string:
        if i != " ":
            flag = True

        if flag == True:
            forward_check.append(i)

    # 입력된 문자가 없으면 공백 문자열 반환
    if forward_check == []:
        return ""

    # 시퀀스 역방향으로 체크하며 가장 앞 공백 제거
    backword_check = []
    flag = False

    while forward_check:
        i = forward_check.pop()
        if i != " ":
            flag = True

        if flag == True:
            backword_check.insert(0,i)

    # 문자 중간에 존재하는 연속되는 공백 하나의 공백으로
    normalized_string = ""
    pre = True

    for i in backword_check:
        if i == " " and pre == True:
            pre = False

        elif i != " " and pre == False:
            normalized_string += " "
            normalized_string += i
            pre = True
            
        elif i != " " and pre == True:
            normalized_string += i

    return normalized_string


def no_vowels(input_string):
    """
    인풋으로 받는 스트링에서 모든 모음 (a, e, i, o, u)를 제거시킨 스트링을 반환함

        Parameters:
            input_string (string): 영어로 된 대문자, 소문자, 띄어쓰기, 문장부호로 이루어진 string
            ex - "This is an example."

        Returns:
            no_vowel_string (string): 모든 모음 (a, e, i, o, u)를 제거시킨 스트링
            ex - "Ths s n xmpl."

        Examples:
            >>> import text_processing as tp
            >>> input_string1 = "This is an example."
            >>> tp.normalize(input_string1)
            "Ths s n xmpl."
            >>> input_string2 = "We love Python!"
            >>> tp.normalize(input_string2)
            ''W lv Pythn!'
    """

    vowel = ['a','e','i','o','u','A','E','I','O','U']
    no_vowel_string = ""

    for i in input_string:
        if i not in vowel:
            no_vowel_string += i

    return no_vowel_string

