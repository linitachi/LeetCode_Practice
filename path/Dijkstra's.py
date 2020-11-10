# 演算法參考資料http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dijkstra.html
import sys


def loadPathMap(path):

    # 創建路徑
    with open(path) as f:
        numberOfNodes = 0
        numberOfNodes = int(f.readline().split()[0])
        map_list = [[sys.maxsize for j in range(numberOfNodes)]
                    for i in range(numberOfNodes)]
        for line in f:
            line = line.split()
            line = list(map(lambda x: int(x), line))
            map_list[line[0] - 1][line[1] - 1] = line[2]
    return map_list


def Dijkstra(map_list, start):
    # 初始化距離表
    distance_list = [sys.maxsize] * len(map_list)
    distance_list[start] = 0

    for i in range(len(map_list)):
        for j in range(len(map_list)):
            if distance_list[j] > map_list[start][j]+distance_list[start]:
                distance_list[j] = map_list[start][j]+distance_list[start]
        start = map_list[start].index(min(map_list[start]))
    print(distance_list)


if __name__ == "__main__":
    map_list = loadPathMap("path\path.txt")
    Dijkstra(map_list, 0)
