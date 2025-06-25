import requests
from fanyi import translate_and_save
def get_chengjiu(API_KEY, APP_ID):
    """获取 Coromon 游戏的成就信息并保存到文件"""

    # API_KEY = ""  # 替换成你自己的 API Key
    # APP_ID  =   # Coromon

    url = (
        "https://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/"
        f"?key={API_KEY}&appid={APP_ID}&l=schinese"
    )

    data = requests.get(url, timeout=15).json()

    achievements = data["game"]["availableGameStats"]["achievements"]
    print(f"共 {len(achievements)} 个成就：\n")

    with open("./chengjiu.txt", "w", encoding="utf-8") as f:
        for a in achievements:
            name = a['displayName']
            desc = a.get('description', '无描述')
            line = f"{name}  |  {desc}\n"
            # print(line, end="")
            f.write(line)


    translate_and_save()
