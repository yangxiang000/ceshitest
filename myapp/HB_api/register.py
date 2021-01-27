from django.http import JsonResponse, HttpResponse
from myapp import views, mysql
import json


def register(request):
    verification = views.post(request)
    date = json.loads(request.POST.get('date', 0))
    if not verification:
        expected_dict = {'expectedTypeRange':[dict],'expectedDict':{
            "orderNo": {'expectedTypeRange': [str]},
            "merNo": {'expectedTypeRange': [str]},
            "merName": {'expectedTypeRange': [str]},
            "merType": {'expectedTypeRange': [str]},
            "certType": {'expectedTypeRange': [str]},
            "certPicturePath": {'expectedTypeRange': [str]},
            "certNo": {'expectedTypeRange': [str]},
            "certNm": {'expectedTypeRange': [str]},
            "proviceCode": {'expectedTypeRange': [str]},
            "cityCode": {'expectedTypeRange': [str]},
            "areaCode": {'expectedTypeRange': [str]},
            "address": {'expectedTypeRange': [str]},
            "legalPersonName": {'expectedTypeRange': [str]},
            "legalPersonId": {'expectedTypeRange': [str]},
            "legalPersonBackPicturePath": {'expectedTypeRange': [str]},
            "legalPersonFrontPicturePath": {'expectedTypeRange': [str]},
            "alipayLogonId": {'expectedTypeRange': [str]},
            "alipayName": {'expectedTypeRange': [str]},
            "contactPersonName": {'expectedTypeRange': [str]},
            "contactPersonMobile": {'expectedTypeRange': [str]},
            "storeId": {'expectedTypeRange': [str]},
            "storeName": {'expectedTypeRange': [str]},
            "storePicture": {'expectedTypeRange': [str]}}
        }
        if views.is_data_valid(expected_dict,date):
            insret = "insert HB_register(" + ",".join(list(date.keys())) + ") values('" + "','".join(
                list(date.values())) + "');"
            mysql.sql(insret)
            return JsonResponse({'rspCd': 200, 'rspInf': '交易成功'})
        else:
            return JsonResponse({'rspCd': 500, 'rspInf': '数据格式错误'})
    else:
        return HttpResponse(verification)
