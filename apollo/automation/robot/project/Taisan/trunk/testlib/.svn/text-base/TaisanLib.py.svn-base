__author__ = 'Eddie'


from robot.api import *
import os
from  datetime  import date
import json

class TaisanLib():

    def __init__(self):
        self.dna_filesize = None
        self.check_filesize = 100
        pass

    def __convert_mode(self,s):
        try:
            s = int(s)
        except:
            s = "'" + s + "'"
        finally:
            return s

    def vdna_query_conf(self, **kwargs):
        d_args = {'meta_uuid1':'f297ff38-aba0-11e0-af25-080027cf46d6',
                    'meta_uuid2':'eef5b7e2-aba2-11e0-af25-080027cf46d6',
                    'meta_uuid3':'56434dfc-b3fe-11e0-8437-08002752146d',
                    'meta_uuid4':'c0ee7e40-b4c3-11e0-8437-08002752146d',
                    'meta_uuid5':'877da2bc-ca44-11e0-9aba-080027cf46d6',
                    'reprocess_dna_filesize':10,
                    'reprocess_less_fn_match':0,
                    'reprocess_less_fp_match':0,
                    'reprocess_exact_match':0,
                    'less_fn_match':0,
                    'less_fp_match':0,
                    'exact_match':0,
                    'speed_change_match':0,
                    'reprocess_speed_change_match':0}

        for k,v in kwargs.items():
            d_args[k] = v

        self.dna_filesize = d_args['reprocess_dna_filesize']
        s = ''
        for k,v in d_args.items():
            v = self.__convert_mode(v)
            s += k + ' = ' + str(v) + '\n'

        return s

    def get_dna_filesize(self):
        return self.dna_filesize

    def get_query_di(self, query_di, *args):
        self.query_di = json.loads(query_di)
        def __get_keys(f_dict):
            for k,v in f_dict.items():
                self.keys_list.append(k)
                if isinstance(v, dict):
                    return __get_keys(v)
                else:
                    self.keys_list.append(v)
                    return self.keys_list

        if args:
            for arg in args:
                arg = json.loads(str(arg))
                self.keys_list = []
                arg_keys_list = __get_keys(arg)

                if isinstance(arg_keys_list[-1],(str,unicode)):
                    value = '"' + str(arg_keys_list[-1]) + '"'
                else:
                    value = str(arg_keys_list[-1])

                if 'metas' in arg_keys_list:
                    metas_index = arg_keys_list.index('metas')
                    t_key = 'self.query_di' + ''.join(map(lambda s:'["' + s + '"]',arg_keys_list[:metas_index + 1]))
                    metas = eval(t_key)
                    for i in range(len(metas)):
                        key = t_key + '[' + str(i) + ']' + ''.join(map(lambda s:'["' + s + '"]',arg_keys_list[metas_index+1:-1]))
                        cmd = ' = '.join([key,value])
                        self.exec_cmd(cmd)
                else:
                    key = 'self.query_di' + ''.join(map(lambda s:'["' + s + '"]',arg_keys_list[:-1]))
                    cmd = ' = '.join([key,value])
                    self.exec_cmd(cmd)
            return json.dumps(self.query_di)

        else:
            return json.dumps(self.query_di)

    def exec_cmd(self,cmd):
        #logger.warn(cmd)
        exec(cmd)




    def get_linux_cmd(self, cmd, value=False):
        if value:
            cmd  = cmd % value

        return cmd

    def get_dna_path(self, di):
        di = json.loads(di)
        #di = dict(di)
        key_id = di["parameters"]["video"]["key_id"]
        website = di["parameters"]["website"]
        d = str(date.today())

        l_path = (d, website, key_id[-2:])

        return "/".join(l_path), key_id

    def parse_query_log(self, log):

        return '\r\n'.join(log.split('\n')[6:])

    def check_retriever_result(self, result, **kwargs):
        result = json.loads(result)
        if result['error_code'] != 0:
            raise AssertionError('retriever error_code is %d,  retriever result is: %s' % (result['error_code'], result))

        r = {}
        for match in result['matches']:
            if match['details']:
                if not match['match_query_profile']:
                    match_query_profile = 'Common'
                else:
                    match_query_profile = match['match_query_profile']
                r.setdefault(match_query_profile,{'audio':0,'video':0})
                for detail in match['details']:
                    r[match_query_profile][detail['track_type']] += 1

        if not r == kwargs:
            e_r = {}
            a_r = {}
            for k,v in kwargs.items():
                if str(v) == 'None':
                    if r.has_key(k):
                        e_r.setdefault(k,None)
                        a_r.setdefault(k,v)
                    continue
                if not r.has_key(k):
                    e_r.setdefault(k,v)
                    a_r.setdefault(k,None)
                    continue
                for kk, vv in v.items():
                    if not r[k].has_key(kk):
                        e_r.setdefault(k,{})
                        e_r[k].setdefault(kk,vv)
                        a_r.setdefault(k,{})
                        a_r[k].setdefault(kk,None)
                        continue
                    if r[k][kk] != vv:
                        e_r.setdefault(k,{})
                        e_r[k].setdefault(kk,vv)
                        a_r.setdefault(k,{})
                        a_r[k].setdefault(kk,r[k][kk])
            if e_r and a_r:
                raise AssertionError('Expected Results: %s, Actual results: %s' % (e_r, a_r))

    def get_dna_file(self):
        import os
        file = os.path.split(os.path.realpath(__file__))[0] + '/dna_file'
        with open(file, 'r') as f:
            lines = f.readlines()

        return '.'.join(lines)

    def check_query_log(self, msg):
        c = msg.split('/r/n')[0].split(':')[-1]
        if self.dna_filesize > self.check_filesize:
            pass


if __name__ == '__main__':
    T = TaisanLib()
    #d = '''{"processor":"retriever","parameters":{"task_id":3495146763,"instruction":"DNAIdentify","website":"youku","website_type":"ugc","slideshow_process":"none","video":{"id":2983894931,"trackingWebsite_id":2,"key_id":"XNTk3NTIzOTky","clip_url":"http://v.youku.com/v_show/id_XNTk3NTIzOTky.html","source_type":"keyword_search","clip_duration":248,"download_duration":0,"max_evidence_size":0,"file_type":"video","download_url":"","post_date":"","img_url":"http://dailymotion.com/fake/x12fx2l.jpg","storage_date":"2013-10-24","storage_domain":"192.168.1.232","is_video_detail_exist":false,"matched_storage_date":"2013-10-24","matched_storage_domain":"192.168.1.232","matched_media_suffix":"flv","is_dna_full_length":false,"is_media_rebuild_index":false,"is_reprocess_enabled":false,"is_media_rebuild_index_needed":false,"manga_storage_date":"","manga_domain_path":"","slideshow_dna_count":0},"metas":[{"meta_id":1,"meta_uuid":"11111111-1111-1111-1111-111111111111","is_light_enabled":false,"query_profile":"%s"},{"meta_id":2,"meta_uuid":"22222222-2222-2222-2222-222222222222","is_light_enabled":false,"query_profile":"%s"},{"meta_id":3,"meta_uuid":"33333333-3333-3333-3333-333333333333","is_light_enabled":false,"query_profile":"%s"},{"meta_id":4,"meta_uuid":"44444444-4444-4444-4444-444444444444","is_light_enabled":false,"query_profile":"%s"},{"meta_id":5,"meta_uuid":"5555555-5555-5555-5555-555555555555","is_light_enabled":false,"query_profile":"%s"}]}}
    #'''
    #print T.get_dna_path(d, 'dddd')
    #print len(T.get_dna_file())
    s = '''
       {
   "task_id": 3495146763,
   "video": {
       "id": 2983894931,
       "trackingWebsite_id": 2,
       "website": "youku",
       "key_id": "XNTk3NTIzOTky",
       "clip_url": "http://v.youku.com/v_show/id_XNTk3NTIzOTky.html",
       "download_url": "http://k.youku.com/player/getFlvPath/sid/2404897768757128e4e79_00/st/flv/fileid/03000201005206EC6CB5AA03B8591DC4C5BF50-74EA-C072-0121-D0854E48F84E?K=219bde26003c84432829aee1&ctype=12&ev=1&oip=1909917328&token=4326&ep=cCaUHkGEUckG7STajz8bb3nmIXAGXP4J9h+Fg9JjALshSui57E3XtO+1P45CFYsRdysHZJj12NWVHEUUYfdH3BkQrE6vO/rg//Li5dlTzJUEEx0+BMXTwVSaQDL3",
       "img_url": "http://dailymotion.com/fake/x12fx2l.jpg",
       "file_type": "audio_video",
       "post_date": "",
       "clip_duration": 123,
       "download_duration": 123,
       "view_count": 0,
       "clip_size": 4428134,
       "slideshow_dna_count": 0,
       "storage_date": "2014-07-09",
       "storage_domain": "192.168.1.246",
       "matched_storage_date": "2014-07-09",
       "matched_storage_domain": "192.168.1.246",
       "matched_media_suffix": "flv",
       "is_media_rebuild_index": false,
       "hybrid_download_url": "",
       "manga_storage_date": "",
       "manga_domain_path": "",
       "is_slideshow": "false",
       "gen_slideshow_di": "false",
       "static_score": 0,
       "blackwhite_score": 0.83,
       "border_detect_info": "",
       "is_border_detected": false
   },
   "matches": [
       {
           "meta_uuid": "11111111-1111-1111-1111-111111111111",
           "meta_title": "Kung.Fu.Dunk.2008",
           "meta_query_profile": "Less FN",
           "match_query_profile": "Common",
           "start_time": "2014-07-09 17:23:43",
           "finish_time": "2014-07-09 17:23:44",
           "details": [
               {
                   "instance_uuid": "49c0b4a2-fed1-11e0-9808-080027cf46d6",
                   "track_type": "video",
                   "track_id": 3,
                   "match_duration": 1360,
                   "score": 100,
                   "reference_offset": 1300,
                   "sample_offset": 1330
               },
               {
                   "instance_uuid": "a0fdc2f6-c906-44ed-9573-69ebfb91c1b9",
                   "track_type": "audio",
                   "track_id": 3,
                   "match_duration": 360,
                   "score": 99,
                   "reference_offset": 300,
                   "sample_offset": 300
               }
           ]
       },
       {
           "meta_uuid": "22222222-2222-2222-2222-222222222222",
           "meta_query_profile": "Less FN",
           "match_query_profile": "",
           "start_time": "2014-07-09 17:23:43",
           "finish_time": "2014-07-09 17:23:44",
           "details": []
       },
       {
           "meta_uuid": "33333333-3333-3333-3333-333333333333",
           "meta_title": "Movie 3--- handspuppy",
           "meta_query_profile": "Less FN",
           "match_query_profile": "Common",
           "start_time": "2014-07-09 17:23:43",
           "finish_time": "2014-07-09 17:23:44",
           "details": [
               {
                   "instance_uuid": "7ac36d4a-9b69-4b19-ab64-314a502e2732",
                   "track_type": "video",
                   "track_id": 0,
                   "match_duration": 120,
                   "score": 66,
                   "reference_offset": 55,
                   "sample_offset": 55
               },
               {
                   "instance_uuid": "7ac36d4a-9b69-4b19-ab64-314a502e2732",
                   "track_type": "audio",
                   "track_id": 2,
                   "match_duration": 840,
                   "score": 96,
                   "reference_offset": 555,
                   "sample_offset": 555
               }
           ]
       },
       {
           "meta_uuid": "44444444-4444-4444-4444-444444444444",
           "meta_query_profile": "Less FN",
           "match_query_profile": "",
           "start_time": "2014-07-09 17:23:43",
           "finish_time": "2014-07-09 17:23:44",
           "details": []
       },
       {
           "meta_uuid": "5555555-5555-5555-5555-555555555555",
           "meta_query_profile": "Less FN",
           "match_query_profile": "",
           "start_time": "2014-07-09 17:23:43",
           "finish_time": "2014-07-09 17:23:44",
           "details": []
       }
   ],
   "consume_time": {
       "dna_generate_time": 6,
       "dna_query_time": 1,
       "download_time": 48,
       "get_slideshow_resource_time": -1,
       "reprocess_dna_generate_time": -1,
       "reprocess_dna_query_time": -1,
       "reprocess_download_time": -1,
       "reprocess_reserve_time": 4,
       "reserve_slideshow_resource_time": -1,
       "reserve_time": 1,
       "slideshow_detect_time": -1
   },
   "resource_node_storage": {
       "sn_dna_size": 64288,
       "sn_full_dna_size": 64288,
       "sn_animation_size": 161739,
       "sn_thumbnail_size": 2986
   },
   "evidence_node_storage": {
       "msn_media_size": 4428134,
       "msn_animation_size": 161739,
       "msn_thumbnail_size": 2986
   },
   "download_flow_rate": 4452384,
   "error_code": 0,
   "error_extra_info": "url [http://v.youku.com/v_show/id_XNTk3NTIzOTky.html], "
}
    '''

    ss = '''
    {
    "task_id": 3495146763,
    "video": {
        "id": 2983894931,
        "trackingWebsite_id": 2,
        "website": "youku",
        "key_id": "XNTk3NTIzOTky",
        "clip_url": "http://v.youku.com/v_show/id_XNTk3NTIzOTky.html",
        "download_url": "http://k.youku.com/player/getFlvPath/sid/540550533955412e7dc62_00/st/flv/fileid/03000201005206EC6CB5AA03B8591DC4C5BF50-74EA-C072-0121-D0854E48F84E?K=fe17680c7be8d3c7261dc95a&ctype=12&ev=1&oip=1909917328&token=6473&ep=dyaUH0yNU80D7CbajD8bMiu2J3ENXP4J9h+Fg9JjALshSui57E3XtO+1P45CFYsRdysHZJj12NWVHEUUYfdH3BkQrE6vO/rg//Li5dlTzJUEEx0+BMXTwVSYRzfy",
        "img_url": "http://dailymotion.com/fake/x12fx2l.jpg",
        "file_type": "audio_video",
        "post_date": "",
        "clip_duration": 123,
        "download_duration": 123,
        "view_count": 0,
        "clip_size": 4428134,
        "slideshow_dna_count": 0,
        "storage_date": "2014-07-16",
        "storage_domain": "192.168.1.246",
        "matched_storage_date": "2014-07-16",
        "matched_storage_domain": "192.168.1.246",
        "matched_media_suffix": "flv",
        "is_media_rebuild_index": false,
        "hybrid_download_url": "",
        "manga_storage_date": "",
        "manga_domain_path": "",
        "is_slideshow": "false",
        "gen_slideshow_di": "false",
        "static_score": 0,
        "blackwhite_score": 0.83,
        "border_detect_info": "",
        "is_border_detected": false
    },
    "matches": [
        {
            "meta_uuid": "f297ff38-aba0-11e0-af25-080027cf46d6",
            "meta_title": "Kung.Fu.Dunk.2008",
            "meta_query_profile": "",
            "match_query_profile": "",
            "start_time": "2014-07-16 18:12:09",
            "finish_time": "2014-07-16 18:12:10",
            "details": [
                {
                    "instance_uuid": "49c0b4a2-fed1-11e0-9808-080027cf46d6",
                    "track_type": "video",
                    "track_id": 3,
                    "match_duration": 1360,
                    "score": 100,
                    "reference_offset": 1300,
                    "sample_offset": 1330
                },
                {
                    "instance_uuid": "a0fdc2f6-c906-44ed-9573-69ebfb91c1b9",
                    "track_type": "audio",
                    "track_id": 3,
                    "match_duration": 360,
                    "score": 99,
                    "reference_offset": 300,
                    "sample_offset": 300
                }
            ]
        },
        {
            "meta_uuid": "56434dfc-b3fe-11e0-8437-08002752146d",
            "meta_title": "Movie 3--- handspuppy",
            "meta_query_profile": "Common",
            "match_query_profile": "",
            "start_time": "2014-07-16 18:12:09",
            "finish_time": "2014-07-16 18:12:10",
            "details": [
                {
                    "instance_uuid": "7ac36d4a-9b69-4b19-ab64-314a502e2732",
                    "track_type": "video",
                    "track_id": 0,
                    "match_duration": 120,
                    "score": 66,
                    "reference_offset": 55,
                    "sample_offset": 55
                },
                {
                    "instance_uuid": "7ac36d4a-9b69-4b19-ab64-314a502e2732",
                    "track_type": "audio",
                    "track_id": 2,
                    "match_duration": 840,
                    "score": 96,
                    "reference_offset": 555,
                    "sample_offset": 555
                }
            ]
        }
    ],
    "consume_time": {
        "dna_generate_time": 5,
        "dna_query_time": 1,
        "download_time": 184,
        "get_slideshow_resource_time": -1,
        "reprocess_dna_generate_time": -1,
        "reprocess_dna_query_time": -1,
        "reprocess_download_time": -1,
        "reprocess_reserve_time": 4,
        "reserve_slideshow_resource_time": -1,
        "reserve_time": 1,
        "slideshow_detect_time": -1
    },
    "resource_node_storage": {
        "sn_dna_size": 64287,
        "sn_full_dna_size": 64287,
        "sn_animation_size": 161739,
        "sn_thumbnail_size": 2986
    },
    "evidence_node_storage": {
        "msn_media_size": 4428134,
        "msn_animation_size": 161739,
        "msn_thumbnail_size": 2986
    },
    "download_flow_rate": 4452631,
    "error_code": 0,
    "error_extra_info": "url [http://v.youku.com/v_show/id_XNTk3NTIzOTky.html], "
}
    '''
    #T.check_retriever_result(s,Common={'audio':0,'video':0})
    #T.check_retriever_result(s,Common={'audio':0,'video':2})
    #T.check_retriever_result(s,Common={'audio':2,'video':0})
    T.check_retriever_result(s,Common={'audio':2,'video':2}, FN=None)
    #T.get_dna_file()