#################
# import module
#################
import urllib3
from bs4 import BeautifulSoup
import certifi

##################
# define function
##################
def extract_data(soup):
    #<= 名前と必殺技名の収取流 =>#
    temp = soup.title.string.replace("の評価","")
    temp = temp.replace("- GameWith","")
    temp = temp.replace("【シンフォギアXD】","")

    name_skill=temp.split("|")
    # print(name_skill)

    #tableの抽出#
    divs  = soup.find_all("div")
    table = ""
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
            result=name_skill+tds
        else:
            result=None

    # print(result)

    return result


def main():
    #<= パラメータの設定 =>#
    url  = "https://symphogearxd.gamewith.jp/article/show/60789"
    http = urllib3.PoolManager(cert_reqs="CERT_REQUIRED",
                            ca_certs=certifi.where())
    request_result = http.request("GET",url)
    soup   = BeautifulSoup(request_result.data,"html.parser")
    result = extract_data(soup)
    print("結果：{}".format(result))


if __name__ =="__main__":
    main()
