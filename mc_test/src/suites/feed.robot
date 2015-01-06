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
    feed_get_check    ${feed_json_res}    ${feed_resp_1}    ${feed_resget}
    ${feed_resget2}    get    ${feed_url}
    ${feed_json_resget}    to_json    ${feed_resget.content}
    is_empty_list    ${feed_json_resget['errors']}
    resp_should_be_equal    ${feed_resget.status_code}    ${200}
    ${feed_piped_response}    delete_item    ${feed_json_resget['response']}
    ${feed_resp}    delete_item    ${feed_resp_1}    next_check_time    crawler_sizzle    crawler_sizzle_name
    resp_should_be_equal    ${feed_piped_response}    ${feed_resp_1}
