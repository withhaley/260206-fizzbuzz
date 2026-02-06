## 100 Prisoners Problem - 100,000회 시뮬레이션
import random

def play_random(n=100):
    """무작위 전략: 각 죄수가 무작위로 50개 상자 선택"""
    boxes = list(range(n))
    random.shuffle(boxes)
    return all(p in [boxes[i] for i in random.sample(range(n), n//2)] for p in range(n))

## 감사합니다. 
def play_optimal(n=100):
    """순환 전략: 자기 번호부터 시작해서 상자 안의 번호를 따라감"""
    boxes = list(range(n))
    random.shuffle(boxes)
    for prisoner in range(n):
        box = prisoner
        for _ in range(n // 2):
            if boxes[box] == prisoner:
                break # 박스에 죄수가 있다면 for 문 종료
            box = boxes[box]
        else:
            return False
    return True

if __name__ == "__main__":
    trials = 100_000
    
    random_wins = sum(play_random() for _ in range(trials))
    optimal_wins = sum(play_optimal() for _ in range(trials))
    
    print(f"시행 횟수: {trials:,}회")
    print(f"무작위 전략 성공률: {random_wins/trials*100:.4f}%")
    print(f"순환 전략 성공률: {optimal_wins/trials*100:.4f}%")
