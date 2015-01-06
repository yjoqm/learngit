*** settings ***
Test Setup        init env    ${merchant_uri}    ${mc_info_uri}
Test Teardown     delete all session
Force Tags        attr
Resource          res.robot
Variables         ../data/var.py

*** Test Cases ***
post one
    post_attr_success    ${attr_url}    ${attr_req_1}    ${attr_resp_1}

get
    ${attr_res}    post_attr_success    ${attr_url}    ${attr_req_1}    ${attr_resp_1}
    ${attr_json_res}    to_json    ${attr_res.content}
    ${attr_resget}    get    ${attr_url+'${attr_json_res['response']['_id']}/'}
    attr_get_check    ${attr_json_res}    ${attr_resp_1}    ${attr_resget}
    ${attr_resget2}    get    ${attr_url+'?advertiser_id=1'}
    resp_should_be_equal    ${attr_resget2.status_code}    ${200}
    ${attr_json_resget2}    to_json    ${attr_resget2.content}
    is_empty_list    ${attr_json_resget2['errors']}
    resp_should_be_equal    ${attr_resget2.status_code}    ${200}
    ${attr_piped_response}    delete_item    ${attr_json_resget2['response'][0]}    status    name
    ${attr_resp}    delete_item    ${attr_resp_1}    name
    resp_should_be_equal    ${attr_piped_response}    ${attr_resp}
