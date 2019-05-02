#################
# import module
#################
import urllib3
from bs4 import BeautifulSoup
import certifi
import time
import csv
import sys

##################
# define function
##################
def extract_data(url):
    #<= webページへのリクエスト=>#
    http = urllib3.PoolManager(cert_reqs="CERT_REQUIRED",
                            ca_certs=certifi.where())
    request_result = http.request("GET",url)
    soup   = BeautifulSoup(request_result.data,"html.parser")

    #<= 名前と必殺技名の収集 =>#
    temp = soup.title.string.replace("の評価","")
    temp = temp.replace("- GameWith","")
    temp = temp.replace("【シンフォギアXD】","")

    name_skill=temp.split("|")
    name_skill=[i.strip(" ") for i in name_skill]
    # print(name_skill)

    #tableの抽出#
    divs  = soup.find_all("div")
    table = ""
    result = []
    for tag in divs:
        try:
            string_ = tag.get("class").pop(0)
            if string_ in "symphogearxd_gear_table1":
                table=tag.find_all("tr")
                break
        except:
            pass
    #<= 行の抽出=>#
    for tr in table:
        th_list = tr.find_all("th")
        th_string_list=[i.string for i in th_list]
        # print(th_string_list)
        #<=星6のデータがあるときのみデータを抽出=>#
        if "初期レアリティ" in th_string_list:
            a_tag=tr.find("a")
            rarity = [a_tag.string]
        elif "属性" in th_string_list:
            a_tag=tr.find("a")
            attribution = [a_tag.string]
        else:
            result=None
    for tag in divs:
        try:
            string_ = tag.get("class").pop(0)
            if string_ in "symphogearxd_gear_table2":
                table=tag.find_all("tr")
                break
        except:
            pass
    #<= 行の抽出=>#
    for tr in table:
        th_list = tr.find_all("th")
        th_string_list=[i.string for i in th_list]
        # print(th_string_list)
        #<=星6のデータがあるときのみデータを抽出=>#
        if "星6" in th_string_list:
            tds=tr.find_all("td")
            tds=[i.string for i in tds]
            # print(tds)
            result = rarity + attribution + name_skill + tds
        else:
            result=None

    # print(result)

    return result

def read_text(text_path):
    with open(text_path) as f:
        lines = f.readlines()
        data=[line.rstrip("\n")for line in lines]
    # print(data)
    return data

def main():
    #<= パラメータの設定 =>#
    text_path="./url_list.txt"
    url_list=read_text(text_path)
    save_file_path="./symphogear.csv"
    save_file = open(save_file_path,"w")
    writer = csv.writer(save_file,lineterminator='\n')
    print("url_length:{}".format(len(url_list)))
    columns=["初期レアリティ","属性","名前","必殺技","HP","ATK","DEF","SPD","CTR","CTD"]
    writer.writerow(columns)
    for index in range(len(url_list)):
        url = url_list[index]
        result = extract_data(url)
        if result is None:
            continue
        sys.stdout.write("\r結果：{}".format(result))
        writer.writerow(result)
        time.sleep(3)
    save_file.close()
    # url  = "https://symphogearxd.gamewith.jp/article/show/60789"
    # result = extract_data(url)
    # print("結果：{}".format(result))


if __name__ =="__main__":
    main()
