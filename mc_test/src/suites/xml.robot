*** settings ***
Test Setup        init env    ${merchant_uri}    ${mc_info_uri}
Test Teardown     delete all session
Force Tags        xml
Resource          res.robot
Variables         ../data/var.py

*** Test Cases ***
post one
    post_xslt_success    ${xslt_url}    ${xslt_req_3}    ${xslt_resp_3}
    post_feed_success    ${feed_url}    ${feed_req_1}    ${feed_resp_2}
    post_xml_success    ${xml_url}    ${xml_req_1}    ${xml_resp_1}

get
    post_xslt_success    ${xslt_url}    ${xslt_req_3}    ${xslt_resp_3}
    post_feed_success    ${feed_url}    ${feed_req_1}    ${feed_resp_2}
    ${xml_res}    post_xml_success    ${xml_url}    ${xml_req_1}    ${xml_resp_1}
    ${xml_json_res}    to_json    ${xml_res.content}
    ${xml_resget}    get    ${xml_url+'${xml_json_res['response']['_id']}/'}
    xml_get_check    ${xml_json_res}    ${xml_resp_1}    ${xml_resget}
    ${xml_resget2}    get    ${xml_url}
    resp_should_be_equal    ${xml_resget2.status_code}    ${200}
    ${xml_json_resget2}    to_json    ${xml_resget2.content}
    ${xml_piped_respone}    delete_item    ${xml_json_resget2['response'][0]}    path
    resp_should_be_equal    ${xml_piped_respone}    ${xml_resp_1}
    ${xml_find_list}    m_select    mc_info    xmls    ${xml_json_res['response']['_id']}
    ${xml_find_list}    delete_item    ${xml_find_list[0]}    path
    resp_should_be_equal    ${xml_find_list}    ${xml_piped_respone}
