import urequests as r
def realtime():
    url = 'http://worldtimeapi.org/api/timezone/Asia/Shanghai'
    resp = r.get(url)
    info = resp.json()['datetime']
    resp.close()
    return {'datetime':info,
            'year':info[0:4],
            'month':info[5:7],
            'day':info[8:10],
            'date':info[0:10],
             'hour':info[11:13],
             'min':info[14:16],
             'sec':info[17:19],
             }