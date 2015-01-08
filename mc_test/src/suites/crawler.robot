*** settings ***
Test Setup        init env    ${merchant_uri}    ${mc_info_uri}
Test Teardown     delete all session
Force Tags        crawler
Resource          res.robot
Variables         ../data/var.py

*** Test Cases ***
post one
    post_crawler_success    ${crawler_url}    ${crawler_req_1}    ${crawler_resp_1}

get
    ${crawler_res}    post_crawler_success    ${crawler_url}    ${crawler_req_1}    ${crawler_resp_1}
    ${crawler_json_res}    to_json    ${crawler_res.content}
    ${crawler_resget}    get    ${crawler_url+'${crawler_json_res['response']['_id']}/'}
    ${crawler_json_resget}    to_json    ${crawler_resget.content}
    is_empty_list    ${crawler_json_resget['errors']}
    resp_should_be_equal    ${crawler_resget.status_code}    ${200}
    ${crawler_piped_response}    delete_item    ${crawler_json_resget['response']}    update_time    create_time
    resp_should_be_equal    ${crawler_piped_response}    ${crawler_resp_1}
    ${crawler_find_list}    m_select    mc_info    crawlersizzle    ${crawler_json_res['response']['_id']}
    resp_should_be_equal    ${crawler_find_list[0]}    ${crawler_piped_response}
    ${crawler_resget2}    get    ${crawler_url}
    resp_should_be_equal    ${crawler_resget2.status_code}    ${200}
    ${crawler_json_resget2}    to_json    ${crawler_resget2.content}
    is_empty_list    ${crawler_json_resget2['errors']}
    ${crawler_piped_response}    delete_item    ${crawler_json_resget2['response'][0]}    update_time    create_time
    resp_should_be_equal    ${crawler_piped_response}    ${crawler_resp_1}
    ${crawler_find_list}    m_select    mc_info    crawlersizzle    ${crawler_json_res['response']['_id']}
    resp_should_be_equal    ${crawler_find_list[0]}    ${crawler_piped_response}

delete
    ${crawler_res}    post_crawler_success    ${crawler_url}    ${crawler_req_1}    ${crawler_resp_1}
    ${crawler_json_res}    to_json    ${crawler_res.content}
    ${crawler_resdel}    delete    ${crawler_url+'${crawler_json_res['response']['_id']}/'}
    ${crawler_json_resdel}    to_json    ${crawler_resdel.content}
    is_empty_list    ${crawler_json_resdel['errors']}
    resp_should_be_equal    ${crawler_resdel.status_code}    ${200}
    ${crawler_find_list}    m_select    mc_info    xslts    ${crawler_json_res['response']['_id']}
    ${crawler_find_listlen}    Evaluate    len(${crawler_find_list})
    Should Be Equal As Numbers    ${crawler_find_listlen}    0

put
    ${crawler_res}    post_crawler_success    ${crawler_url}    ${crawler_req_1}    ${crawler_resp_1}
    ${crawler_json_res}    to_json    ${crawler_res.content}
    ${crawler_resget}    put    ${crawler_url+'${crawler_json_res['response']['_id']}/'}    ${crawler_req_2}
    ${crawler_json_resput}    to_json    ${crawler_resget.content}
    is_empty_list    ${crawler_json_resput['errors']}
    resp_should_be_equal    ${crawler_resget.status_code}    ${200}
    ${crawler_piped_response}    delete_item    ${crawler_json_resput['response']}    update_time    create_time
    resp_should_be_equal    ${crawler_piped_response}    ${crawler_resp_2}
    ${crawler_find_list}    m_select    mc_info    crawlersizzle    ${crawler_json_res['response']['_id']}
    resp_should_be_equal    ${crawler_find_list[0]}    ${crawler_piped_response}
