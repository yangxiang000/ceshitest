from django.shortcuts import render
from django.http import JsonResponse


def index(requset):
    return render(requset, 'index.html')


# 判断 pre_validate_data 符不符合给定的 expected_structure
def is_data_valid(expected_structure, pre_validate_data):
    # 结构字典基础校验
    if not isinstance(expected_structure, dict) or not expected_structure:
        raise TypeError('expected_structure must be valid dict')
    # 获取结构字典中固定键的值
    expected_type_range = expected_structure.get('expectedTypeRange')
    expected_value_range = expected_structure.get('expectedValueRange') \
        if expected_structure.get('expectedValueRange') else []
    expected_dict = expected_structure.get('expectedDict') if expected_structure.get('expectedDict') else {}
    # 基础校验
    if not all(map(lambda x: isinstance(x, type), expected_type_range)) \
            or not isinstance(expected_value_range, list) or not isinstance(expected_dict, dict):
        raise TypeError('expectedType、 expectedRange、 expectedDict  must be type_list、 list、dict ')
    # 数据类型不在期待值中则返回 False
    if not type(pre_validate_data) in expected_type_range:
        return False
    # 如果待验证数据类型为 list ，则将每一个元素与期待值进行校验
    if type(pre_validate_data) == list:
        for list_piece in pre_validate_data:
            if expected_value_range and not any(map(is_data_valid, expected_value_range,
                                                    x2list(len(expected_value_range), list_piece))):
                return False
    # 如果待校验数据类型为 dict，则将每一个键的值与期待值进行校验
    elif type(pre_validate_data) == dict:
        for k, v in expected_dict.items():
            if k not in pre_validate_data or not is_data_valid(v, pre_validate_data[k]):
                return False
    return True


def x2list(expected_len, raw_material):
    new_list = list()
    for i in range(expected_len):
        new_list.append(raw_material)
    return new_list


# post字典数据结构检验示例
# test_data = [{"baseText": "", "comparedText": "", "targetSimilarity": {'test':'1.9'}},
#            {"baseText": "", "comparedText": "", "targetSimilarity": {'test':1.9}}]
# expected_dict = {
#                     "baseText": {'expectedTypeRange': [str]}，
#                     "comparedText": {'expectedTypeRange': [str]},
#                     "targetSimilarity": {
#                         'expectedTypeRange': [dict],
#                         'expectedDict': {
#                             'test':{
#                                     'expectedTypeRange': [int, float]
#                                 }
#                             }
#                         }
#                 }
#
# expected_structure = {
#                        'expectedTypeRange': [list],
#                        'expectedValueRange':
#                           [
#                              {'expectedTypeRange':[dict], 'expectedDict':expect_dict}
#                           ]
#                      }

# 接口函数
def post(request, fromList=[]):
    if request.method == 'POST':  # 当提交表单时
        # 判断是否传参
        if request.POST:
            for value in fromList:
                if request.POST.get(value, 0):
                    continue
                else:
                    return JsonResponse({'rspCd': 500, 'rspInf': '{}参数未传'.format(value)})
            return False
        else:
            return JsonResponse({'rspCd': 500, 'rspInf': '参数未传'})
    else:
        return JsonResponse({'rspCd': 500, 'rspInf': '请求方法错误'})
