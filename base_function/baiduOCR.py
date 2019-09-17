from aip import AipOcr
import json

class baiduApi:
    def __init__(self,APP_ID,API_KEY,SECRET_KEY):
        '''
        """ 你的 APPID AK SK """
        APP_ID = '你的 App ID'
        API_KEY = '你的 Api Key'
        SECRET_KEY = '你的 Secret Key'
        '''
        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


    """ 读取图片 """
    def get_file_content(self,imageFile):
        with open(imageFile, 'rb') as fp:
            return fp.read()



    def getWordFromImage(self,imageFile):
        options = {}
        options["recognize_granularity"] = "big"
        options["detect_direction"] = "false"
        options["vertexes_location"] = "true"
        options["probability"] = "false"
        # options["probability"] = "true"

        image = self.get_file_content(imageFile)
        result = self.client.accurate(image, options)
        return result

if __name__=="__main__":
    APP_ID='17235264'
    API_KEY='ejTp8Xd1ZTUGjnO1WkRoWFWE'
    SECRET_KEY='MPapr5pwGlYBu5GHZXjYxnGmOekDd2QB'
    obj = baiduApi(APP_ID,API_KEY,SECRET_KEY)
    imageFile=r'D:\browser_dwliuc\screenshot\111.png'
    result = obj.getWordFromImage(imageFile)
    for word in result['words_result']:
        print(word['words'])
    # print(result)
