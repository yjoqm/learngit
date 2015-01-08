*** settings ***
Test Setup        init env    ${merchant_uri}    ${mc_info_uri}
Test Teardown     delete all session
Force Tags        xslt
Resource          res.robot
Variables         ../data/var.py

*** Test Cases ***
post two
    post_xslt_success    ${xslt_url}    ${xslt_req_1}    ${xslt_resp_1}

get
    ${xslt_res}    post_xslt_success    ${xslt_url}    ${xslt_req_1}    ${xslt_resp_1}
    ${xslt_json_res}    to_json    ${xslt_res.content}
    ${xslt_resget}    get    ${xslt_url+'1/'}
    ${xslt_json_resget}    to_json    ${xslt_resget.content}
    is_empty_list    ${xslt_json_resget['errors']}
    resp_should_be_equal    ${xslt_resget.status_code}    ${200}
    ${xslt_piped_respone}    delete_item    ${xslt_json_resget['response']}
    resp_should_be_equal    ${xslt_piped_respone}    ${xslt_resp_1}
    ${xslt_find_list}    m_select    mc_info    xslts    ${xslt_json_res['response']['_id']}
    resp_should_be_equal    ${xslt_find_list[0]}    ${xslt_piped_respone}
    ${xslt_resget2}    get    ${xslt_url}
    ${xslt_json_resget2}    to_json    ${xslt_resget2.content}
    resp_should_be_equal    ${xslt_resget2.status_code}    ${200}
    ${xslt_piped_respone}    delete_item    ${xslt_json_resget2['response'][0]}
    resp_should_be_equal    ${xslt_piped_respone}    ${xslt_resp_1}
    ${xslt_find_list}    m_select    mc_info    xslts    ${xslt_json_res['response']['_id']}
    resp_should_be_equal    ${xslt_find_list[0]}    ${xslt_piped_respone}

delete
    ${xslt_res}    post_xslt_success    ${xslt_url}    ${xslt_req_1}    ${xslt_resp_1}
    ${xslt_json_res}    to_json    ${xslt_res.content}
    ${xslt_resdel}    delete    ${xslt_url+'${xslt_json_res['response']['_id']}/'}
    ${xslt_json_resdel}    to_json    ${xslt_resdel.content}
    resp_should_be_equal    ${xslt_resdel.status_code}    ${200}
    is_empty_list    ${xslt_json_resdel['errors']}
    ${xslt_find_list}    m_select    mc_info    xslts    ${xslt_json_res['response']['_id']}
    ${xslt_find_listlen}    Evaluate    len(${xslt_find_list})
    Should Be Equal As Numbers    ${xslt_find_listlen}    0

put
    ${xslt_res}    post_xslt_success    ${xslt_url}    ${xslt_req_1}    ${xslt_resp_1}
    ${xslt_json_res}    to_json    ${xslt_res.content}
    ${xslt_resput}    put    ${xslt_url+'${xslt_json_res['response']['_id']}/'}    ${xslt_req_2}
    ${xslt_json_resput}    to_json    ${xslt_resput.content}
    is_empty_list    ${xslt_json_resput['errors']}
    resp_should_be_equal    ${xslt_resput.status_code}    ${200}
    ${xslt_piped_respone}    delete_item    ${xslt_json_resput['response']}
    resp_should_be_equal    ${xslt_piped_respone}    ${xslt_resp_2}
    ${xslt_find_list}    m_select    mc_info    xslts    ${xslt_json_res['response']['_id']}
    resp_should_be_equal    ${xslt_find_list[0]}    ${xslt_piped_respone}
