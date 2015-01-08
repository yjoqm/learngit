*** settings ***
Test Setup        init env    ${merchant_uri}    ${mc_info_uri}
Test Teardown     delete all session
Force Tags        mertype
Resource          res.robot
Variables         ../data/var.py

*** Test Cases ***
post one
    post_mertype_success    ${mertype_url}    ${mertype_req_1}    ${mertype_resp_1}

get
    ${mertype_res}    post_mertype_success    ${mertype_url}    ${mertype_req_1}    ${mertype_resp_1}
    ${mertype_json_res}    to_json    ${mertype_res.content}
    ${mertype_resget}    get    ${mertype_url+'1/'}
    ${mertype_json_resget}    to_json    ${mertype_resget.content}
    is_empty_list    ${mertype_json_resget['errors']}
    resp_should_be_equal    ${mertype_resget.status_code}    ${200}
    ${mertype_piped_respone}    delete_item    ${mertype_json_resget['response']}
    resp_should_be_equal    ${mertype_piped_respone}    ${mertype_resp_1}
    ${mertype_find_list}    m_select    mc_info    merchanttypes    ${mertype_json_res['response']['_id']}
    resp_should_be_equal    ${mertype_find_list[0]}    ${mertype_piped_respone}
    ${mertype_resget2}    get    ${mertype_url}
    resp_should_be_equal    ${mertype_resget2.status_code}    ${200}
    ${mertype_json_resget2}    to_json    ${mertype_resget2.content}
    ${mertype_piped_respone}    delete_item    ${mertype_json_resget2['response'][0]}
    resp_should_be_equal    ${mertype_piped_respone}    ${mertype_resp_1}
    ${mertype_find_list}    m_select    mc_info    merchanttypes    ${mertype_json_res['response']['_id']}
    resp_should_be_equal    ${mertype_find_list[0]}    ${mertype_piped_respone}

put
    ${mertype_res}    post_mertype_success    ${mertype_url}    ${mertype_req_1}    ${mertype_resp_1}
    ${mertype_json_res}    to_json    ${mertype_res.content}
    ${mertype_resput}    put    ${mertype_url+'1/'}    ${mertype_req_2}
    ${mertype_json_resput}    to_json    ${mertype_resput.content}
    is_empty_list    ${mertype_json_resput['errors']}
    resp_should_be_equal    ${mertype_resput.status_code}    ${200}
    ${mertype_piped_respone}    delete_item    ${mertype_json_resput['response']}
    resp_should_be_equal    ${mertype_piped_respone}    ${mertype_resp_2}
    ${mertype_find_list}    m_select    mc_info    merchanttypes    ${mertype_json_res['response']['_id']}
    resp_should_be_equal    ${mertype_find_list[0]}    ${mertype_piped_respone}
