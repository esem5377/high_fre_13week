import numpy as np

def calculate_h_field(ux, uy, E, f):
    # 상산 정의 (진공 상태)
    u0 = 4 * np.pi * 1e-7
    e0 = 8.854e-12
    
    # 각주파수(w), 파수(k), 고유 임피던스(eta) 계산
    w = 2 * np.pi * f
    k_mag = w * np.sqrt(u0 * e0)
    eta = np.sqrt(u0 / e0)
    
    # Ex, Ey 계산 (ux 값이 0인지 아닌지에 따라 분기)
    if ux != 0:
        # Ey 계산 (양수 값 선택)
        Ey = E / np.sqrt(1 + (uy/ux)**2)
        # 내적 조건(ux*Ex + uy*Ey = 0)을 이용하여 Ex 계산
        Ex = -(uy/ux) * Ey
    else:
        # ux가 0이면 파동이 y축 방향으로 진행, 전기장은 x축 방향
        Ey = 0
        Ex = E
        
    # k 벡터와 E 벡터 정의 (z축 성분은 0)
    k_vec = np.array([ux, uy, 0]) # 방향 벡터만 사용해도 식 전개에 무방 (단위 벡터라 가정)
    E_vec = np.array([Ex, Ey, 0])
    
    # H 벡터 계산 (Cross product)
    # H = (k x E) / eta
    H_vec = np.cross(k_vec, E_vec) / eta
    
    Hx, Hy, Hz = H_vec
    return Hx, Hy, Hz

# 예시 실행
ux, uy = 1/np.sqrt(2), 1/np.sqrt(2) # 45도 방향 진행
E = 10 # V/m
f = 1e9 # 1 GHz
Hx, Hy, Hz = calculate_h_field(ux, uy, E, f)
print(f"H field: Hx={Hx:.6e}, Hy={Hy:.6e}, Hz={Hz:.6e}")
