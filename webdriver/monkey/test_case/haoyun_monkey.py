from foryou_app.monkey.common.common import DriverThread


def haoyun_monkey():
    driver_1 = DriverThread(1, "Thread-1",
                            '/Users/wenxueyang/PycharmProjects/fuyoukache/monkey/data/haoyun4.3.0.apk',
                            'com.foryou.haoyun', '.entry.EntryActivity', '4723', 1, '11801380001')
    # driver_2 = DriverThread(2, "Thread-2",
    #                         '/Users/wenxueyang/PycharmProjects/fuyoukache/monkey/data/haoyun4.3.0.apk',
    #                         'com.foryou.haoyun', '.entry.EntryActivity', '4724', 2, '11811380001')
    driver_1.start()
    # driver_2.start()
    driver_1.join()
    # driver_2.join()


haoyun_monkey()
