import time

# ==========================================
# 1. HÀM GỐC VÀ CÁC BIẾN THỂ LỖI (MUTANTS)
# ==========================================

# Hàm gốc (Original Program) cần kiểm thử
def is_adult_original(age):
    if age >= 18:
        return True
    else:
        return False

# Mutant 1: Thay đổi toán tử so sánh (>= thành >)
def is_adult_mutant_1(age):
    if age > 18:  # LỖI ĐỘT BIẾN Ở ĐÂY
        return True
    else:
        return False

# Mutant 2: Thay đổi toán tử so sánh (>= thành ==)
def is_adult_mutant_2(age):
    if age == 18:  # LỖI ĐỘT BIẾN Ở ĐÂY
        return True
    else:
        return False

# Mutant 3: Thay đổi giá trị logic trả về (False thành True)
def is_adult_mutant_3(age):
    if age >= 18:
        return True
    else:
        return True  # LỖI ĐỘT BIẾN Ở ĐÂY


# ==========================================
# 2. BỘ TEST CASE (TEST SUITE)
# ==========================================

# Bộ test ban đầu (Bộ test YẾU) - Chỉ gồm 2 test case cơ bản
weak_test_suite = [
    {"age": 20, "expected": True},   # Test Case 1
    {"age": 10, "expected": False}   # Test Case 2
]

# Bộ test cải tiến (Bộ test MẠNH) - Bổ sung thêm kiểm tra giá trị biên
strong_test_suite = [
    {"age": 20, "expected": True},   # Test Case 1
    {"age": 10, "expected": False},  # Test Case 2
    {"age": 18, "expected": True}    # Test Case 3 (Bổ sung để diệt Mutant 1)
]


# ==========================================
# 3. HÀM CHẠY KIỂM THỬ (TEST RUNNER)
# ==========================================

def run_mutation_testing(test_suite, suite_name):
    print(f"\n" + "="*50)
    print(f" BẮT ĐẦU ĐÁNH GIÁ: {suite_name}")
    print("="*50)
    
    # Danh sách các mutant cần kiểm tra
    mutants = [
        {"name": "Mutant 1 (Toán tử >)", "func": is_adult_mutant_1},
        {"name": "Mutant 2 (Toán tử ==)", "func": is_adult_mutant_2},
        {"name": "Mutant 3 (Trả về True ở else)", "func": is_adult_mutant_3},
    ]
    
    killed_count = 0
    total_mutants = len(mutants)
    
    for mutant in mutants:
        print(f"\n👉 Chạy bộ test trên [{mutant['name']}]...")
        mutant_killed = False
        
        # Chạy từng test case trên mutant hiện tại
        for i, test in enumerate(test_suite, 1):
            result = mutant["func"](test["age"])
            
            # Nếu kết quả của mutant KHÁC với kết quả mong đợi (kết quả của hàm gốc)
            if result != test["expected"]:
                print(f"   => ❌ Test Case {i} (age={test['age']}): Thất bại! (Kết quả thực tế: {result}, Mong đợi: {test['expected']})")
                mutant_killed = True
                break  # Chỉ cần 1 test case phát hiện ra lỗi, mutant sẽ bị tiêu diệt ngay lập tức
            else:
                print(f"   =>  Test Case {i} (age={test['age']}): Vượt qua (Pass)")
                
        if mutant_killed:
            print(f" 🔥 KẾT LUẬN: {mutant['name']} --> BỊ TIÊU DIỆT (Killed)!")
            killed_count += 1
        else:
            print(f" 🛡️ KẾT LUẬN: {mutant['name']} --> SỐNG SÓT (Survived)! -> [Bộ test yếu]")
            
    # Tính Mutation Score
    mutation_score = (killed_count / total_mutants) * 100
    print("\n" + "-"*40)
    print(f"📊 KẾT QUẢ CUỐI CÙNG CHO {suite_name}:")
    print(f"   - Số Mutant bị tiêu diệt: {killed_count}/{total_mutants}")
    print(f"   - ĐIỂM ĐỘT BIẾN (MUTATION SCORE): {mutation_score:.2f}%")
    print("-"*40)


# ==========================================
# 4. CHẠY CHƯƠNG TRÌNH CHÍNH
# ==========================================
if __name__ == "__main__":
    print("ỨNG DỤNG MINH HỌA MUTATION TESTING TRONG KIỂM THỬ PHẦN MỀM")
    time.sleep(1)
    
    # Giai đoạn 1: Chạy với bộ test yếu
    run_mutation_testing(weak_test_suite, "BỘ TEST BAN ĐẦU (YẾU - CHƯA CÓ GIÁ TRỊ BIÊN)")
    
    time.sleep(2)
    
    # Giai đoạn 2: Chạy với bộ test mạnh sau khi được nâng cấp
    run_mutation_testing(strong_test_suite, "BỘ TEST CẢI TIẾN (MẠNH - ĐÃ BỔ SUNG BIÊN AGE=18)")