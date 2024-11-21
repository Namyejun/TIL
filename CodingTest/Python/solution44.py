import re

def solution(new_id):
    answer = ''
    while new_id != answer:
        answer = new_id
        new_id = str(new_id)
        # 1
        new_id = new_id.lower()
        
        # 2
        rule = re.compile('[~!@#$%^&*()=+\[\{\]\}:?,<>/]+')
        new_id = rule.sub('', new_id)

        # 3
        rule = re.compile('[.]{2,}')
        new_id = rule.sub('.', new_id)

        # 4
        rule = re.compile("^[.]")
        new_id = rule.sub('', new_id)
        rule = re.compile("[.]$")
        new_id = rule.sub('', new_id)
        
        # 5
        if len(new_id) == 0:
            new_id = 'aaa'

        # 6
        if len(new_id) > 15:
            new_id = new_id[:15]

        # 7
        if len(new_id) <= 2:
            new_id = new_id + new_id[-1]*(3 - len(new_id))
        
    return new_id