import math

def calculate_thermal_noise(ts, b):
    """
    수신기 열잡음 전력을 계산하는 함수
    :param ts: 수신기 잡음 온도 (K)
    :param b: 수신기 대역폭 (Hz)
    :return: (n, ndBm) - W 단위 전력, dBm 단위 전력
    """
    k = 1.380649e-23  # 볼츠만 상수
    
    n = k * ts * b
    ndBm = 10 * math.log10(n) + 30
    
    return n, ndBm

if __name__ == "__main__":
    print("=== 수신기 열잡음 전력 계산기 ===")
    
    try:
        # 사용자로부터 직접 입력받기 (실수형으로 변환)
        ts_input = float(input("수신기 잡음 온도(K)를 입력하세요 (예: 290): "))
        b_input = float(input("수신기 대역폭(Hz)을 입력하세요 (예: 1000000): "))
        
        # 계산 함수 호출
        n_out, ndBm_out = calculate_thermal_noise(ts_input, b_input)
        
        # 결과 출력
        print("\n--- [계산 결과] ---")
        print(f"입력된 온도: {ts_input} K")
        print(f"입력된 대역폭: {b_input:,.0f} Hz")
        print(f"열잡음 전력 (n): {n_out:.4e} W")
        print(f"열잡음 전력 (ndBm): {ndBm_out:.4f} dBm")
        print("================================")
        
    except ValueError:
        print("\n[오류] 올바른 숫자를 입력해주세요. (문자나 공백은 입력할 수 없습니다.)")
