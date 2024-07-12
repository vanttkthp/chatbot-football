import re

import mysql.connector
import json
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="V@nDC1684",
    database="football"
)

mycursor = mydb.cursor()
mydb.commit()
class ConvertData:
    """
    Truy vấn và xử lý dữ liệu
    """
    def __init__(self):
        self.resultsukien = []
        self.resulttinhhuong = []

    def convertsukien(self):
        """
        Lấy dữ liệu bảng bệnh
        """
        dbsukien = mydb.cursor()
        dbsukien.execute("SELECT * FROM football.su_kien;")
        sukien = dbsukien.fetchall()
        dirsukien = {}
        for i in sukien:
            dirsukien['id'] = i[0]
            dirsukien['name'] = i[1]
            dirsukien['detail'] = i[2]
            self.resultsukien.append(dirsukien)
            dirsukien = {}

    def converttinhhuong(self):
        """
        Lấy dữ liệu từ bảng tinhhuong
        """
        dbtinhhuong = mydb.cursor()
        dbtinhhuong.execute("SELECT * FROM football.tinh_huong;")
        tinhhuong = dbtinhhuong.fetchall()
        dirtinhhuong = {}
        # resulttinhhuong=[]
        for i in tinhhuong:
            dirtinhhuong['id'] = i[0]
            dirtinhhuong['name'] = i[1]
            self.resulttinhhuong.append(dirtinhhuong)
            dirtinhhuong = {}
    
    def get_sukien_by_id(self, id_sukien):
        """
        Tìm sukien dựa trên id
        """
        for i in self.resultsukien:
            if i["id"] == id_sukien:
                return i
        return 0

    def get_tinhhuong_by_id(self, id_tinhhuong):
        for i in self.resulttinhhuong:
            if i["id"] == id_tinhhuong:
                return i
        return 0

class Person:
    def __init__(self, name, phoneNumber, email):
        self.name = name

    def __str__(self):
        return f"{self.name}"

class Validate:
    def __init__(self) -> None:
        pass

    def validate_input_number_form(self,value):
        while (1):
            valueGetRidOfSpace = ''.join(value.split(' '))
            check = valueGetRidOfSpace.isnumeric()
            if (check):
                return valueGetRidOfSpace
            else:
                print("-->Chatbot: Vui lòng nhập 1 số dương")
                value = input()

    def validate_phonenumber(self,value):
        while (1):
            valueGetRidOfSpace = ''.join(value.split(' '))
            check = valueGetRidOfSpace.isnumeric()
            if (check):
                return valueGetRidOfSpace
            else:
                print("-->Chatbot: Vui lòng nhập 1 số điện thoại đúng định dạng")
                value = input()


    def validate_email(self, email):
        while (1):
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

            if (re.fullmatch(regex, email)):
                # print("Chatbot:Tôi đã nhận được thông tin Email của bạn")
                return email

            else:
                print("-->Chatbot: Vui lòng nhập lại email")
                email = input()

    def validate_name(self, value):
        while (1):
            valueGetRidOfSpace = ''.join(value.split(' '))

            check = valueGetRidOfSpace.isalpha()
            if (check):
                # print("Tôi đã nhận được thông tin Tên của bạn")
                return value
            else:
                print("-->Chatbot: Vui lòng nhập lại tên ! ")
                value = input()

    def validate_binary_answer(self, value):
        acceptance_answer_lst = ['1', 'y', 'yes', 'co', 'có']
        decline_answer_lst = ['0', 'n', 'no', 'khong', 'không']
        value = value+''
        while (1):
            if (value) in acceptance_answer_lst:
                return True
            elif value in decline_answer_lst:
                return False
            else:
                print(
                    "-->Chatbot: Câu trả lời không hợp lệ. Vui lòng nhập lại câu trả lời")
                value = input()
