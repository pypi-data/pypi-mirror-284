from afeng_tools.encryption_tool import hashlib_tools

from afeng_tools.web_tool import response_tools
from afeng_tools.web_tool.core.web_common_models import ResponseModel
from afeng_tools.weixin_min_program import weixin_mp_tools, weixin_mp_settings
from afeng_tools.weixin_min_program.core.weixin_mp_api_service import request_jscode2session
from afeng_tools.weixin_min_program.core.weixin_mp_models import WxUserProfile, WxUserBasicInfo
from afeng_tools.weixin_min_program.model.weixin_mp_enums import WeixinMpConfigKeyEnum
from afeng_tools.weixin_min_program.model.weixin_mp_open_models import WxMpLoginInfo, WxMpUserInfo, WxMpUserBasicInfo

# 缓存
__LOCAL_CACHE__ = dict()


def login_code2Session(mp_app_id: str, js_code: str) -> ResponseModel:
    result = request_jscode2session(mp_app_id, js_code)
    if result.errcode == 40029:
        return response_tools.create_json_response_data(error_no=429, message='js_code无效')
    elif result.errcode == 40226:
        return response_tools.create_json_response_data(error_no=4226, message='高风险等级用户, 无法登录小程序')
    elif result.errcode is None or result.errcode == 0:
        login_info = WxMpLoginInfo(
            mp_app_id=mp_app_id,
            union_id=result.unionid,
            open_id=result.openid,
            session_key=result.session_key,
        )
        login_callback = weixin_mp_settings.get_config(mp_app_id, WeixinMpConfigKeyEnum.mp_login_callback)
        if login_callback:
            token = login_callback(login_info)
        else:
            token = hashlib_tools.calc_md5(login_info.mp_app_id + login_info.open_id + login_info.union_id)
        __LOCAL_CACHE__[token] = login_info
        return response_tools.create_json_response_data(data=token)
    else:
        return login_code2Session(mp_app_id, js_code)


def decrypt_userinfo(mp_app_id: str, token: str, user_profile: WxUserProfile) -> ResponseModel:
    get_login_info_callback = weixin_mp_settings.get_config(mp_app_id, WeixinMpConfigKeyEnum.mp_get_login_info_callback)
    if get_login_info_callback:
        login_info = get_login_info_callback(token)
    else:
        login_info = __LOCAL_CACHE__.get(token)
    session_key = login_info.session_key
    if user_profile.signature == weixin_mp_tools.calc_signature(session_key=session_key, raw_data=user_profile.rawData):
        user_data = weixin_mp_tools.decrypt_data(app_id=mp_app_id,
                                                 session_key=session_key,
                                                 encrypted_data=user_profile.encryptedData, iv_value=user_profile.iv)
        # 保存用户信息
        save_userinfo_callback = weixin_mp_settings.get_config(mp_app_id,
                                                               WeixinMpConfigKeyEnum.mp_save_userinfo_callback)
        if save_userinfo_callback:
            user_data = save_userinfo_callback(WxMpUserInfo(
                token=token,
                nick_name=user_data.get('nickName'),
                avatar_url=user_data.get('avatarUrl'),
                city=user_data.get('city'),
                country=user_data.get('country'),
                province=user_data.get('province'),
                gender=user_data.get('gender'),
                language=user_data.get('language'),
            ))
        return response_tools.create_json_response_data(data=user_data)
    return response_tools.create_json_response_data(error_no=401, message='认证失败')


def save_basic_user(mp_app_id: str, token: str, user_basic_info: WxUserBasicInfo) -> ResponseModel:
    # 保存用户基础信息
    save_user_basic_info_callback = weixin_mp_settings.get_config(mp_app_id,
                                                                  WeixinMpConfigKeyEnum.mp_save_user_basic_info_callback)
    if save_user_basic_info_callback:
        user_data = save_user_basic_info_callback(WxMpUserBasicInfo(
            token=token,
            nick_name=user_basic_info.nickName,
            avatar_url=user_basic_info.avatarUrl,
        ))
        return response_tools.create_json_response_data(data=user_data)
    return response_tools.create_json_response_data(error_no=401, message='保存用户基础信息失败')