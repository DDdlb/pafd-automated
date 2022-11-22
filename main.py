import json
import time
import os
from json import loads as json_loads
from os import path as os_path, getenv
from sys import exit as sys_exit
from getpass import getpass
import re
import base64
import easyocr
import io
import numpy
from PIL import Image
from PIL import ImageEnhance
info = '{"e":0,"m":"操作成功","d":{"info":{"whether_qk":"1","tw":"13","sfcxtz":"0","sfjcbh":"0","sfcxzysx":"0","qksm":"","sfyyjc":"0","jcjgqr":"0","remark":"","address":"上海市杨浦区新江湾城街道复旦大学江湾校区食堂","geo_api_info":"{\"type\":\"complete\",\"position\":{\"Q\":31.335800509983,\"R\":121.50389919704901,\"lng\":121.503899,\"lat\":31.335801},\"location_type\":\"html5\",\"message\":\"Get geolocation success.Convert Success.Get address success.\",\"accuracy\":29,\"isConverted\":true,\"status\":1,\"addressComponent\":{\"citycode\":\"021\",\"adcode\":\"310110\",\"businessAreas\":[{\"name\":\"江湾\",\"id\":\"310110\",\"location\":{\"Q\":31.310831,\"R\":121.49710900000002,\"lng\":121.497109,\"lat\":31.310831}},{\"name\":\"淞南\",\"id\":\"310113\",\"location\":{\"Q\":31.336023,\"R\":121.482393,\"lng\":121.482393,\"lat\":31.336023}}],\"neighborhoodType\":\"\",\"neighborhood\":\"\",\"building\":\"\",\"buildingType\":\"\",\"street\":\"淞沪路\",\"streetNumber\":\"2005号\",\"country\":\"中国\",\"province\":\"上海市\",\"city\":\"\",\"district\":\"杨浦区\",\"towncode\":\"310110020000\",\"township\":\"新江湾城街道\"},\"formattedAddress\":\"上海市杨浦区新江湾城街道复旦大学江湾校区食堂\",\"roads\":[],\"crosses\":[],\"pois\":[],\"info\":\"SUCCESS\"}","area":"","province":"","city":"","sfzx":"","sfjcwhry":"0","sfjchbry":"0","sfcyglq":"0","gllx":"","glksrq":"","jcbhlx":"","jcbhrq":"","bztcyy":"","sftjhb":"0","sftjwh":"0","gwszdd":"","sfpcgr":"0","jrszss":"","glfs":"","glgcdd":"","glqsrq":"","gljsrq":"","gzdd":"","sfwztl":"0","sftztl":"0","sffsksfl":"0","sfzgn":1,"sfjczgfxry":"0","sfcyglgcq":"0","xs_wcymjzdd":"0","xs_sfwcymjz_dd":"","fxyy":"","bztcyyqt":"","xs_dyzdd":"0","xs_dyzdd_text":"","xs_dezdd":"0","xs_dezdd_text":"","xs_sfdez":"0","xs_sfdsz":"0","xs_dszdd":"0","xs_dszdd_text":"","jzymmc":"","jzymifjzj":"0","uid":"542801","created":1669002823,"date":"20221121","xs_ymtype":"0","xs_sfwcymjz":"0","xs_sfdyz":"0","xs_sfwcjqz":"0","gov_zgfx":1,"ip":"[2001:da8:8001:864:b438:9548:fa09:eb28]","ipwllx":"","ipsfxyw":"0","jcqzrq":"","sfjcqz":"","jhfjrq":"","fhjtgj":"","fhjtgjbc":"","fkqssj":"","fklb":"","sjzxqsy":"","id":44570629,"sfyqjzgc":"","jrsfqzys":"","jrsfqzfy":"","jrdqtlqk":[],"jrdqjcqk":[],"sfyjfx":"0","sfjzxnss":"0","yjrxsj":"","rzqs":"","dsxm":"","wyyd":"0","bzxxzdz":"","xjrdxq":"","tjfs":"","fhjtgjzwh":""},"isConfirm":true,"oldInfo":{"whether_qk":"1","tw":"13","sfcxtz":"0","sfjcbh":"0","sfcxzysx":"0","qksm":"","sfyyjc":"0","jcjgqr":"0","remark":"","address":"上海市杨浦区新江湾城街道复旦大学江湾校区食堂","geo_api_info":"{\"type\":\"complete\",\"position\":{\"Q\":31.335800509983,\"R\":121.50389919704901,\"lng\":121.503899,\"lat\":31.335801},\"location_type\":\"html5\",\"message\":\"Get geolocation success.Convert Success.Get address success.\",\"accuracy\":29,\"isConverted\":true,\"status\":1,\"addressComponent\":{\"citycode\":\"021\",\"adcode\":\"310110\",\"businessAreas\":[{\"name\":\"江湾\",\"id\":\"310110\",\"location\":{\"Q\":31.310831,\"R\":121.49710900000002,\"lng\":121.497109,\"lat\":31.310831}},{\"name\":\"淞南\",\"id\":\"310113\",\"location\":{\"Q\":31.336023,\"R\":121.482393,\"lng\":121.482393,\"lat\":31.336023}}],\"neighborhoodType\":\"\",\"neighborhood\":\"\",\"building\":\"\",\"buildingType\":\"\",\"street\":\"淞沪路\",\"streetNumber\":\"2005号\",\"country\":\"中国\",\"province\":\"上海市\",\"city\":\"\",\"district\":\"杨浦区\",\"towncode\":\"310110020000\",\"township\":\"新江湾城街道\"},\"formattedAddress\":\"上海市杨浦区新江湾城街道复旦大学江湾校区食堂\",\"roads\":[],\"crosses\":[],\"pois\":[],\"info\":\"SUCCESS\"}","area":"上海市 杨浦区","province":"上海市","city":"上海市","sfzx":"0","sfjcwhry":"0","sfjchbry":"0","sfcyglq":"0","gllx":"","glksrq":"","jcbhlx":"","jcbhrq":"","ismoved":"0","bztcyy":"","sftjhb":"0","sftjwh":"0","gwszdd":"","sfpcgr":"0","jrszss":"","glfs":"","glgcdd":"","glqsrq":"","gljsrq":"","gzdd":"","sfwztl":"0","sftztl":"0","sffsksfl":"0","sfzgn":1,"sfjczgfxry":"0","sfcyglgcq":"0","xs_wcymjzdd":"0","xs_sfwcymjz_dd":"","fxyy":"","bztcyyqt":"","xs_dyzdd":"0","xs_dyzdd_text":"","xs_dezdd":"0","xs_dezdd_text":"","xs_sfdez":"0","xs_sfdsz":"0","xs_dszdd":"0","xs_dszdd_text":"","jzymmc":"","jzymifjzj":"0","uid":"542801","created":1669002823,"date":"20221121","xs_ymtype":"0","xs_sfwcymjz":"0","xs_sfdyz":"0","xs_sfwcjqz":"0","gov_zgfx":1,"ip":"[2001:da8:8001:864:b438:9548:fa09:eb28]","ipwllx":"","ipsfxyw":"0","jcqzrq":"","sfjcqz":"","jhfjrq":"","fhjtgj":"","fhjtgjbc":"","fkqssj":"","fklb":"","sjzxqsy":"","id":44570629},"hasFlag":false,"uinfo":{"uid":"542801","realname":"代刘博","sex":"未知","email":"","mobile":"","weixin":"","qq":"","csrq":"0","jg":"","mz":"","zjhlx":"1","zjh":"","hyzk":"","jkzk":"","gj":"","xx":"","whcd":"","zgxl":"","xyzj":"","zzmm":"","photo":"","avatar":"https://zlapp.fudan.edu.cn/backend/uc/img/headpic.png","active_role_id":"542731","is_del":"0","role":{"roleid":542731,"number":"21210240146","identity":"研究生","identity_id":43,"sfzx":1},"departs":{"1044":"计算机科学技术学院"},"age":0,"type":"real"},"isFirst":false,"setting":{"title":"平安复旦","desc":"温馨提示： 不外出、不聚集、不吃野味， 戴口罩、勤洗手、咳嗽有礼，开窗通风，发热就诊。
”基本信息“展示的数据为您初次填报平安复旦时的信息，您实时的状态信息可以在”每日更新“中维护完善。","area":"沪","sendmsg":"","img":"image/28/955456df76e0d2d8d36b7b0ddc0d8f3d.jpg","copyright":"","notifywid":"","sms":"0","mp":"0","city":"上海市","mpid":"","templateid":"","notice_num":"2"},"date":"2022-11-22","his":{"id":"66021","uid":"542801","bj":"","xb":"1","sjh":"17302208786","syd":"","sfzx":"0","sflgj":"0","ljrq":"","ljjtgj":"","ljhbcc":"","fjrq":"","fjjtgj":"","fjhbcc":"","sftjwh":"0","sftjhb":"0","qtljdd":"","fxrq":"20210804","fxjtgj":"其他","fxhbcc":"","fxsftjwh":"0","fxsftjhb":"0","jhfjrq":"20210829","jhfjjtgj":"飞机","jhfjhbcc":"","jhfjsftjwh":"0","jhfjsftjhb":"0","sfyljjh":"0","jhljrq":"","jhljjtgj":"","jhljhbcc":"","jhfjsj":"","sfgr":"0","sfjcgrz":"0","sffr":"0","jcjssfgr":"0","sfjchbqy":"0","created":"1629328378","jtzz":"上海市杨浦区国伟路300号爱久家园E栋","tjwhrq":"","tjhbrq":"","tjhbdq":"","fxtjwhrq":"","fxtjhbrq":"","fxtjhbdq":"","jhfjtjwhrq":"","jhfjtjhbrq":"","jhfjtjhbdq":"","jchbqyrq":"","sfjcwhqy":"","jcwhqyrq":"","jcgrzrq":"","created_uid":"3259","jtszd":"{\"myprovice\":\"\",\"mycity\":\"\",\"myarea\":\"\",\"xxdz\":\"\",\"sfgn\":\"\",\"gwdz\":\"\"}","dqszd":"1","dqszd_info":"{\"myprovice\":\"\",\"mycity\":\"\",\"myarea\":\"\",\"xxdz\":\"\",\"xq\":\"\",\"ss\":\"\",\"qs\":\"\",\"cw\":\"\",\"sfgn\":\"\",\"gwdz\":\"\"}","lhtlcs":"","dqjtxx":"","dqjtxx_info":"","dqjcxx":"","dqjcxx_info":"","jcgrhz":"0","jcyshz":"0","sfczfrqk":"0","sfczhxdgr":"0","sfysfy":"0","sfjjgl":"0","lhxc_ext":"[{\"ljrq\":\"\",\"ljjtgj\":\"\",\"ljhbcc\":\"\",\"fjrq\":\"\",\"fjjtgj\":\"\",\"fjhbcc\":\"\"}]","sfjctzqy":"","sfjcwzqy":"","jctzqyrq":"","jcwzqyrq":"","fxsftjtz":"","fxtjtzdq":"","fxtjtzrq":"","fxsftjwz":"","fxtjwzdq":"","fxtjwzrq":"","sftjtz":"0","tjtzdq":"","tjtzrq":"","sftjwz":"0","tjwzdq":"","tjwzrq":"","xsdl":"2","sfdrfdy":"","drfdyyx":"","yx":"计算机科学与技术学院","xslx":"全日制学历研究生大陆学生","rkjtkn":"0","sfbyb":"0","sfdzb":"0","dylx":"","fdyxm":"赵琼","sfjj":"0","jg":"","sfzjh":"","sfjczgfxqy":"0","sfjczgfxqyjcsj":"","fxsftjzgdx":"0","fxtjzgdxdq":"","fxtjzgdxrq":""},"env":"FUDAN-ZLAPP"}}'


from requests import session, post, adapters
adapters.DEFAULT_RETRIES = 5

class Fudan:
    """
    建立与复旦服务器的会话，执行登录/登出操作
    """
    UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0"

    # 初始化会话
    def __init__(self,
                 uid, psw,
                 url_login='https://uis.fudan.edu.cn/authserver/login',
                 url_code="https://zlapp.fudan.edu.cn/backend/default/code"):
        """
        初始化一个session，及登录信息
        :param uid: 学号
        :param psw: 密码
        :param url_login: 登录页，默认服务为空
        """
        self.session = session()
        self.session.keep_alive = True # 改为持久链接
        self.session.headers['User-Agent'] = self.UA
        self.url_login = url_login
        self.url_code = url_code

        self.uid = uid
        self.psw = psw

    def _page_init(self):
        """
        检查是否能打开登录页面
        :return: 登录页page source
        """
        print("◉Initiating——", end='')
        page_login = self.session.get(self.url_login)

        print("return status code",
              page_login.status_code)

        if page_login.status_code == 200:
            print("◉Initiated——", end="")
            return page_login.text
        else:
            print("◉Fail to open Login Page, Check your Internet connection\n")
            self.close()

    def login(self):
        """
        执行登录
        """
        page_login = self._page_init()

        print("getting tokens")
        data = {
            "username": self.uid,
            "password": self.psw,
            "service": "https://zlapp.fudan.edu.cn/site/ncov/fudanDaily"
        }

        # 获取登录页上的令牌
        result = re.findall(
            '<input type="hidden" name="([a-zA-Z0-9\-_]+)" value="([a-zA-Z0-9\-_]+)"/?>', page_login)
        # print(result)
        # result 是一个列表，列表中的每一项是包含 name 和 value 的 tuple，例如
        # [('lt', 'LT-6711210-Ia3WttcMvLBWNBygRNHdNzHzB49jlQ1602983174755-7xmC-cas'), ('dllt', 'userNamePasswordLogin'), ('execution', 'e1s1'), ('_eventId', 'submit'), ('rmShown', '1')]
        data.update(
            result
        )

        headers = {
            "Host": "uis.fudan.edu.cn",
            "Origin": "https://uis.fudan.edu.cn",
            "Referer": self.url_login,
            "User-Agent": self.UA
        }

        print("◉Login ing——", end="")
        post = self.session.post(
            self.url_login,
            data=data,
            headers=headers,
            allow_redirects=False)

        print("return status code", post.status_code)

        if post.status_code == 302:
            print("\n***********************"
                  "\n◉登录成功"
                  "\n***********************\n")
        else:
            print("◉登录失败，请检查账号信息")
            self.close()

    def logout(self):
        """
        执行登出
        """
        exit_url = 'https://uis.fudan.edu.cn/authserver/logout?service=/authserver/login'
        expire = self.session.get(exit_url).headers.get('Set-Cookie')
        # print(expire)

        if '01-Jan-1970' in expire:
            print("◉登出完毕")
        else:
            print("◉登出异常")

    def close(self, exit_code=0):
        """
        执行登出并关闭会话
        """
        self.logout()
        self.session.close()
        print("◉关闭会话")
        print("************************")
        sys_exit(exit_code)


class Zlapp(Fudan):
    last_info = ''

    def check(self):
        """
        检查
        """
        print("◉检测是否已提交")
#         get_info = self.session.get(
#             'https://zlapp.fudan.edu.cn/ncov/wap/fudan/get-info')
#         last_info = get_info.json()
        last_info = json.loads(info)

        print("◉上一次提交日期为:", last_info["d"]["info"]["date"])

        position = last_info["d"]["info"]['geo_api_info']
        position = json_loads(position)

        print("◉上一次提交地址为:", position['formattedAddress'])
        # print("◉上一次提交GPS为", position["position"])
        # print(last_info)
        
        # 改为上海时区
        os.environ['TZ'] = 'Asia/Shanghai'
        time.tzset()
        today = time.strftime("%Y%m%d", time.localtime())
        print("◉今日日期为:", today)
        if last_info["d"]["info"]["date"] == today:
            print("\n*******今日已提交*******")
            self.close()
        else:
            print("\n\n*******未提交*******")
            self.last_info = last_info["d"]["oldInfo"]
            
    def read_captcha(self, img_byte):
        img = Image.open(io.BytesIO(img_byte)).convert('L')
        enh_bri = ImageEnhance.Brightness(img)
        new_img = enh_bri.enhance(factor=1.5)
        
        image = numpy.array(new_img)
        reader = easyocr.Reader(['en'])
        horizontal_list, free_list = reader.detect(image, optimal_num_chars=4)
        character = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        allow_list = list(character)
        allow_list.extend(list(character.lower()))
    
        result = reader.recognize(image, 
                                allowlist=allow_list,
                                horizontal_list=horizontal_list[0],
                                free_list=free_list[0],
                                detail = 0)
        return result[0]
    

    def validate_code(self):
        img = self.session.get(self.url_code).content
        return self.read_captcha(img)

    def checkin(self):
        """
        提交
        """
        headers = {
            "Host": "zlapp.fudan.edu.cn",
            "Referer": "https://zlapp.fudan.edu.cn/site/ncov/fudanDaily?from=history",
            "DNT": "1",
            "TE": "Trailers",
            "User-Agent": self.UA
        }

        print("\n\n◉◉提交中")

        geo_api_info = json_loads(self.last_info["geo_api_info"])
        province = self.last_info["province"]
        city = self.last_info["city"]
        district = geo_api_info["addressComponent"].get("district", "")
        
        while(True):
            print("◉正在识别验证码......")
            code = self.validate_code()
            print("◉验证码为:", code)
            if(city=="上海市"):
                area = " ".join((city, district))
            else:
                area = " ".join((province, city, district))
            self.last_info.update(
                {
                    "tw": "13",
                    "province": province,
                    "city": city,
                    "area": area,
                    #"sfzx": "1",  # 是否在校
                    #"fxyy": "",  # 返校原因
                    "code": code,
                }
            )
            # print(self.last_info)
            save = self.session.post(
                'https://zlapp.fudan.edu.cn/ncov/wap/fudan/save',
                data=self.last_info,
                headers=headers,
                allow_redirects=False)

            save_msg = json_loads(save.text)["m"]
            print(save_msg, '\n\n')
            time.sleep(0.1)
            if(json_loads(save.text)["e"] != 1):
                break

def get_account():
    """
    获取账号信息
    """
    uid = getenv("STD_ID")
    psw = getenv("PASSWORD")
    if uid != None and psw != None:
        print("从环境变量中获取了用户名和密码！")
        return uid, psw
    print("\n\n请仔细阅读以下日志！！\n请仔细阅读以下日志！！！！\n请仔细阅读以下日志！！！！！！\n\n")
    if os_path.exists("account.txt"):
        print("读取账号中……")
        with open("account.txt", "r") as old:
            raw = old.readlines()
        if (raw[0][:3] != "uid") or (len(raw[0]) < 10):
            print("account.txt 内容无效, 请手动修改内容")
            sys_exit()
        uid = (raw[0].split(":"))[1].strip()
        psw = (raw[1].split(":"))[1].strip()

    else:
        print("未找到account.txt, 判断为首次运行, 请接下来依次输入学号密码")
        uid = input("学号：")
        psw = getpass("密码：")
        with open("account.txt", "w") as new:
            tmp = "uid:" + uid + "\npsw:" + psw +\
                "\n\n\n以上两行冒号后分别写上学号密码，不要加空格/换行，谢谢\n\n请注意文件安全，不要放在明显位置\n\n可以从dailyFudan.exe创建快捷方式到桌面"
            new.write(tmp)
        print("账号已保存在目录下account.txt，请注意文件安全，不要放在明显位置\n\n建议拉个快捷方式到桌面")

    return uid, psw


if __name__ == '__main__':
    uid, psw = get_account()
    # print(uid, psw)
    zlapp_login = 'https://uis.fudan.edu.cn/authserver/login?' \
                  'service=https://zlapp.fudan.edu.cn/site/ncov/fudanDaily'
    code_url = "https://zlapp.fudan.edu.cn/backend/default/code"
    daily_fudan = Zlapp(uid, psw,
                        url_login=zlapp_login, url_code=code_url)
    daily_fudan.login()

    daily_fudan.check()
    daily_fudan.checkin()
    # 再检查一遍
    daily_fudan.check()
    daily_fudan.close(1)
