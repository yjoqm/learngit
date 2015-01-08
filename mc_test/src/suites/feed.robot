*** settings ***
Test Setup        init env    ${merchant_uri}    ${mc_info_uri}
Test Teardown     delete all session
Force Tags        feed
Resource          res.robot
Variables         ../data/var.py

*** Test Cases ***
post one
    post_xslt_success    ${xslt_url}    ${xslt_req_1}    ${xslt_resp_1}
    post_feed_success    ${feed_url}    ${feed_req_1}    ${feed_resp_1}

get
    post_xslt_success    ${xslt_url}    ${xslt_req_1}    ${xslt_resp_1}
    ${feed_res}    post_feed_success    ${feed_url}    ${feed_req_1}    ${feed_resp_1}
    ${feed_json_res}    to_json    ${feed_res.content}
    ${feed_resget}    get    ${feed_url+'${feed_json_res['response']['_id']}/'}
    ${feed_json_resget}    to_json    ${feed_resget.content}
    is_empty_list    ${feed_json_resget['errors']}
    resp_should_be_equal    ${feed_resget.status_code}    ${200}
    ${feed_piped_response}    delete_item    ${feed_json_resget['response']}
    ${feed_resp}    delete_item    ${feed_resp_1}    next_check_time    crawler_sizzle    crawler_sizzle_name
    resp_should_be_equal    ${feed_piped_response}    ${feed_resp_1}
    ${feed_find_list}    m_select    mc_info    feeds    ${feed_json_res['response']['_id']}
    ${feed_find_list}    delete_item    ${feed_find_list[0]}    next_check_time    crawler_sizzle    crawler_sizzle_name
    resp_should_be_equal    ${feed_find_list}    ${feed_piped_response}
    ${feed_resget2}    get    ${feed_url}
    ${feed_json_resget}    to_json    ${feed_resget.content}
    is_empty_list    ${feed_json_resget['errors']}
    resp_should_be_equal    ${feed_resget.status_code}    ${200}
    ${feed_piped_response}    delete_item    ${feed_json_resget['response']}
    ${feed_resp}    delete_item    ${feed_resp_1}    next_check_time    crawler_sizzle    crawler_sizzle_name
    resp_should_be_equal    ${feed_piped_response}    ${feed_resp_1}

delete
    post_xslt_success    ${xslt_url}    ${xslt_req_1}    ${xslt_resp_1}
    ${feed_res}    post_feed_success    ${feed_url}    ${feed_req_1}    ${feed_resp_1}
    ${feed_json_res}    to_json    ${feed_res.content}
    ${feed_resdel}    delete    ${feed_url+'${feed_json_res['response']['_id']}/'}
    resp_should_be_equal    ${feed_resdel.status_code}    ${200}
    ${feed_json_resget}    to_json    ${feed_resdel.content}
    is_empty_list    ${feed_json_resget['errors']}
    ${feed_find_list}    m_select    mc_info    feeds    ${feed_json_res['response']['_id']}
    ${feed_find_listlen}    Evaluate    len(${feed_find_list})
    Should Be Equal As Numbers    ${feed_find_listlen}    0

put
    post_xslt_success    ${xslt_url}    ${xslt_req_1}    ${xslt_resp_1}
    ${feed_res}    post_feed_success    ${feed_url}    ${feed_req_1}    ${feed_resp_1}
    ${feed_json_res}    to_json    ${feed_res.content}
    ${feed_resput}    put    ${feed_url+'${feed_json_res['response']['_id']}/'}    ${feed_req_3}
    ${feed_json_resput}    to_json    ${feed_resput.content}
    is_empty_list    ${feed_json_resput['errors']}
    resp_should_be_equal    ${feed_resput.status_code}    ${200}
    ${feed_piped_response}    delete_item    ${feed_json_resput['response']}
    ${feed_resp3}    delete_item    ${feed_resp_3}    next_check_time    crawler_sizzle    crawler_sizzle_name
    resp_should_be_equal    ${feed_piped_response}    ${feed_resp3}
    ${feed_find_list}    m_select    mc_info    feeds    ${feed_json_res['response']['_id']}
    ${feed_find_list}    delete_item    ${feed_find_list[0]}    next_check_time    crawler_sizzle    crawler_sizzle_name
    resp_should_be_equal    ${feed_find_list}    ${feed_piped_response}
