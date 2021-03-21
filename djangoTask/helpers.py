from rest_framework.response import Response


def SuccessfulResponse(result=None, status=200, code=0):
    return Response(
        {
            'code': code,
            'message': None,
            'result': result
        },
        status=status)


class ERROR:
    ORDER_DOES_NOT_EXIST = Response(
        {
            'code': 4041,
            'message': 'Order does not exist',
            'result': None
        },
        status=404
    )

    GOOD_DOES_NOT_EXIST = Response(
        {
            'code': 4042,
            'message': 'Good does not exist',
            'result': None
        },
        status=404
    )
