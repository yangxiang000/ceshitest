from django.http import JsonResponse, HttpResponse
from myapp import views, mysql
import json


def pay_status(request):
    verification = views.post(request)
    date = json.loads(request.POST.get('date', 0))
    if not verification:
        expected_dict = {'expectedTypeRange': [dict], 'expectedDict': {
            "brwOrdNo": {'expectedTypeRange': [str]},
            "brwOrdDt": {'expectedTypeRange': [str]},
            "ordTyp": {'expectedTypeRange': [str]},
            "appId": {'expectedTypeRange': [str]},
            "appNm": {'expectedTypeRange': [str]}
        }}
        # 验证接口数据格式与数据值是否正确
        if views.is_data_valid(expected_dict, date):
            insret = "insert HB_pay_status(" + ",".join(list(date.keys())) + ") values('" + "','".join(
                list(date.values())) + "');"
            print(insret)
            mysql.sql(insret)
            return JsonResponse({'rspCd': 200, 'rspInf': '交易成功'})
        else:
            return JsonResponse({'rspCd': 500, 'rspInf': '数据格式错误'})
    else:
        return HttpResponse(verification)
