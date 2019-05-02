#################
# import module
#################
import urllib3
from bs4 import BeautifulSoup
import certifi

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

def main():
    #<= パラメータの設定 =>#
    url  = "https://symphogearxd.gamewith.jp/article/show/60789"
    result = extract_data(url)
    print("結果：{}".format(result))


if __name__ =="__main__":
    main()


