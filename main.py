import requests

res_parse_list = []
response = requests.get("https://porsche.ua/model/911-spirit-70")

response_text = response.text

response_parse = response_text.split("<strong>")

for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("1"):
        # print(parse_elem_1)
        for parse_elem_2 in parse_elem_1.split("</strong>"):
            # print(parse_elem_2)
            if parse_elem_2.startswith("1") and parse_elem_2[0].isdigit():
                #print(parse_elem_2)
                res_parse_list.append(parse_elem_2)

porsche = res_parse_list[1]
print("машина порш 911 Spirit 70 -" ,porsche, "грн")

def car():
    salary = int(input("введіть зарплату за місяць - "))
    percentage = int(input("введіть відсоток витрат - "))
    m = salary * (percentage / 100)
    car = int(porsche.replace(" ", ""))
    years = car/m/12
    print("Щоб заробити на цю машину вам треба", round(years, 2), "років")
car()