import numpy as np

def analyze_polarization():
    # 1. 사용자로부터 복소수 Ex, Ey 입력받기
    print("--- 복소수 전기장 성분 입력 ( 예: 1+0j 또는 0-1j ) ---")
    try:
        Ex_complex = complex(input("Ex (V/m) 입력: "))
        Ey_complex = complex(input("Ey (V/m) 입력: "))
    except ValueError:
        print("올바른 복소수 형식이 아닙니다. 파이썬 복소수 형식(a+bj)으로 입력해주세요.")
        return

    # theta (w*t) 값을 0에서 2*pi까지 1000등분
    theta = np.linspace(0, 2 * np.pi, 1000)
    
    # Ex, Ey의 크기(magnitude)와 위상각(phase angle) 추출
    Ex_mag = np.abs(Ex_complex)
    Ex_phase = np.angle(Ex_complex)
    
    Ey_mag = np.abs(Ey_complex)
    Ey_phase = np.angle(Ey_complex)
    
    # 시간에 따른 Ex(t), Ey(t) 궤적 계산
    Ex_t = Ex_mag * np.cos(theta + Ex_phase)
    Ey_t = Ey_mag * np.cos(theta + Ey_phase)
    
    # 합성 전기장 크기 E(t) 계산
    E_t = np.sqrt(Ex_t**2 + Ey_t**2)
    
    # a) 최소값, b) 최대값 산출
    min_E = np.min(E_t)
    max_E = np.max(E_t)
    
    # c) Axial Ratio (AR) 계산
    AR = max_E / min_E if min_E != 0 else float('inf')
    
    # d) Gamma (타원 장축 각도) 계산
    # max_E가 발생하는 인덱스 추출
    max_indices = np.where(np.isclose(E_t, max_E))[0]
    
    # 최대값이 발생하는 theta 중 가장 작은 값 선택 (라디안)
    gamma_rad = theta[max_indices[0]]
    
    # 라디안 단위를 디그리(degree) 단위로 변환
    gamma_deg = np.degrees(gamma_rad)
    
    # 결과 출력
    print("\n--- 분석 결과 ---")
    print(f"a) min(E)          : {min_E:.4f} V/m")
    print(f"b) max(E)          : {max_E:.4f} V/m")
    print(f"c) Axial Ratio (AR): {AR:.4f}")
    print(f"d) Gamma (degree)  : {gamma_deg:.2f} deg")

# 함수 실행
if __name__ == "__main__":
    analyze_polarization()
