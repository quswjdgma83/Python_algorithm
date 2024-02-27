def solution(babbling):
    valid_sounds = ["aya", "ye", "woo", "ma"]
    count = 0
    
    for word in babbling:
        # 복사본 문자열을 만들어 작업
        temp_word = word
        prev_sound = ""
        is_valid = True
        
        for sound in valid_sounds:
            # 현재 발음으로 임시 문자열에서 발음을 모두 대체
            temp_word = temp_word.replace(sound, f" {sound} ")
        
        # 분리된 발음들을 확인
        sounds_in_word = temp_word.split()
        
        for sound in sounds_in_word:
            # 연속되는 발음이 있는지, 혹은 유효하지 않은 발음이 포함되어 있는지 확인
            if sound == prev_sound or sound not in valid_sounds:
                is_valid = False
                break
            prev_sound = sound
        
        # 모든 발음이 유효하고 연속되지 않는 경우에만 카운트
        if is_valid and ''.join(sounds_in_word) == word:
            count += 1
    
    return count

# 테스트 케이스 실행
# test_cases = [
#     ["aya", "yee", "u", "maa"],
#     ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
# ]

# results = [solution(test_case) for test_case in test_cases]
# results
solution("ayayemaayaye")
