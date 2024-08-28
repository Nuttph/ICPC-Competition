import math

def distance(p1, p2):
    """คำนวณระยะห่างระหว่างสองจุด p1 และ p2"""
    print(f'({p1[0]} - {p2[0]}) ** 2 + ({p1[1]} - {p2[1]}) ** 2')
    print(f'{math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)}')
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def longest_strip(polygon):
    """หาความยาวของเส้นตรงที่ยาวที่สุดในรูปหลายเหลี่ยม"""
    max_distance = 0
    n = len(polygon)
    
    # ตรวจสอบระยะห่างระหว่างทุกจุดยอด
    for i in range(n):
        for j in range(i + 1, n):
            print(f'pi = {polygon[i]} : pj = {polygon[j]}')
            max_distance = max(max_distance, distance(polygon[i], polygon[j]))
    
    return max_distance

# อ่านข้อมูลจากอินพุต
n = int(input())
polygon = []

for _ in range(n):
    x, y = map(int, input().split())
    polygon.append((x, y))

print(polygon)

# คำนวณและแสดงผลลัพธ์
result = longest_strip(polygon)
print(f"{result}")
