from datetime import datetime
import sqlite3, json



def check_result(cdl , op , candle):
    if op == 101:
        if cdl < candle:
            return True
        else:
            return False
    elif op == 99:
        if cdl > candle:
            return True
        else:
            return False
    else:
        return "No Value"


def chek(candle, list):
    if len(candle) > len(list) and len(candle) > 4:
        for data in list:
            result = check_result(candle[data[0]][data[1]], data[2], candle[data[3]][data[4]])
            if not result:
                return False
        return True
    else:
        return False

def back(list, stoploss, profitbook):
    connc = sqlite3.connect('fiveMinCandle.db') 
    cursor = connc.cursor()
    cursor.execute('SELECT * FROM candles')
    rows = cursor.fetchall()
    result_list = []
    for row in rows:
        id, date, candle = row
        data_list = []
        data = json.loads(candle)
        entry = ""
        for candle in data:
            dt = datetime.fromisoformat(candle[0])
            time = dt.strftime("%H:%M")
            data_list.append(candle)
            if entry == "":
                result = chek(data_list, list)
                if result: 
                    entry = candle[4]
                    entry_time = time
                else:
                    continue
            else:
                if candle[4] >  entry + profitbook:
                    result_list.append(f"Date  : {date} - Entry {entry_time} : Price {entry} -  Exit {time}: Price {candle[4]} - Book Profit {candle[4] - entry}")
                    entry = ""
                elif candle[4] <  entry - stoploss:
                    result_list.append(f"Date  : {date} - Entry {entry_time} : Price {entry} -  Exit {time}: Price {candle[4]}  - Book Loss {candle[4] - entry}")
                    entry = ""
                elif len(data_list) > 71:
                    result_list.append(f"Date  : {date} - Entry {entry_time} : Price {entry} -  Exit {time}: Price {candle[4]} - Market Close {candle[4] - entry}")
                    entry = ""
                else:
                    continue
    return result_list
