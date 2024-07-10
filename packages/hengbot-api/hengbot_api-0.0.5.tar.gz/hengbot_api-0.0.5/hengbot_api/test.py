import unittest
import sys
from hengbot_api import sparky
import time


def test_get_batteryPercentage():
    ip = sys.argv[1]
    with sparky.RobotControl(ip) as rc:
        a = time.time()
        while rc.batteryPercentage == '':
            if time.time() - a > 2:
                break
            pass
        print(rc.batteryPercentage)


if __name__ == '__main__':
    # print(sys.argv[1])
    testcase = unittest.FunctionTestCase(test_get_batteryPercentage)

    suite = unittest.TestSuite()
    suite.addTest(testcase)

    runner = unittest.TextTestRunner()
    runner.run(suite)
