#!/usr/bin/env python
# coding=utf-8

# -*- coding: utf-8 -*-
import json
import time
import unittest
import HTMLTestRunner
from datetime import datetime
from time import sleep


def cron_time(key):
    tim = datetime.now()
    print "[%s][check][%s] field started\n" % (tim, key)
    sleep(1)


def check_over(key):
    tim = datetime.now()
    print "[%s][check][%s] field finished\n" % (tim, key)


def format_result(api_type, result):
    if result['status'] == 0:
        print "********************* Result ******************************\n"
        print "%s compare result is PASS.\n" % (api_type)
        print "***********************************************************\n"
    else:
        print "********************* Result ******************************\n"
        print "%s compare result is FAIL.\n" % (api_type)
        print "-----------------------------------------------------------\n"
        print "Details info as below:\n"
        for k, v in result['errors'].iteritems():
            print "[%s] field : %s\n" % (k, v)
        print "***********************************************************\n"


# expect_json  对应表格内的实际值，actual_json  对应表格内的期待值
def cam_compare_json(expect_json, actual_json, campaign_id):
    print "Campaign API start to compare......\n"
    print "--------------------------------------------------\n"
    err = {}
    if isinstance(expect_json, str) and isinstance(actual_json, str):
        expect_json = json.loads(expect_json, encoding='utf-8')
        actual_json = json.loads(actual_json, encoding='utf-8')
        actual_json = actual_json["response"][campaign_id]
        try:
            for k, v in actual_json.iteritems():
                if k == "code":
                    if v != 0:
                        err[k] = "code is not 0"
                elif k == "msg":
                    if v != "success":
                        err[k] = "msg is not success"
                else:
                    for k1, v1 in v.iteritems():
                        if k1 == "advertiser_id":
                            cron_time(k1)
                            E_advertiser_id = expect_json[k1]
                            A_advertiser_id = v1
                            if E_advertiser_id != A_advertiser_id:
                                err[k1] = "%s expect %s,actual %s!" % (k1, E_advertiser_id, A_advertiser_id)
                            check_over(k1)
                        elif k1 == "advertiser_name":
                            cron_time(k1)
                            E_advertiser_name = expect_json[k1]
                            A_advertiser_name = v1
                            if E_advertiser_name != A_advertiser_name:
                                err[k1] = "%s expect %s,actual %s!" % (
                                    k1, E_advertiser_name, A_advertiser_name)
                            check_over(k1)
                        # elif k1 == "budget":
                        #     cron_time(k1)
                        #     for k2, v2 in expect_json[k1].iteritems():
                        #         E_budget = expect_json[k1][k2]
                        #         try:
                        #             A_budget = v1[k2]
                        #         except Exception as e:
                        #             exc = "Exception_[%s][%s]" % (k1, k2)
                        #             err[exc] = str(e) + " not in api_json!"
                        #             continue
                        #         if E_budget != A_budget:
                        #             b_k1 = "[%s][%s]" % (k1, k2)
                        #             err[b_k1] = "budget expect %s,actual %s!" % (E_budget, A_budget)
                        #     check_over(k1)
                        # elif k1 == "campaign_id":
                        #     cron_time(k1)
                        #     E_campaign_id = expect_json[k1]
                        #     A_campaign_id = v1
                        #     if E_campaign_id != A_campaign_id:
                        #         err[k1] = "%s expect %s,actual %s!" % (k1, E_campaign_id, A_campaign_id)
                        elif k1 == "campaign_name":
                            cron_time(k1)
                            E_campaign_name = expect_json[k1]
                            A_campaign_name = v1
                            if E_campaign_name != A_campaign_name:
                                err[k1] = "%s expect %s,actual %s!" % (k1, E_campaign_name, A_campaign_name)
                            check_over(k1)
                        elif k1 == "click_limit":
                            cron_time(k1)
                            E_click_limit = expect_json[k1]
                            A_click_limit = v1
                            if E_click_limit != A_click_limit:
                                err[k1] = "%s expect %s,actual %s!" % (k1, E_click_limit, A_click_limit)
                            check_over(k1)
                        # elif k1 == "delivery_speed":
                        #     cron_time(k1)
                        #     E_delivery_speed = expect_json[k1]
                        #     A_delivery_speed = v1
                        #     if E_delivery_speed != A_delivery_speed:
                        #         err[k1] = "%s expect %s,actual %s!" % (k1, E_delivery_speed, A_delivery_speed)
                        #     check_over(k1)
                        # elif k1 == "delivery_time":  # 需要确定投放周期是几个
                        #     cron_time(k1)
                        #     E_delivery_time = expect_json[k1]
                        #     if len(E_delivery_time) == len(v1):
                        #         for i in range(len(E_delivery_time)):
                        #             E_delivery_time_start = E_delivery_time[i]["start"]
                        #             E_delivery_time_end = E_delivery_time[i]["end"]
                        #             A_delivery_time_start = v1[i]["start"]
                        #             A_delivery_time_end = v1[i]["end"]
                        #             if E_delivery_time_start != A_delivery_time_start:
                        #                 dt = "[%s][%s][start]" % (k1, i)
                        #                 err[dt] = "start expect %s,actual %s!" % (
                        #                     E_delivery_time_start, A_delivery_time_start)
                        #             if E_delivery_time_end != A_delivery_time_end:
                        #                 dt = "[%s][%s][end]" % (k1, i)
                        #                 err[dt] = "end expect %s,actual %s!" % (
                        #                     E_delivery_time_end, A_delivery_time_end)
                        #     else:
                        #         err["Exception_delivery_time"] = "delivery_time expect %s, actual %s!" % (
                        #             E_delivery_time, v1)
                        #     check_over(k1)
                        elif k1 == "frequency_control":
                            cron_time(k1)
                            E_fre_con = expect_json[k1]
                            if len(E_fre_con) == len(v1):
                                for i in range(len(E_fre_con)):
                                    E_frequency_control_ftype = E_fre_con[i]["ftype"]
                                    E_frequency_control_period = E_fre_con[i]["period"]
                                    E_frequency_control_periodNum = E_fre_con[i]["periodNum"]
                                    E_frequency_control_times = E_fre_con[i]["times"]

                                    A_frequency_control_ftype = v1[i]["ftype"]
                                    A_frequency_control_period = v1[i]["period"]
                                    A_frequency_control_periodNum = v1[i]["periodNum"]
                                    A_frequency_control_times = v1[i]["times"]
                                    if E_frequency_control_ftype != A_frequency_control_ftype:
                                        fc = "[%s][%s][ftype]" % (k1, i)
                                        err[fc] = "ftype  expect %s,actual %s!" % (
                                            E_frequency_control_ftype, A_frequency_control_ftype)
                                    if E_frequency_control_period != A_frequency_control_period:
                                        fc = "[%s][%s][period]" % (k1, i)
                                        err[fc] = "period  expect %s,actual %s!" % (
                                            E_frequency_control_period, A_frequency_control_period)
                                    if E_frequency_control_periodNum != A_frequency_control_periodNum:
                                        fc = "[%s][%s][periodNum]" % (k1, i)
                                        err[fc] = "periodNum  expect %s,actual %s!" % (
                                            E_frequency_control_periodNum, A_frequency_control_periodNum)
                                    if E_frequency_control_times != A_frequency_control_times:
                                        fc = "[%s][%s][times]" % (k1, i)
                                        err[fc] = "times  expect %s,actual %s!" % (
                                            E_frequency_control_times, A_frequency_control_times)
                            else:
                                err["Exception_frequency_control"] = "frequency_control expect %s, actual %s!" % (
                                    E_fre_con, v1)
                            check_over(k1)
                        elif k1 == "impression_limit":
                            cron_time(k1)
                            E_impression_limit = expect_json[k1]
                            A_impression_limit = v1
                            if E_impression_limit != A_impression_limit:
                                err[k1] = "%s expect %s,actual %s!" % (
                                    k1, E_impression_limit, A_impression_limit)
                            check_over(k1)
                        elif k1 == "linear":
                            cron_time(k1)
                            E_linear = expect_json[k1]
                            A_linear = v1
                            if E_linear != A_linear:
                                err[k1] = "%s expect %s,actual %s!" % (k1, E_linear, A_linear)
                            check_over(k1)
                        elif k1 == "session_control":
                            cron_time(k1)
                            E_ses_con = expect_json[k1]
                            for sc in E_ses_con:
                                if not sc in v1:
                                    sc_k1 = "[%s][%s]" % (k1, sc)
                                    err[sc_k1] = "%s in expect %s ,not in actual %s!" % (sc)
                            check_over(k1)
                        elif k1 == "status":
                            cron_time(k1)
                            E_status = expect_json[k1]
                            A_status = v1
                            if E_status != A_status:
                                err[k1] = "%s expect %s,actual %s" % (k1, E_status, A_status)
                            check_over(k1)
                        elif k1 == "time_part":
                            cron_time(k1)
                            E_time_part = expect_json[k1]
                            for tp in E_time_part:
                                if not tp in v1:
                                    tp_k1 = "[%s][%s]" % (k1, tp)
                                    err[tp_k1] = "%s in expect %s ,not in actual %s!" % (tp, E_time_part, v1)
                            check_over(k1)
                        else:
                            continue
        except Exception as e:
            err["campare_err"] = str(e)
    else:
        err["Exception_json_type"] = "json type is not string."
    if err:
        resp = {"status": 1, "result": "fail", "errors": err}
        api_type = "Campaign_id: %s" % (campaign_id)
        format_result(api_type, resp)
        result = {"status": 1}
    else:
        resp = {"status": 0, "result": "pass", "errors": ""}
        api_type = "campaign_id: %s" % (campaign_id)
        format_result(api_type, resp)
        result = {"status": 0}
    print "Campaign API compared finish.\n"
    return result


# expect_json  对应表格内的实际值，actual_json  对应表格内的期待值
def adg_compare_json(expect_json, actual_json, adgroup_id):
    print "Adgroup API start to compare......\n"
    print "--------------------------------------------------\n"
    err = {}
    if isinstance(expect_json, str) and isinstance(actual_json, str):
        expect_json = json.loads(expect_json, encoding='utf-8')
        actual_json = json.loads(actual_json, encoding='utf-8')
        actual_json = actual_json["response"][adgroup_id]
        try:
            for k, v in actual_json.iteritems():
                if k == "code":
                    if v != 0:
                        err[k] = "code is not 0"
                elif k == "msg":
                    if v != "success":
                        err[k] = "msg is not success"
                else:
                    for k1, v1 in v.iteritems():
                        # if k1 == "ad_id":
                        #     cron_time(k1)
                        #     E_ad_id = expect_json[k1]
                        #     for ad in E_ad_id:
                        #         if not ad in v1:
                        #             a_k1 = "[%s][%s]" % (k1, ad)
                        #             err[a_k1] = "%s in expect %s, not in actual %s!" % (ad, E_ad_id, v1)
                        #     check_over(k1)
                        # elif k1 == "adgroup_id":
                        #     cron_time(k1)
                        #     E_adgroup_id = expect_json[k1]
                        #     A_adgroup_id = v1
                        #     if E_adgroup_id != A_adgroup_id:
                        #         err[k1] = "%s expect %s,actual %s!" % (k1, E_adgroup_id, A_adgroup_id)
                        #     check_over(k1)
                        if k1 == "adgroup_name":
                            cron_time(k1)
                            E_adgroup_name = expect_json[k1]
                            A_adgroup_name = v1
                            if E_adgroup_name != A_adgroup_name:
                                err[k1] = "%s expect %s,actual %s!" % (k1, E_adgroup_name, A_adgroup_name)
                            check_over(k1)
                        elif k1 == "advertiser_id":
                            cron_time(k1)
                            E_advertiser_id = expect_json[k1]
                            A_advertiser_id = v1
                            if E_advertiser_id != A_advertiser_id:
                                err[k1] = "%s expect %s,actual %s!" % (k1, E_advertiser_id, A_advertiser_id)
                            check_over(k1)
                        # elif k1 == "campaign_id":
                        #     cron_time(k1)
                        #     E_campaign_id = expect_json[k1]
                        #     A_campaign_id = v1
                        #     if E_campaign_id != A_campaign_id:
                        #         err[k1] = "%s expect %s,actual %s!" % (k1, E_campaign_id, A_campaign_id)
                        #     check_over(k1)
                        elif k1 == "click_url_prefix":
                            cron_time(k1)
                            E_click_url_prefix = expect_json[k1]
                            A_click_url_prefix = v1
                            if E_click_url_prefix != A_click_url_prefix:
                                err[k1] = "%s expect %s,actual %s!" % (k1, E_click_url_prefix, A_click_url_prefix)
                            check_over(k1)
                        elif k1 == "click_url_suffix":
                            cron_time(k1)
                            E_click_url_suffix = expect_json[k1]
                            A_click_url_suffix = v1
                            if E_click_url_suffix != A_click_url_suffix:
                                err[k1] = "%s expect %s,actual %s!" % (k1, E_click_url_suffix, A_click_url_suffix)
                            check_over(k1)
                        elif k1 == "deeplink_direct":
                            cron_time(k1)
                            E_deeplink_direct = expect_json[k1]
                            A_deeplink_direct = v1
                            if E_deeplink_direct != A_deeplink_direct:
                                err[k1] = "%s expect %s,actual %s!" % (k1, E_deeplink_direct, A_deeplink_direct)
                            check_over(k1)
                        elif k1 == "media_level":
                            cron_time(k1)
                            E_media_level = expect_json[k1]
                            A_media_level = v1
                            if E_media_level != A_media_level:
                                err[k1] = "%s expect %s,actual %s!" % (k1, E_media_level, A_media_level)
                            check_over(k1)
                        elif k1 == "pmp_guard":
                            cron_time(k1)
                            E_pmp_guard = expect_json[k1]
                            A_pmp_guard = v1
                            if E_pmp_guard != A_pmp_guard:
                                err[k1] = "%s expect %s,actual %s!" % (k1, E_pmp_guard, A_pmp_guard)
                            check_over(k1)
                        # elif k1 == "price":
                        #     cron_time(k1)
                        #     for k2, v2 in expect_json[k1].iteritems():
                        #         for k3, v3 in v2.iteritems():
                        #             E_price = expect_json[k1][k2][k3]
                        #             try:
                        #                 A_price = v1[k2][k3]
                        #             except Exception as e:
                        #                 exc = "Exception_[%s][%s][%s]" % (k1, k2, k3)
                        #                 err[exc] = str(e) + " not in api_json %s!" % (v1)
                        #                 continue
                        #             if E_price != A_price:
                        #                 b_k1 = "[%s][%s][%s]" % (k1, k2, k3)
                        #                 err[b_k1] = "[%s][%s][%s] expect %s,actual %s!" % (
                        #                     k1, k2, k3, E_price, A_price)
                        #     check_over(k1)
                        # elif k1 == "publisher_category":
                        #     cron_time(k1)
                        #     for k2, v2 in expect_json[k1].iteritems():
                        #         E_pub = expect_json[k1][k2]
                        #         try:
                        #             A_pub = v1[k2]
                        #         except Exception as e:
                        #             exc = "Exception_[%s][%s]" % (k1, k2)
                        #             err[exc] = str(e) + " not in api_json %s!" % (v1)
                        #             continue
                        #         for pb in E_pub:
                        #             if not pb in A_pub:
                        #                 p_k1 = "[%s][%s][%s]" % (k1, k2, pb)
                        #                 err[p_k1] = "%s in expect %s ,not in actual %s!" % (pb, E_pub, A_pub)
                        #     check_over(k1)
                        # elif k1 == "pv_type":
                        #     cron_time(k1)
                        #     for k2, v2 in expect_json[k1].iteritems():
                        #         E_pv = expect_json[k1][k2]
                        #         try:
                        #             A_pv = v1[k2]
                        #         except Exception as e:
                        #             exc = "Exception_[%s][%s]" % (k1, k2)
                        #             err[exc] = str(e) + " not in api_json %s!" % (v1)
                        #             continue
                        #         if E_pv != A_pv:
                        #             pv_k1 = "[%s][%s]" % (k1, k2)
                        #             err[pv_k1] = "pv_type expect %s,actual %s!" % (E_pv, A_pv)
                        #     check_over(k1)
                        elif k1 == "status":
                            cron_time(k1)
                            E_status = expect_json[k1]
                            A_status = v1
                            if E_status != A_status:
                                err[k1] = "%s expect %s,actual %s" % (k1, E_status, A_status)
                            check_over(k1)
                        # elif k1 == "target":
                        #     cron_time(k1)
                        #     for k2, v2 in expect_json[k1].iteritems():
                        #         for k3, v3 in v2.iteritems():
                        #             for k4, v4 in v3.iteritems():
                        #                 E_target = expect_json[k1][k2][k3][k4]
                        #                 try:
                        #                     A_target = v1[k2][k3][k4]
                        #                 except Exception as e:
                        #                     exc = "Exception_[%s][%s][%s][%s]" % (k1, k2, k3, k4)
                        #                     err[exc] = str(e) + " not in api_json %s!" % (v1)
                        #                     continue
                        #                 for tg in E_target:
                        #                     if not tg in A_target:
                        #                         p_k1 = "[%s][%s][%s][%s][%s]" % (k1, k2, k3, k4, tg)
                        #                         err[p_k1] = "[%s] expect %s ,actual %s!" % (
                        #                             tg, E_target, A_target)
                        #     check_over(k1)
                        else:
                            continue
        except Exception as e:
            err["campare_err"] = str(e)
    else:
        err["Exception_json_type"] = "json type is not string."
    if err:
        resp = {"status": 1, "result": "fail", "errors": err}
        api_type = "adgroup_id: %s" % (adgroup_id)
        format_result(api_type, resp)
        result = {"status": 1}
    else:
        resp = {"status": 0, "result": "pass", "errors": ""}
        api_type = "Adgroup_id: %s" % (adgroup_id)
        format_result(api_type, resp)
        result = {"status": 0}
    print "Adgroup API compared finish.\n"
    return result


# expect_json  对应表格内的实际值，actual_json  对应表格内的期待值
def ad_compare_json(expect_json, actual_json, ad_id):
    print "AD API start to compare......\n"
    print "--------------------------------------------------\n"
    err = {}
    if isinstance(expect_json, str) and isinstance(actual_json, str):
        expect_json = json.loads(expect_json, encoding='utf-8')
        actual_json = json.loads(actual_json, encoding='utf-8')
        actual_json = actual_json["response"][ad_id]
        try:
            for k, v in actual_json.iteritems():
                if k == "code":
                    if v != 0:
                        err[k] = "code is not 0"
                elif k == "msg":
                    if v != "success":
                        err[k] = "msg is not success"
                else:
                    for k1, v1 in v.iteritems():
                        # if k1 == "ad_id":
                        #     cron_time(k1)
                        #     E_ad_id = expect_json[k1]
                        #     A_ad_id = v1
                        #     if E_ad_id != A_ad_id:
                        #         err[k1] = "%s expect %s,actual %s!" % (k1, E_ad_id, A_ad_id)
                        # if k1 == "ad_name":
                        #     cron_time(k1)
                        #     E_ad_name = expect_json[k1]
                        #     A_ad_name = v1
                        #     if E_ad_name != A_ad_name:
                        #         err[k1] = "%s expect %s,actual %s!" % (k1, E_ad_name, A_ad_name)
                        #     check_over(k1)
                        # elif k1 == "adgroup_id":
                        #     cron_time(k1)
                        #     E_adgroup_id = expect_json[k1]
                        #     A_adgroup_id = v1
                        #     if E_adgroup_id != A_adgroup_id:
                        #         err[k1] = "%s expect %s,actual %s!" % (k1, E_adgroup_id, A_adgroup_id)
                        # elif k1 == "campaign_id":
                        #     cron_time(k1)
                        #     E_campaign_id = expect_json[k1]
                        #     A_campaign_id = v1
                        #     if E_campaign_id != A_campaign_id:
                        #         err[k1] = "%s expect %s,actual %s!" % (k1, E_campaign_id, A_campaign_id)
                        if k1 == "advertiser_id":
                            cron_time(k1)
                            E_advertiser_id = expect_json[k1]
                            A_advertiser_id = v1
                            if E_advertiser_id != A_advertiser_id:
                                err[k1] = "%s expect %s,actual %s!" % (k1, E_advertiser_id, A_advertiser_id)
                            check_over(k1)
                        # elif k1 == "template_id":
                        #     cron_time(k1)
                        #     E_template_id = expect_json[k1]
                        #     A_template_id = v1
                        #     if E_template_id != A_template_id:
                        #         err[k1] = "%s expect %s,actual %s!" % (k1, E_template_id, A_template_id)
                        #     check_over(k1)
                        elif k1 == "display_rule_id":
                            cron_time(k1)
                            E_display_rule_id = expect_json[k1]
                            A_display_rule_id = v1
                            if E_display_rule_id != A_display_rule_id:
                                err[k1] = "%s expect %s,actual %s!" % (k1, E_display_rule_id, A_display_rule_id)
                            check_over(k1)
                        # elif k1 == "category":
                        #     cron_time(k1)
                        #     for k2, v2 in expect_json[k1].iteritems():
                        #         E_category = v2
                        #         try:
                        #             A_category = v1[k2]
                        #         except Exception as e:
                        #             exc = "Exception_[%s][%s]" % (k1, k2)
                        #             err[exc] = str(e) + " not in api_json %s!" % (v1)
                        #             continue
                        #         for cg in E_category:
                        #             if not cg in A_category:
                        #                 c_k1 = "[%s][%s][%s]" % (k1, k2, cg)
                        #                 err[c_k1] = "%s in expect %s ,not in actual %s!" % (cg, E_category, A_category)
                        # elif k1 == "vendor_type":
                        #     cron_time(k1)
                        #     E_vendor_type = expect_json[k1]
                        #     A_vendor_type = v1
                        #     if E_vendor_type != A_vendor_type:
                        #         err[k1] = "%s expect %s,actual %s!" % (k1, E_vendor_type, A_vendor_type)
                        #     check_over(k1)
                        elif k1 == "size_sensitive":
                            cron_time(k1)
                            E_size_sensitive = expect_json[k1]
                            A_size_sensitive = v1
                            if E_size_sensitive != A_size_sensitive:
                                err[k1] = "%s expect %s,actual %s!" % (k1, E_size_sensitive, A_size_sensitive)
                            check_over(k1)
                        # elif k1 == "third_imp_monitor":
                        #     cron_time(k1)
                        #     E_third_imp_monitor = expect_json[k1]
                        #     for tim in E_third_imp_monitor:
                        #         if not tim in v1:
                        #             tim_k1 = "[%s][%s]" % (k1, tim)
                        #             err[tim_k1] = "%s in expect %s ,not in actual %s!" % (
                        #                 tim, E_third_imp_monitor, v1)
                        #     check_over(k1)
                        # elif k1 == "third_click_monitor":
                        #     cron_time(k1)
                        #     E_third_click_monitor = expect_json[k1]
                        #     for tcm in E_third_click_monitor:
                        #         if not tcm in v1:
                        #             tcm_k1 = "[%s][%s]" % (k1, tcm)
                        #             err[tcm_k1] = "%s in expect %s ,not in actual %s!" % (
                        #                 tcm, E_third_click_monitor, v1)
                        #     check_over(k1)
                        elif k1 == "app_notice_url":
                            cron_time(k1)
                            E_app_notice_url = expect_json[k1]
                            A_app_notice_url = v1
                            if E_app_notice_url != A_app_notice_url:
                                err[k1] = "%s expect %s,actual %s!" % (k1, E_app_notice_url, A_app_notice_url)
                            check_over(k1)
                        elif k1 == "status":
                            cron_time(k1)
                            E_status = expect_json[k1]
                            A_status = v1
                            if E_status != A_status:
                                err[k1] = "%s expect %s,actual %s!" % (k1, E_status, A_status)
                            check_over(k1)
                        elif k1 == "view_type":
                            cron_time(k1)
                            E_view_type = expect_json[k1]
                            for vt in E_view_type:
                                if not vt in v1:
                                    vt_k1 = "[%s][%s]" % (k1, vt)
                                    err[vt_k1] = "%s in expect %s ,not in actual %s!" % (
                                        vt, E_view_type, v1)
                            check_over(k1)
                        # elif k1 == "material_id":
                        #     cron_time(k1)
                        #     E_material_id = expect_json[k1]
                        #     for ma in E_material_id:
                        #         if not ma in v1:
                        #             ma_k1 = "[%s][%s]" % (k1, ma)
                        #             err[ma_k1] = "%s in expect %s ,not in actual %s!" % (
                        #                 ma, E_material_id, v1)
                        #     check_over(k1)
                        # elif k1 == "audit_status":
                        #     cron_time(k1)
                        #     for k2, v2 in expect_json[k1].iteritems():
                        #         E_audit_status = expect_json[k1][k2]
                        #         try:
                        #             A_audit_status = v1[k2]
                        #         except Exception as e:
                        #             exc = "Exception_[%s][%s]" % (k1, k2)
                        #             err[exc] = str(e) + " not in api_json %s!" % (v1)
                        #             continue
                        #         if E_audit_status != A_audit_status:
                        #             pv_k1 = "[%s][%s]" % (k1, k2)
                        #             err[pv_k1] = "expect %s,actual %s!" % (E_audit_status, A_audit_status)
                        # elif k1 == "ad_mapping":
                        #     cron_time(k1)
                        #     for k2, v2 in expect_json[k1].iteritems():
                        #         E_ad_mapping = expect_json[k1][k2]
                        #         try:
                        #             A_ad_mapping = v1[k2]
                        #         except Exception as e:
                        #             exc = "Exception_[%s][%s]" % (k1, k2)
                        #             err[exc] = str(e) + " not in api_json %s!" % (v1)
                        #             continue
                        #         if E_ad_mapping != A_ad_mapping:
                        #             pv_k1 = "[%s][%s]" % (k1, k2)
                        #             err[pv_k1] = "expect %s,actual %s!" % (E_ad_mapping, A_ad_mapping)
                        elif k1 == "support_size":
                            cron_time(k1)
                            E_support_size = expect_json[k1]
                            for ss in E_support_size:
                                if not ss in v1:
                                    ss_k1 = "[%s][%s]" % (k1, ss)
                                    err[ss_k1] = "%s in expect %s ,not in actual %s!" % (ss, E_support_size, v1)
                            check_over(k1)
                        elif k1 == "creative_grade":
                            cron_time(k1)
                            E_creative_grade = expect_json[k1]
                            A_creative_grade = v1
                            if E_creative_grade != A_creative_grade:
                                err[k1] = "%s expect %s,actual %s!" % (k1, E_creative_grade, A_creative_grade)
                            check_over(k1)
                        # elif k1 == "ad_level":
                        #     cron_time(k1)
                        #     ad_level = expect_json[k1]
                        #     if (type(ad_level) != type(v1)):
                        #         err["Exception_ad_level"] = "ad_level type expect %s, actual %s" % (
                        #             type(ad_level), type(v1))
                        #         continue
                        #     for k2, v2 in ad_level.iteritems():
                        #         E_ad_level = ad_level[k2]
                        #         try:
                        #             A_ad_level = v1[k2]
                        #         except Exception as e:
                        #             exc = "Exception_[%s][%s]" % (k1, k2)
                        #             err[exc] = str(e) + " not in api_json %s!" % (v1)
                        #             continue
                        #         if E_ad_level != A_ad_level:
                        #             pv_k1 = "[%s][%s]" % (k1, k2)
                        #             err[pv_k1] = "expect %s,actual %s!" % (E_ad_level, A_ad_level)

                        elif k1 == "template_size_mapping":
                            cron_time(k1)
                            E_template_size_mapping = expect_json[k1]
                            for tsm in E_template_size_mapping:
                                if not tsm in v1:
                                    tsm_k1 = "[%s][%s]" % (k1, tsm)
                                    err[tsm_k1] = "%s in expect %s ,not in actual %s!" % (
                                        tsm, E_template_size_mapping, v1)
                            check_over(k1)
                        else:
                            continue
        except Exception as e:
            err["campare_err"] = str(e)
    else:
        err["Exception_json_type"] = "json type is not string."
    if err:
        resp = {"status": 1, "result": "fail", "errors": err}
        api_type = "Ad_id: %s" % (ad_id)
        format_result(api_type, resp)
        result = {"status": 1}
    else:
        resp = {"status": 0, "result": "pass", "errors": ""}
        api_type = "ad_id: %s" % (ad_id)
        format_result(api_type, resp)
        result = {"status": 0}
    print "AD API compared finish.\n"
    return result


def api_unit_test(cam_case_result, cam_api_result, adg_case_result, adg_api_result, ad_case_result, ad_api_result,
                  campaign_id, adgroup_id, ad_id):
    class API_Test(unittest.TestCase):
        def setUp(self):
            self.cam_case_result = cam_case_result
            self.cam_api_result = cam_api_result
            self.adg_case_result = adg_case_result
            self.adg_api_result = adg_api_result
            self.ad_case_result = ad_case_result
            self.ad_api_result = ad_api_result
            self.campaign_id = campaign_id
            self.adgroup_id = adgroup_id
            self.ad_id = ad_id
            self.verficationErrors = []
            self.result = {}

        def campaign_api_test(self):
            self.result = cam_compare_json(self.cam_case_result, self.cam_api_result, self.campaign_id)
            self.assertEqual(0, self.result["status"])

        def adgroup_api_test(self):
            self.result = adg_compare_json(self.adg_case_result, self.adg_api_result, self.adgroup_id)
            self.assertEqual(0, self.result["status"])

        def ad_api_test(self):
            self.result = ad_compare_json(self.ad_case_result, self.ad_api_result, self.ad_id)
            self.assertEqual(0, self.result["status"])

        def tearDown(self):
            self.assertEqual([], self.verficationErrors)

    test_cases = unittest.TestSuite()
    test_cases.addTest(API_Test("campaign_api_test"))
    test_cases.addTest(API_Test("adgroup_api_test"))
    test_cases.addTest(API_Test("ad_api_test"))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    fp = open("api_result_" + now + ".html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='FE API TEST RESULT', description='DESCRIPTION:')
    result = runner.run(test_cases)
    fp.close()
    if result.failure_count == 0:
        return {"status": 0}
    else:
        return {"status": 1}
