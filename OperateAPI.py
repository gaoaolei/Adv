import requests


class APIData(object):
    def getdata(self, url, headers):
        """忽略警告"""
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=url, headers=headers, verify=False)
        print(response.json())
        return response.json()


if __name__ == "__main__":
    header = {"channel": "unknown",
              "is-white": "0",
              "hardware-id": "ffffffff-8d61-83d7-ffff-ffffc50eefef",
              "uuid": "00000000-6ee7-9cb3-ffff-ffffe9983c01",
              "device-id": "20190712141352c5590aeffbbec19d7b474f3958f971c8018c311326c075ea",
              "mac": "E0:13:B5:C0:04:E7",
              "platform": "android",
              "app-version": "40063",
              "sys-ver": "8.1.0",
              "reg": "2886735079",
              "trusted-id": "",
              "imei": "868795049782259",
              "model": "V1813BA",
              "wlb-imei": "868795049782259",
              "client-id": "41115ae5c02d5198",
              "brand": "vivo",
              "application-id": "com.kmxs.reader",
              "AUTHORIZATION": "",
              "sign": "c56fdc79ba65fa59b87c3eac6a676190",
              "User-Agent": "webviewversion/30415",
              "Host": "api-ks.wtzw.com",
              "Connection": "Keep-Alive",
              "Accept-Encoding": "gzip",
              "If-Modified-Since": "Mon, 12 Aug 2019 05:32:06 GMT"}

    url = "https://api-ks.wtzw.com/api/v1/reader-adv"

    a = APIData().getdata(url,header)
    print(a)
