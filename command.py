"""
1、D:\Python38\python.exe run_page/keep_sync.py 139297
D:\Python38\python.exe run_page/keep_sync.py 13046 57596 --with-gpx

2、D:\Python38\python.exe run_page/gen_svg.py --from-db --title "Dice" --type github --athlete "Dice" --special-distance 10 --special-distance2 20 --special-color yellow --special-color2 red --output assets/github.svg --use-localtime --min-distance 0.5

3、D:\Python38\python.exe run_page/gen_svg.py --from-db --title "Dice" --type grid --athlete "Dice"  --output assets/grid.svg --min-distance 1.0 --special-color yellow --special-color2 red --special-distance 20 --special-distance2 40 --use-localtime

4、D:\Python38\python.exe run_page/gen_svg.py --from-db --type circular --use-localtime

5、D:\Desktop\runningPage\running_page>pnpm install
6、D:\Desktop\runningPage\running_page>pnpm develop
# 缓存数据在 running_page/assets文件夹下，删除年份数据；删除data.db数据文件。
访问本地浏览器即可

修改keep_sync里三处跑步单词为骑行单词即可导出骑行数据
RUN_DATA_API = "https://api.gotokeep.com/pd/v3/stats/detail?dateUnit=all&type=running&lastDate={last_date}"
替换为：
RUN_DATA_API = "https://api.gotokeep.com/pd/v3/stats/detail?dateUnit=all&type=cycling&lastDate={last_date}"

RUN_LOG_API = "https://api.gotokeep.com/pd/v3/runninglog/{run_id}"
替换为：
RUN_LOG_API = "https://api.gotokeep.com/pd/v3/cyclinglog/{run_id}"

 and run_data["dataType"] == "outdoorRunning"
 替换为：
 and run_data["dataType"] == "outdoorCycling"
"""
