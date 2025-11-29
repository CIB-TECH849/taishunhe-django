from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# 綠界 / 其他金流 callback 可在這裡處理
@csrf_exempt
def payment_callback(request):
    # TODO: 驗證金流回傳、更新訂單狀態
    return HttpResponse("OK")
