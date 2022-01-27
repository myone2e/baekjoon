while True:
    try: # 기본적으로 실행되는 코드
        A, B = map(int, input().split())
        print(A+B)
    except: # 에러 발생 시 실행되는 코드 # 특정 오류 지정도 가능
        break
    
    # else는 예외 발생하지 않았을 때 실행되는 코드