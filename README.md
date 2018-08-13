# telegram-number
Get Telegram Channel/Group members count and save it to csv.
## Dependence
```
pip install requests
```
## Changes
### In line 60 and 61:
```
api = 'https://api.telegram.org/<Your Bot Token>/getChatMembersCount?chat_id=@'+chat_id
api_name = 'https://api.telegram.org/<Your Bot Token>/getChat?chat_id=@'+chat_id
```
Change "&lt;Your Bot Token&gt;" to your own bot token.

### In line 55:
```
csvFile = open("data_output.csv", "a")
```
data_output.csv is output file

### In line 53:
```
chat_list = ["Sample_1","Sample_2"]
```
Replace Sample_1 Sample_2 with a real chat id
