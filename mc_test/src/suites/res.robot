*** settings ***
Library           src.McLibrary
Variables         ../data/var.py

*** keywords ***
init env
    [Arguments]    ${merchant_uri}    ${mc_info_uri}
    create_mongo_client    ${merchant_uri}    merchant
    create_mongo_client    ${mc_info_uri}    mc_info
    init_db    merchant
    init_db    mc_info
    create_session

post_xslt_success
    [Arguments]    ${xslt_url}    ${xslt_req}    ${xslt_resp}
    ${xslt_res}    json_post    ${xslt_url}    ${xslt_req}
    resp_should_be_equal    ${xslt_res.status_code}    ${200}
    ${xslt_json_res}    to_json    ${xslt_res.content}
    resp_should_be_equal    ${xslt_json_res['status']}    ${0}
    is_empty_list    ${xslt_json_res['errors']}
    ${xslt_find_list}    m_select    mc_info    xslts    ${xslt_json_res['response']['_id']}
    resp_should_be_equal    ${xslt_find_list[0]}    ${xslt_resp}
    ${xslt_piped_response}    delete_item    ${xslt_json_res['response']}
    resp_should_be_equal    ${xslt_piped_response}    ${xslt_resp}
    [Return]    ${xslt_res}

post_feed_success
    [Arguments]    ${feed_url}    ${feed_req}    ${feed_resp}
    ${feed_res}    json_post    ${feed_url}    ${feed_req}
    resp_should_be_equal    ${feed_res.status_code}    ${200}
    ${feed_json_res}    to_json    ${feed_res.content}
    resp_should_be_equal    ${feed_json_res['status']}    ${0}
    is_empty_list    ${feed_json_res['errors']}
    ${feed_find_list}    m_select    mc_info    feeds    ${feed_json_res['response']['_id']}
    resp_should_be_equal    ${feed_find_list[0]}    ${feed_resp}
    ${feed_piped_response}    delete_item    ${feed_json_res['response']}
    resp_should_be_equal    ${feed_piped_response}    ${feed_resp}
    [Teardown]
    [Return]    ${feed_res}

post_xml_success
    [Arguments]    ${xml_url}    ${xml_req}    ${xml_resp}
    ${xml_res}    xml_post    ${xml_url}    ${xml_req}
    resp_should_be_equal    ${xml_res.status_code}    ${200}
    ${xml_json_res}    to_json    ${xml_res.content}
    resp_should_be_equal    ${xml_json_res['status']}    ${0}
    is_empty_list    ${xml_json_res['errors']}
    ${xml_find_list}    m_select    mc_info    xmls    ${xml_json_res['response']['_id']}    path
    resp_should_be_equal    ${xml_find_list[0]}    ${xml_resp}
    ${xml_piped_response}    delete_item    ${xml_json_res['response']}    path
    resp_should_be_equal    ${xml_piped_response}    ${xml_resp}
    [Teardown]
    [Return]    ${xml_res}

post_merchant_success
    [Arguments]    ${merchant_url}    ${merchant_req}    ${merchant_resp}
    ${merchant_res}    mer_post    ${merchant_url}    ${merchant_req}
    resp_should_be_equal    ${merchant_res.status_code}    ${200}
    ${merchant_json_res}    to_json    ${merchant_res.content}
    resp_should_be_equal    ${merchant_json_res['status']}    ${0}
    is_empty_list    ${merchant_json_res['errors']}
    ${merchant_find_list}    mer_select    online    1    ${merchant_json_res['response']['_id']}
    ${merchant_find_dblist}    delete_item    ${merchant_find_list[0]}    hash
    ${merchant_piped_respone}    delete_item    ${merchant_json_res['response']}    hash
    ${merchant_piped_respone}    delete_item    ${merchant_json_res['response']}    64strid
    resp_should_be_equal    ${merchant_piped_respone}    ${merchant_resp}
    resp_should_be_equal    ${merchant_find_dblist}    ${merchant_resp}
    [Teardown]
    [Return]    ${merchant_res}

post_attr_success
    [Arguments]    ${attr_url}    ${attr_req}    ${attr_resp}
    ${attr_res}    json_post    ${attr_url}    ${attr_req}
    resp_should_be_equal    ${attr_res.status_code}    ${200}
    ${attr_json_res}    to_json    ${attr_res.content}
    resp_should_be_equal    ${attr_json_res['status']}    ${0}
    is_empty_list    ${attr_json_res['errors']}
    ${attr_piped_response}    delete_item    ${attr_json_res['response']}    name
    ${attr_resp}    delete_item    ${attr_resp}    name
    resp_should_be_equal    ${attr_piped_response}    ${attr_resp}
    [Teardown]
    [Return]    ${attr_res}

post_mertype_success
    [Arguments]    ${mertype_url}    ${mertype_req}    ${mertype_resp}
    ${mertype_res}    json_post    ${mertype_url}    ${mertype_req}
    resp_should_be_equal    ${mertype_res.status_code}    ${200}
    ${mertype_json_res}    to_json    ${mertype_res.content}
    resp_should_be_equal    ${mertype_json_res['status']}    ${0}
    is_empty_list    ${mertype_json_res['errors']}
    ${mertype_find_list}    m_select    mc_info    merchanttypes    ${mertype_json_res['response']['_id']}
    resp_should_be_equal    ${mertype_find_list[0]}    ${mertype_resp}
    ${mertype_piped_response}    delete_item    ${mertype_json_res['response']}
    resp_should_be_equal    ${mertype_piped_response}    ${mertype_resp}
    [Teardown]
    [Return]    ${mertype_res}

post_crawler_success
    [Arguments]    ${crawler_url}    ${crawler_req}    ${crawler_resp}
    ${crawler_res}    json_post    ${crawler_url}    ${crawler_req}
    resp_should_be_equal    ${crawler_res.status_code}    ${200}
    ${crawler_json_res}    to_json    ${crawler_res.content}
    resp_should_be_equal    ${crawler_json_res['status']}    ${0}
    is_empty_list    ${crawler_json_res['errors']}
    ${crawler_find_list}    m_select    mc_info    crawlersizzle    ${crawler_json_res['response']['_id']}
    resp_should_be_equal    ${crawler_find_list[0]}    ${crawler_resp}
    ${crawler_piped_response}    delete_item    ${crawler_json_res['response']}
    resp_should_be_equal    ${crawler_piped_response}    ${crawler_resp}
    [Teardown]
    [Return]    ${crawler_res}

xslt_get_check
    [Arguments]    ${xslt_json_res}    ${xslt_resp_1}    ${xslt_json_resget}
    ${xslt_piped_respone}    delete_item    ${xslt_json_resget['response']}
    resp_should_be_equal    ${xslt_piped_respone}    ${xslt_resp_1}
    ${xslt_find_list}    m_select    mc_info    xslts    ${xslt_json_res['response']['_id']}
    resp_should_be_equal    ${xslt_find_list[0]}    ${xslt_piped_respone}

feed_get_check
    [Arguments]    ${feed_json_res}    ${feed_resp_1}    ${feed_resget}
    ${feed_json_resget}    to_json    ${feed_resget.content}
    is_empty_list    ${feed_json_resget['errors']}
    resp_should_be_equal    ${feed_resget.status_code}    ${200}
    ${feed_piped_response}    delete_item    ${feed_json_resget['response']}
    ${feed_resp}    delete_item    ${feed_resp_1}    next_check_time    crawler_sizzle    crawler_sizzle_name
    resp_should_be_equal    ${feed_piped_response}    ${feed_resp_1}
    ${feed_find_list}    m_select    mc_info    feeds    ${feed_json_res['response']['_id']}
    ${feed_find_list}    delete_item    ${feed_find_list[0]}    next_check_time    crawler_sizzle    crawler_sizzle_name
    resp_should_be_equal    ${feed_find_list}    ${feed_piped_response}

attr_get_check
    [Arguments]    ${attr_json_res}    ${attr_resp_1}    ${attr_resget}
    ${attr_json_resget}    to_json    ${attr_resget.content}
    is_empty_list    ${attr_json_resget['errors']}
    resp_should_be_equal    ${attr_resget.status_code}    ${200}
    ${attr_piped_response}    delete_item    ${attr_json_resget['response']}    status    name
    ${attr_resp}    delete_item    ${attr_resp_1}    name
    resp_should_be_equal    ${attr_piped_response}    ${attr_resp}
    ${attr_find_list}    m_select    mc_info    attrs    ${attr_json_res['response']['_id']}
    ${attr_find_list}    delete_item    ${attr_find_list[0]}    name    status
    ${attr_piped_response}    delete_item    ${attr_piped_response}    macro
    resp_should_be_equal    ${attr_find_list}    ${attr_piped_response}

crawler_get_check
    [Arguments]    ${crawler_json_res}    ${crawler_resp_1}    ${crawler_resget}
    ${crawler_json_resget}    to_json    ${crawler_resget.content}
    is_empty_list    ${crawler_json_resget['errors']}
    resp_should_be_equal    ${crawler_resget.status_code}    ${200}
    ${crawler_piped_response}    delete_item    ${crawler_json_resget['response']}    update_time    create_time
    resp_should_be_equal    ${crawler_piped_response}    ${crawler_resp_1}
    ${crawler_find_list}    m_select    mc_info    crawlersizzle    ${crawler_json_res['response']['_id']}
    resp_should_be_equal    ${crawler_find_list[0]}    ${crawler_piped_response}

xml_get_check
    [Arguments]    ${xml_json_res}    ${xml_resp_1}    ${xml_resget}
    ${xml_json_resget}    to_json    ${xml_resget.content}
    is_empty_list    ${xml_json_resget['errors']}
    resp_should_be_equal    ${xml_resget.status_code}    ${200}
    ${xml_piped_respone}    delete_item    ${xml_json_resget['response']}    path
    resp_should_be_equal    ${xml_piped_respone}    ${xml_resp_1}
    ${xml_find_list}    m_select    mc_info    xmls    ${xml_json_res['response']['_id']}
    ${xml_find_list}    delete_item    ${xml_find_list[0]}    path
    resp_should_be_equal    ${xml_find_list}    ${xml_piped_respone}

merchant_get_check
    [Arguments]    ${merchant_json_res}    ${merchant_resp_1}    ${merchant_resget}
    ${merchant_json_resget}    to_json    ${merchant_resget.content}
    is_empty_list    ${merchant_json_resget['errors']}
    resp_should_be_equal    ${merchant_resget.status_code}    ${200}
    ${merchant_piped_respone}    delete_item    ${merchant_json_resget['response']}    hash    64strid
    resp_should_be_equal    ${merchant_piped_respone}    ${merchant_resp_1}

mertype_get_check
    [Arguments]    ${mertype_json_res}    ${mertype_resp_1}    ${mertype_resget}
    ${mertype_json_resget}    to_json    ${mertype_resget.content}
    is_empty_list    ${mertype_json_resget['errors']}
    resp_should_be_equal    ${mertype_resget.status_code}    ${200}
    ${mertype_piped_respone}    delete_item    ${mertype_json_resget['response']}
    resp_should_be_equal    ${mertype_piped_respone}    ${mertype_resp_1}
    ${mertype_find_list}    m_select    mc_info    merchanttypes    ${mertype_json_res['response']['_id']}
    resp_should_be_equal    ${mertype_find_list[0]}    ${mertype_piped_respone}
