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
    merchant_get_check    ${merchant_json_res}    ${merchant_resp_1}    ${merchant_resget}
    ${merchant__resget2}    get    ${merchant_url+'?advertiser_id=1&offline=False'}
    resp_should_be_equal    ${merchant__resget2.status_code}    ${200}
