import re
def solution(new_id):

    id = new_id.lower()

    #2단계 - 알파벳소문자, 숫자, -,_,. 제외 제거
    id = re.sub('[^a-z0-9\-_.]', '', id)

    #3단계
    id = re.sub('\.+','.',id)
    #4단계
    id = re.sub('^[.]|[.]$','',id)
    #5단계, 6단계
    id = 'a' if len(id)==0 else id[:15]
    id = re.sub('^[.]|[.]$','',id)
    #7단계
    id = id if len(id)>2 else id + ''.join([id[-1] for i in range(3-len(id))])


    return id