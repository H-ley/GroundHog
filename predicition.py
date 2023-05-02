#! /usr/bin/python3
from math import sqrt

tendency_switch = 0

def compute_relative_evo(period = 0, input_list = []):
    if (len(input_list) > period):
        try:
            value = round((input_list[-1] / input_list[-(1 + period)] - 1) * 100)
            return '{}'.format(value)
        except (ValueError, FloatingPointError, ZeroDivisionError):
            return "nan"
    return "nan"

def compute_std_deviation(period = 0, input_list = []):
    if (len(input_list) >= period):
        try:
            avg = sum(input_list[-period:]) / period
            std_dev = sqrt(sum(map(lambda x:(x - avg)**2, input_list[-period:])) / period)
            return '{:.2f}'.format(std_dev)
        except (ValueError, FloatingPointError, ZeroDivisionError):
            return "nan"
    return "nan"

def compute_std_deviation_n(period = 0, input_list = []):
    if (len(input_list) >= period):
        try:
            avg = sum(input_list[-period:]) / period
            std_dev = sqrt(sum(map(lambda x:(x - avg)**2, input_list[-period:])) / period)
            return '{:.2f}'.format(std_dev)
        except (ValueError, FloatingPointError, ZeroDivisionError):
            return None
    return None

def compute_mobile_avg(period = 0, input_list = []):
    if (len(input_list) >= period):
        try:
            avg = sum(input_list[-period:]) / period
            std_dev = sum(input_list[-period:]) / period
            return std_dev
        except (ValueError, FloatingPointError, ZeroDivisionError):
            return None
    return None

def compute_increase_avg(period = 0, input_list = []):
    if (len(input_list) > period):
        try:
            avg_inc = sum(list(map(lambda x, y: max(0, x - y), input_list[-period:], input_list[-(period + 1):-1]))) / period
            return '{:.2f}'.format(avg_inc)
        except (ValueError, FloatingPointError, ZeroDivisionError):
            return "nan"
    return "nan"

def compute_switch_status(period, input_list):
    global tendency_switch
    if (len(input_list) > period + 1):
        try:
            value = round((input_list[-1] / input_list[-(1 + period)] - 1) * 100)
            prevalue = round((input_list[-2] / input_list[-(2 + period)] - 1) * 100)
            if (abs(prevalue + value) != abs(prevalue) + abs(value)):
                tendency_switch += 1
                return "    a switch occurs"
        except (ValueError, FloatingPointError, ZeroDivisionError):
            return ""
    return ""


def display_final(pos_list, in_list, period):
    if (len(in_list) < period):
        exit(84)
    global tendency_switch
    print("Global tendency switched {} times".format(tendency_switch))
    pos_list = list(map(lambda x : abs(x - .5), pos_list))
    oth_list = sorted(pos_list)
    fin_list = oth_list[-5:]
    fin_list = list(map(lambda x : in_list[pos_list.index(x) + period - 1], fin_list))
    print("5 weirdest values are {}".format(fin_list[::-1]))

def display_results(period, input_value, input_list):
    print("g={}    r={}%    s={}{}".format(
    compute_increase_avg(period, input_list),
    compute_relative_evo(period, input_list),
    compute_std_deviation(period, input_list),
    compute_switch_status(period, input_list)))

def groundhog(period):
    input_value = input()
    input_list = []
    std_dev_list = []
    mobile_avg_list = []
    pos_list = []
    trend_switch_nb = 0
    while (input_value != "STOP"):
        try:
            input_list.append(float(input_value))
            display_results(period, input_value, input_list)
            std_dev_list.append(compute_std_deviation_n(period, input_list))
            mobile_avg_list.append(compute_mobile_avg(period, input_list))
            std_dev_list = list(filter(None, std_dev_list))
            try:
                bande_basse = mobile_avg_list[-1] - 2 * float(std_dev_list[-1])
                bande_haute = mobile_avg_list[-1] + 2 * float(std_dev_list[-1])
                pos_list.append((input_list[-1] - bande_basse) / (bande_haute - bande_basse))
            except (IndexError, ZeroDivisionError):
                pass
        except ValueError:
            continue
        input_value = input()
        try:
            float(input_value)
        except ValueError:
            if (input_value != "STOP"):
                exit(84)
    display_final(pos_list, input_list, period)
