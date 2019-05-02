#################
# import module
#################
import urllib3
from bs4 import BeautifulSoup
import certifi

##################
# define function
##################
def extract_url_list(url):
    #<= webページへのリクエスト=>#
    http = urllib3.PoolManager(cert_reqs="CERT_REQUIRED",
                            ca_certs=certifi.where())
    request_result = http.request("GET",url)
    soup   = BeautifulSoup(request_result.data,"html.parser")

    #tableの取得#
    tables  = soup.find_all("table")
    for tag in tables:
        try:
            string_ = tag.get("class").pop(0)
            #<=キャラリストの場合、データを取得=>#
            if string_ in "sorttable":
                # print("in")
                trs = tag.find_all("tr")
                break
        except:
            pass

    #<= 各行からリンクを抽出 =>#
    url_list=[]
    for tr in trs:
        td_list = tr.find_all("td")
        for td in td_list:
            a_list=td.find_all("a")
            a_list=[a.get("href") for a in a_list]
            #<=リンクがない場合はコンティニュー=>#
            if len(a_list) == 0:
                continue
            url_list.append(a_list[0])

    #<=リストの中から同じURLを消す=>#
    result = list(set(url_list))

    return result

#<= テキストファイルにデータを書き出す =>#
def write_text(url_result,save_file):
    with open(save_file,mode="w") as f:
        for url in url_result:
            f.write(url+"\n")
    print("done")

def main():
    #<= パラメータの設定 =>#
    url  = "https://symphogearxd.gamewith.jp/article/show/60694"

    #<=ulrの取得=>#
    result =extract_url_list(url)

    #<=データをテキストに保存する=>#
    save_file="./url_list.txt"
    write_text(result,save_file)


if __name__ =="__main__":
    main()
