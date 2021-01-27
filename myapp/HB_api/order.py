from django.http import JsonResponse, HttpResponse
from myapp import views, mysql
import json


def create_order(request):
    verification = views.post(request)
    date = json.loads(request.POST.get('date', 0))
    if not verification:
        expected_dict = {'expectedTypeRange': [dict], 'expectedDict': {
            "brwOrdNo": {'expectedTypeRange': [str]},
            "merchId": {'expectedTypeRange': [str]},
            "brwOrdDt": {'expectedTypeRange': [str]},
            "ordType": {'expectedTypeRange': [str]},
            "payType": {'expectedTypeRange': [str]},
            "merNo": {'expectedTypeRange': [str]},
            "depId": {'expectedTypeRange': [str]},
            "depNm": {'expectedTypeRange': [str]},
            "productNm": {'expectedTypeRange': [str]},
            "productId": {'expectedTypeRange': [str]},
            "payAmt": {'expectedTypeRange': [str]},
            "loanAmt": {'expectedTypeRange': [str]},
            "loanMonth": {'expectedTypeRange': [str]},
            "mblNo": {'expectedTypeRange': [str]},
            "cusNm": {'expectedTypeRange': [str]},
            "usrProv": {'expectedTypeRange': [str]},
            "mngModel": {'expectedTypeRange': [str]},
            "busTyp": {'expectedTypeRange': [str]},
            "depProvNo": {'expectedTypeRange': [str]},
            "oprId": {'expectedTypeRange': [str]},
            "oprMblNo": {'expectedTypeRange': [str]},
            "rpyDay": {'expectedTypeRange': [str]},
            "appId": {'expectedTypeRange': [str]},
            "appNm": {'expectedTypeRange': [str]},
            "pkgTyp": {'expectedTypeRange': [str]},
            "provinceRate": {'expectedTypeRange': [str]},
            "bonusAmount": {'expectedTypeRange': [str]},
            "needPayFlag": {'expectedTypeRange': [str]}
        }}
        # 验证接口数据格式与数据值是否正确
        if views.is_data_valid(expected_dict, date):
            insret = "insert HB_order(" + ",".join(list(date.keys())) + ") values('" + "','".join(
                list(date.values())) + "');"
            print(insret)
            mysql.sql(insret)
            return JsonResponse({'rspCd': 200, 'rspInf': '交易成功'})
        else:
            return JsonResponse({'rspCd': 500, 'rspInf': '数据格式错误'})
    else:
        return HttpResponse(verification)
