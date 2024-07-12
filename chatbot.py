import re
import os
from collections import Counter
import itertools
from class_all import *
import time

def count_common_elements(arr1, arr2):
    set1 = set(list(arr1))
    set2 = set(list(arr2))
    common_elements = set1.intersection(set2)
    return len(list(common_elements))

forward_rules = [
    (['S01'], ['D01', 'D02']),
    (['S02'], ['D01', 'D02', 'D11']),
    (['S03'], ['D02', 'D11']),
    (['S04'], ['D04']),
    (['S05'], ['D03', 'D05']),
    (['S06'], ['D02', 'D03', 'D05', 'D06', 'D08']),
    (['S07'], ['D03', 'D05', 'D06', 'D07', 'D08']),
    (['S08'], ['D03', 'D05', 'D06', 'D08']),
    (['S09'], ['D05', 'D06', 'D07']),
    (['S10'], ['D05', 'D06', 'D07']),
    (['S11'], ['D05', 'D06']),
    (['S12'], ['D05', 'D07']),
    (['S13'], ['D09']),
    (['S14'], ['D09']),
    (['S15'], ['D06', 'D07']),
    (['S16'], ['D10']),
    (['S17'], ['D10']),
    (['S18'], ['D10']),
    (['S19'], ['D02', 'D11']),
    (['S20'], ['D11']),
    (['S21'], ['D06', 'D07']),
    (['S22'], ['D06', 'D07']),
    (['S23'], ['D03', 'D05', 'D06', 'D07', 'D08']),
    (['S24'], ['D03', 'D07']),
    (['S25'], ['D01', 'D03']),
    (['S26'], ['D02', 'D08']),
]

backward_rules = [
    (['D01'], ['S01', 'S02', 'S25']),
    (['D02'], ['S01', 'S02', 'S06']),
    (['D02'], ['S01', 'S03']),
    (['D02'], ['S01', 'S19']),
    (['D03'], ['S05', 'S06', 'S25']),
    (['D03'], ['S05', 'S07', 'S25']),
    (['D03'], ['S05', 'S08', 'S25']),
    (['D03'], ['S05', 'S23', 'S25']),
    (['D04'], ['S04']),
    (['D05'], ['S05', 'S06', 'S24']),
    (['D05'], ['S05', 'S07', 'S24']),
    (['D05'], ['S05', 'S08', 'S24']),
    (['D05'], ['S05', 'S23', 'S24']),
    (['D05'], ['S08', 'S12']),
    (['D05'], ['S09', 'S12']),
    (['D05'], ['S10', 'S12']),
    (['D05'], ['S11', 'S12']),
    (['D05'], ['S17']),
    (['D06'], ['S06']),
    (['D06'], ['S07']),
    (['D06'], ['S08']),
    (['D06'], ['S09']),
    (['D06'], ['S10']),
    (['D06'], ['S11']),
    (['D06'], ['S15']),
    (['D06'], ['S21']),
    (['D06'], ['S22']),
    (['D06'], ['S23']),
    (['D07'], ['S07', 'S24']),
    (['D07'], ['S09', 'S24']),
    (['D07'], ['S10', 'S24']),
    (['D07'], ['S15', 'S24']),
    (['D07'], ['S21', 'S24']),
    (['D07'], ['S22', 'S24']),
    (['D07'], ['S23', 'S24']),
    (['D08'], ['S06', 'S26']),
    (['D08'], ['S07', 'S26']),
    (['D08'], ['S08', 'S26']),
    (['D08'], ['S23', 'S26']),
    (['D09'], ['S13']),
    (['D09'], ['S14']),
    (['D10'], ['S16']),
    (['D10'], ['S17']),
    (['D10'], ['S18']),
    (['D11'], ['S02', 'S20']),
    (['D11'], ['S03', 'S20']),
    (['D11'], ['S19', 'S20']),
]

db=ConvertData()
db.convertsukien()
db.converttinhhuong()

person = Person(None, None, None)
validate = Validate()


def welcome_question():
    print("-->Chatbot: Xin chào, tôi là Ball-Ball một chatbot giúp xác định các lỗi vị phạm trong 1 trận bóng!")
    print("-->Chatbot: Để bắt đầu xác định tình huống và đưa ra kết quả đầu tiên bạn hãy để lại email, tên và số điện thoại của bạn")

    print("-->Chatbot: Bạn hãy nhập tên của mình")
    person.name = validate.validate_name(input())
    print(f'-->Người dùng: Tên của tôi là {person.name}')
    print("--------------------*-------------------------")
    return person

def first_question(person):
    while True:
            print(f"{person.name} muốn biết thêm thông tin nào dưới đây:")
            print("1. Luật bóng đá của FiFa")
            print("2. Các giải đấu Anh, Đức, Châu Âu (2021-2022)")
            print("3. Xác định tình huống trong một trận đấu")
            print("4. Thoát")

            # Yêu cầu người dùng nhập số
            user_input = input("Nhập số từ 1 đến 4: ")
            print("--------------------*-------------------------")
            # Kiểm tra xem người dùng đã nhập số hay không
            if user_input.isdigit():
                choice = int(user_input)

                # Kiểm tra xem số có trong khoảng từ 1 đến 3 hay không
                if 1 <= choice <= 4:
                    if choice == 4:
                        print("Chúc bạn 1 ngày vui vẻ, cảm ơn bạn đã trò chuyện với BB <3")
                    return choice
                else:
                    print("Số bạn nhập không hợp lệ. Vui lòng nhập lại.")
                    print("--------------------*-------------------------")

            else:
                print("Vui lòng nhập một số từ 1 đến 3.")
                print("----------------*-----------------")

person = welcome_question()

def second_question():
    while(1):
        print(f'-->Chatbot: Chào {person.name}, bạn đang muốn tìm hiểu về luật bóng đán nào ?')
        print('1. Luật bóng đá FIFA là gì ?')
        print('2. FIFA yêu cầu bóng thi đấu như nào ?')
        print('3. Số lượng cầu thủ ?')
        print('4. Các trang bị của cầu thủ ?')
        print('5. Trọng tài ?')
        print('6. Trợ lý trọng tài ?')
        print('7. Thời gian thi đấu ?')
        print('8. Tái khởi động trận đấu ?')
        print('9. Bóng trong cuộc và ngoài cuộc ?')
        print('10. Cách tính bàn thắng  ?')
        print('11. Việt vị ?')
        print('12. Hành vi phạm luật trong bóng đá ?')
        print('13. Đá phạt trực tiếp hoặc gián tiếp ?')
        print('14. Phạt đèn ?')
        print('15. Ném biên ?')
        print('16. Phát bóng ?')
        print('17. Phạt góc ?')
        print('0. Không câu nào ở trên')
        print('---------------Câu trả lời của bạn---------------')
        answer = validate.validate_input_number_form(input())
        file_path = r'C:\Users\Acer\Dropbox\PC\Desktop\adu nam 4 roi\HTTT\CHTDTTT\luat\{}.txt'.format(answer)

        print(f'-->{person.name}: Lựa chọn của tôi {answer}')
        if (int(answer) < 0 or int(answer) > 17):
            print('-->Chatbot: Vui lòng nhập số từ 0 -> 17')
            continue
        elif (answer == '0'):
            print(f'-->Rất xin lỗi vì tôi chưa đủ thông tin cung cấp cho {person.name}')
            print("--------------------*-------------------------")
            break
        else:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    print(content)  # In ra nội dung của file
            except FileNotFoundError:
                print("File không tồn tại hoặc đường dẫn không chính xác.")
            except Exception as e:
                print("Đã xảy ra lỗi:", e)
            break

def third1_question(person):
    chosen_values = []  # Tạo một danh sách rỗng để lưu giá trị khi choice = 1, 2 hoặc 3

    while True:
        print(f"{person.name} Bạn muốn biết thông tin về giải đấu nước nào :")
        print("1. Anh")
        print("2. Đức")
        print("3. Châu Âu")

        user_input = input("Nhập số từ 1 đến 3: ")
        print("--------------------*-------------------------")
        if user_input.isdigit():
            choice = int(user_input)

            # Kiểm tra xem số có trong khoảng từ 1 đến 3 hay không
            if 1 <= choice <= 3:
                return choice
            else:
                print("Số bạn nhập không hợp lệ. Vui lòng nhập lại.")
                print("--------------------*-------------------------")

        else:
            print("Vui lòng nhập một số từ 1 đến 3.")
            print("----------------*-----------------")

def third2_question(person, choose):
    while True:
        if choose == 1:
            print(
                f"{person.name} Bạn muốn biết thông tin về giải đấu nào của nước Anh :"
            )
            print("1. Ngoại hạng")
            print("2. Giải hạng nhất")

        if choose == 2:
            print(
                f"{person.name} Bạn muốn biết thông tin về giải đấu nào của nước Đức :"
            )
            print("1. Giải Bundesliga")
            print("2. Giải DFB-Pokal")

        if choose == 3:
            print(
                f"{person.name} Bạn muốn biết thông tin về giải đấu nào của Châu Âu :"
            )
            print("1.Cúp C1 ")
            print("1.Cúp C2 ")

        user_input = input("Nhập số từ 1 đến 2: ")
        print("--------------------*-------------------------")
        if user_input.isdigit():
            choice = int(user_input)

            # Kiểm tra xem số có trong khoảng từ 1 đến 3 hay không
            if 1 <= choice <= 2:
                return choice
            else:
                print("Số bạn nhập không hợp lệ. Vui lòng nhập lại.")
                print("--------------------*-------------------------")

        else:
            print("Vui lòng nhập một số từ 1 đến 2.")
            print("----------------*-----------------")

def third3_question(person):
    while True:
        print(f"{person.name} Bạn muốn biết thông tin về giải đấu đó năm bao nhiêu :")
        print("1. 2021")
        print("2. 2022")

        user_input = input("Nhập số từ 1 đến 2: ")
        print("--------------------*-------------------------")
        if user_input.isdigit():
            choice = int(user_input)

            # Kiểm tra xem số có trong khoảng từ 1 đến 3 hay không
            if 1 <= choice <= 2:
                if choice == 1:
                    return 2021
                else:
                    return 2022
            else:
                print("Số bạn nhập không hợp lệ. Vui lòng nhập lại.")
                print("--------------------*-------------------------")
        else:
            print("Vui lòng nhập một số từ 1 đến 2.")
            print("----------------*-----------------")

def third_question(person):
    result = third1_question(person)
    result2 = third2_question(person, result)
    result3 = third3_question(person)

    filename = str(result) + "_" + str(result2) + "_" + str(result3) + ".txt"
    # print(filename)
    full_path = os.path.join(
        r"C:\Users\Acer\Dropbox\PC\Desktop\adu nam 4 roi\HTTT\CHTDTTT\giai_dau\\", filename
    )
    try:
        with open(full_path, "r", encoding="utf-8") as full:
            content = full.read()
            print(content)
    except FileNotFoundError:
        print("File không tồn tại hoặc đường dẫn không chính xác.")
    except Exception as e:
        print("Đã xảy ra lỗi:", e)

def forth1_question(list_situation_of_person, person):
    List_situation = [db.resulttinhhuong[0], db.resulttinhhuong[1], db.resulttinhhuong[2],
                 db.resulttinhhuong[3], db.resulttinhhuong[4], db.resulttinhhuong[5]]

    while (1):
        if len(list_situation_of_person ) == len(List_situation) or len(list_situation_of_person ) == 3:
            break
        if len(list_situation_of_person ) == 0:
            print(f'-->Chatbot: {person.name} bạn muốn xác định tình huống có liên quan nào dưới đây (Nhập số thứ tự của tình huống để chọn. Có thể lựa chọn nhiều)')
        else:
            print(f'-->Chatbot: {person.name} ngoài tình huống đó ra còn thêm tình huống nào nữa không (Nhập số thứ tự của tình huống để chọn. Có thể lựa chọn nhiều)')

        count = 1
        for i in List_situation:
            if i not in list_situation_of_person :
                print(f'{count}. {i["name"]} \n')
            count += 1

        print("0. Không có tình huống nào kể trên\n -------------Câu trả lời của bạn--------------")
        answer = validate.validate_input_number_form(input())
        print("--------------------*-------------------------")
        print(f'-->{person.name}: Câu trả lời của tôi là {answer}')

        if answer == '0':
            break
        elif int(answer) < 0 or int(answer) > 6:
            print('-->Chatbot: Vui lòng nhập 1 số từ 0 tới 6')
            continue
        else:
            selected_situation = List_situation[int(answer) - 1]
            List_situation.pop(int(answer) - 1)
            list_situation_of_person.append(selected_situation["id"])
        print(
            f'-->Chatbot: Danh sách mã các tình huống {person.name} gặp phải:')
        for s in list_situation_of_person:
                res = db.get_tinhhuong_by_id(s)
                print(res["name"])
    return list_situation_of_person 

def forth2_question(list_situation_of_person, person):
    List_situation = [db.resulttinhhuong[6], db.resulttinhhuong[7], db.resulttinhhuong[8],
                 db.resulttinhhuong[9], db.resulttinhhuong[10], db.resulttinhhuong[11]]

    while (1):
        if len(list_situation_of_person ) == len(List_situation):
            break
        if len(list_situation_of_person ) == 0:
            print(f'-->Chatbot: {person.name} bạn muốn xác định tình huống có liên quan nào dưới đây (Nhập số thứ tự của tình huống để chọn. Có thể lựa chọn nhiều)')
        else:
            print(f'-->Chatbot: {person.name} ngoài tình huống đó ra còn thêm tình huống nào nữa không (Nhập số thứ tự của tình huống để chọn. Có thể lựa chọn nhiều)')
           

        count = 1
        for i in List_situation:
            if i not in list_situation_of_person :
                print(f'{count}. {i["name"]} \n')
            count += 1

        print("0. Không có tình huống nào kể trên\n -------------Câu trả lời của bạn--------------")
        answer = validate.validate_input_number_form(input())
        print("--------------------*-------------------------")
        print(f'-->{person.name}: Câu trả lời của tôi là {answer}')

        if answer == '0':
            break
        elif int(answer) < 0 or int(answer) > 6:
            print('-->Chatbot: Vui lòng nhập 1 số từ 0 tới 6')
            continue
        else:
            selected_situation = List_situation[int(answer) - 1]
            List_situation.pop(int(answer) - 1)
            list_situation_of_person.append(selected_situation["id"])
        print(
            f'-->Chatbot: Danh sách mã các tình huống {person.name} gặp phải:')
        for s in list_situation_of_person:
                res = db.get_tinhhuong_by_id(s)
                print(res["name"])
    return list_situation_of_person 

def forth3_question(list_situation_of_person, person):
    List_situation = [db.resulttinhhuong[12], db.resulttinhhuong[13], db.resulttinhhuong[14],
                 db.resulttinhhuong[15], db.resulttinhhuong[16], db.resulttinhhuong[17],db.resulttinhhuong[18]]

    while (1):
        if len(list_situation_of_person ) == len(List_situation):
            break
        if len(list_situation_of_person ) == 0:
            print(f'-->Chatbot: {person.name} bạn muốn xác định tình huống có liên quan nào dưới đây (Nhập số thứ tự của tình huống để chọn)')
        else:
            print(f'-->Chatbot: {person.name} ngoài tình huống đó ra còn thêm tình huống nào nữa không (Nhập số thứ tự của tình huống để chọn)')

        count = 1
        for i in List_situation:
            if i not in list_situation_of_person :
                print(f'{count}. {i["name"]} \n')
            count += 1

        print("0. Không có tình huống nào kể trên\n -------------Câu trả lời của bạn--------------")
        answer = validate.validate_input_number_form(input())
        print("--------------------*-------------------------")
        print(f'-->{person.name}: Câu trả lời của tôi là {answer}')

        if answer == '0':
            break
        elif int(answer) < 0 or int(answer) > 7:
            print('-->Chatbot: Vui lòng nhập 1 số từ 0 tới 7')
            continue
        else:
            selected_situation = List_situation[int(answer) - 1]
            List_situation.pop(int(answer) - 1)
            list_situation_of_person.append(selected_situation["id"])
        print(
            f'-->Chatbot: Danh sách mã các tình huống {person.name} gặp phải:')
        for s in list_situation_of_person:
                res = db.get_tinhhuong_by_id(s)
                print(res["name"])
    return list_situation_of_person 

def forth4_question(list_situation_of_person, person):
    List_situation = [db.resulttinhhuong[19], db.resulttinhhuong[20], db.resulttinhhuong[21],
                 db.resulttinhhuong[22], db.resulttinhhuong[23], db.resulttinhhuong[24],db.resulttinhhuong[25]]

    while (1):
        if len(list_situation_of_person ) == len(List_situation):
            break
        if len(list_situation_of_person ) == 0:
            print(f'-->Chatbot: {person.name} bạn muốn xác định tình huống có liên quan nào dưới đây (Nhập số thứ tự của tình huống để chọn. Có thể lựa chọn nhiều)')
        else:
            print(f'-->Chatbot: {person.name} ngoài tình huống đó ra còn thêm tình huống nào nữa không (Nhập số thứ tự của tình huống để chọn. Có thể lựa chọn nhiều)')

        count = 1
        for i in List_situation:
            if i not in list_situation_of_person :
                print(f'{count}. {i["name"]} \n')
            count += 1

        print("0. Không có tình huống nào kể trên\n -------------Câu trả lời của bạn--------------")
        answer = validate.validate_input_number_form(input())
        print("--------------------*-------------------------")
        print(f'-->{person.name}: Câu trả lời của tôi là {answer}')

        if answer == '0':
            break
        elif int(answer) < 0 or int(answer) > 7:
            print('-->Chatbot: Vui lòng nhập 1 số từ 0 tới 7')
            continue
        else:
            selected_situation = List_situation[int(answer) - 1]
            List_situation.pop(int(answer) - 1)
            list_situation_of_person.append(selected_situation["id"])
        print(
            f'-->Chatbot: Danh sách mã các tình huống {person.name} gặp phải:')
        for s in list_situation_of_person:
                res = db.get_tinhhuong_by_id(s)
                print(res["name"])
    return list_situation_of_person 

def forth_question(list_situation_of_person):
    result = forth1_question(list_situation_of_person,person)
    if(len(result)<3):
        result=forth2_question(result,person)
    if(len(result)<3):
        result=forth3_question(result,person)
    if(len(result)<3):
        result=forth4_question(result,person)
    return result

def forward_channing(list_situation_of_person):
    mang =[]
    for s in list_situation_of_person:
        for rule in forward_rules:
            if s == rule[0][0]:
                mang.append(rule[1])

    mang_lien_ket = list(itertools.chain(*mang))

    # Đếm tần suất xuất hiện của từng phần tử
    dem_so_phan_tu = Counter(mang_lien_ket)

    # Tìm phần tử có số lần xuất hiện nhiều nhất
    tan_suat_cao_nhat = max(dem_so_phan_tu.values())
    cac_phan_tu_xuat_hien_nhieu_nhat = [phan_tu for phan_tu, tan_suat in dem_so_phan_tu.items() if tan_suat == tan_suat_cao_nhat]

    # Nếu chỉ có một phần tử có số lần xuất hiện cao nhất, trả về phần tử và số lần xuất hiện
    return cac_phan_tu_xuat_hien_nhieu_nhat, tan_suat_cao_nhat

def backward_channing(list_situation_of_person,list_event_precdict):
    result = []
    max = -1
    min = 0
    for e in list_event_precdict:
        for rule in backward_rules:
            if e==rule[0][0]:
                if count_common_elements(list_situation_of_person,rule[1]) > max:
                    max =  count_common_elements(list_situation_of_person,rule[1])
        if max>min:
            result.clear()
            result.append(e)
            min = max
        elif max == min:
            result.append(e)
    return result



tmp = first_question(person)

while(tmp!=4):
    if(tmp==1):
        second_question()
    if(tmp==2):
        third_question(person)
    if(tmp==3):
        list_situation_of_person = []
        list_situation_of_person+=forth_question(list_situation_of_person)
        list_situation_of_person = sorted(list(set(list_situation_of_person)))
        if len(list_situation_of_person)==0:
            print('-->Chatbot: Xin lỗi bạn vì trong danh sách các tình huống của tôi không có tình huống bạn cần xác định')
            print("-----------------------------------------------*-------------------------------------------------------")
        else:
            list_event_precdict , frequency = forward_channing(list_situation_of_person)

            print('-->Chatbot: Từ những tình huống : ')
            for s in list_situation_of_person:
                res = db.get_tinhhuong_by_id(s)
                print(res["name"])

            if frequency == len(list_situation_of_person):
                print('-->Các kết quả có thể xảy ra là : ')
                for e in list_event_precdict:
                    res = db.get_sukien_by_id(e)
                    print(res["name"])
                print("--------------------*-------------------------")
            else:
                result = backward_channing(list_situation_of_person,list_event_precdict)
                print('-->Các kết quả có thể xảy ra là : ')
                for e in result:
                    res = db.get_sukien_by_id(e)
                    print(res["name"])
                print()
                print("--------------------*-------------------------")
        list_situation_of_person.clear()
        time.sleep(5)
    print('-->Chatbot: Bạn có muốn tiếp tục trò truyện cùng với BB không (yes/no):')
    answer = validate.validate_binary_answer(input())
    if answer:
        tmp = first_question(person)

    else:
        break;
