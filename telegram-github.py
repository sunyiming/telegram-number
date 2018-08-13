import requests
import csv
import json
import time
#字典嵌套处理
def get_target_value(key, dic, tmp_list):
    """
    :param key: 目标key值
    :param dic: JSON数据
    :param tmp_list: 用于存储获取的数据
    :return: list
    """
    if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
        return 'argv[1] not an dict or argv[-1] not an list '
 
    if key in dic.keys():
        tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list
    else:
        for value in dic.values():  # 传入数据不符合则对其value值进行遍历
            if isinstance(value, dict):
                get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
            elif isinstance(value, (list, tuple)):
                _get_value(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用_get_value
    return tmp_list
def _get_value(key, val, tmp_list):

    for val_ in val:
        if isinstance(val_, dict):  
            get_target_value(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
        elif isinstance(val_, (list, tuple)):
            _get_value(key, val_, tmp_list)   # 传入数据的value值是列表或者元组，则调用自身
#数据处理
def data_process(chat_id,r_name,r):
    jsons = json.dumps(r)
    dicts = json.loads(jsons)
    print (dicts["result"])
    result = str(dicts["result"])
    
    jsons_name = json.dumps(r_name)
    dicts_name = json.loads(jsons_name)
    #print (get_target_value('title',dicts_name,[])[0])
    result_name = get_target_value('title',dicts_name,[])[0].encode('gb2312','ignore').decode('gbk')
    
    final_result = [chat_id,result_name,result]
    return final_result
#数据写入
def csv_write(final_result):
    csvFile = open("data_output.csv", "a")
    writer = csv.writer(csvFile)
    writer.writerow(final_result)
    csvFile.close()
#主程序
chat_list = ["Sample_1","Sample_2"]
localtime = [time.asctime( time.localtime(time.time()) )]
csvFile = open("data_output.csv", "a")
writer = csv.writer(csvFile)
writer.writerow(localtime)
csvFile.close()
for chat_id in chat_list:
    api = 'https://api.telegram.org/<Your Bot Token>/getChatMembersCount?chat_id=@'+chat_id
    api_name = 'https://api.telegram.org/<Your Bot Token>/getChat?chat_id=@'+chat_id
    r = requests.get(api).json()
    r_name = requests.get(api_name).json()
    print(data_process(chat_id,r_name,r))
    csv_write(data_process(chat_id,r_name,r))