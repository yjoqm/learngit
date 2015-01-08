*** settings ***
Test Setup        init env    ${merchant_uri}    ${mc_info_uri}
Test Teardown     delete all session
Force Tags        merchant
Resource          res.robot
Variables         ../data/var.py

*** Test Cases ***
post one
    post_merchant_success    ${merchant_url}    ${merchant_req_1}    ${merchant_resp_1}

get
    ${merchant_res}    post_merchant_success    ${merchant_url}    ${merchant_req_1}    ${merchant_resp_1}
    ${merchant_json_res}    to_json    ${merchant_res.content}
    ${merchant_resget}    get    ${merchant_url+'1/?advertiser_id=1&offline=False'}
    ${merchant_json_resget}    to_json    ${merchant_resget.content}
    is_empty_list    ${merchant_json_resget['errors']}
    resp_should_be_equal    ${merchant_resget.status_code}    ${200}
    ${merchant_piped_respone}    delete_item    ${merchant_json_resget['response']}    hash    64strid
    resp_should_be_equal    ${merchant_piped_respone}    ${merchant_resp_1}
    ${merchant_find_list}    mer_select    online    1    ${merchant_json_res['response']['_id']}
    ${merchant_find_list}    delete_item    ${merchant_find_list[0]}    hash
    resp_should_be_equal    ${merchant_find_list}    ${merchant_piped_respone}
    ${merchant_resget2}    get    ${merchant_url+'?advertiser_id=1&offline=False'}
    ${merchant_json_resget2}    to_json    ${merchant_resget2.content}
    resp_should_be_equal    ${merchant_resget2.status_code}    ${200}
    ${merchant_piped_respone}    delete_item    ${merchant_json_resget2['response'][0]}    hash    64strid
    resp_should_be_equal    ${merchant_piped_respone}    ${merchant_resp_1}
    ${merchant_find_list}    mer_select    online    1    ${merchant_json_res['response']['_id']}
    ${merchant_find_list}    delete_item    ${merchant_find_list[0]}    hash
    resp_should_be_equal    ${merchant_find_list}    ${merchant_piped_respone}

put
    ${merchant_res}    post_merchant_success    ${merchant_url}    ${merchant_req_1}    ${merchant_resp_1}
    ${merchant_json_res}    to_json    ${merchant_res.content}
    ${merchant_resput}    mer_put    ${merchant_url+'${merchant_json_res['response']['_id']}/'}    ${merchant_req_2}
    ${merchant_json_resput}    to_json    ${merchant_resput.content}
    is_empty_list    ${merchant_json_resput['errors']}
    resp_should_be_equal    ${merchant_resput.status_code}    ${200}
    ${merchant_piped_respone}    delete_item    ${merchant_json_resput['response']}    hash    64strid    validate_msg
    resp_should_be_equal    ${merchant_piped_respone}    ${merchant_resp_2}
    ${merchant_find_list}    mer_select    online    1    ${merchant_json_res['response']['_id']}
    ${merchant_find_list}    delete_item    ${merchant_find_list[0]}    hash    validate_msg
    resp_should_be_equal    ${merchant_find_list}    ${merchant_piped_respone}
