#[?] 검색 알고리즘, 되어있는 데이터를 이진 검색을 사용하여 반씩 나눠서 검색
def main():
    #Input
    data = [1, 3, 5 , 7, 9]
    N = len(data)
    search = 3 #검색할 데이터
    flag = False # 플래그 변수: 찾으면 True 찾지 못하면 False
    index = -1 #인덱스 변수: 찾은 위치

    #Process: 이진검색 알고리즘(Index Scan)
    low = 0
    high = N-1
    while low <= high:
        mid = int((low+high)/2)
        if data[mid] == search:
            flag = True;
            index = mid;
            break;
        if data[mid] > search:
            high = mid -1
        else:
            low = mid + 1

    #Output
    if flag:
        print(f"{search}를 {index}위치에서 찾았습니다.")
    else:
        print("찾지 못했습니다.")


if __name__ == "__main__":
    main()