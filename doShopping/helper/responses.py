from rest_framework.response import Response as DRFResponse
from .encoder import JsonSerializable
from .error_codes import error

class Response:
    """
    Response format for the APIs
    """

    @staticmethod
    def success(data=None, message="Operation completed!", status=200, **kwargs):
        """
        Success response
        @param data:
        @param kwargs:
        @return:
        """
        return DRFResponse(
            data=dict(
                response_code=200,
                response_message=message,
                data=JsonSerializable.format(data),
                success=True,
                error_code=status,
                error_message=error.get(str(status), ""),
                **kwargs
            ),
            status=status
        )

    @staticmethod
    def server_error(data=None, message="Internal server error", status=500, **kwargs):
        """
        Internal server error response
        @param data:
        @param kwargs:
        @return:
        """
        return DRFResponse(
            data=dict(
                response_code=500,
                response_message=message,
                data=JsonSerializable.format(data),
                success=False,
                error_code=status,
                error_message=error.get(str(status), ""),
                **kwargs
            ),
            status=status
        )

    @staticmethod
    def unauthorized(data=None, message="Unauthorized", status=401, **kwargs):
        """
        Unauthorized response if authentication failed
        @param data:
        @param kwargs:
        @return:
        """
        return DRFResponse(
            data=dict(
                response_code=401,
                response_message=message,
                data=JsonSerializable.format(data),
                success=False,
                error_code=status,
                error_message=error.get(str(status), ""),
                **kwargs
            ),
            status=status
        )

    @staticmethod
    def bad_request(data=None, message="Bad Request!", status=400, **kwargs):
        """
        Bad request response if not allowed functionality
        @param data:
        @param status:
        @param kwargs:
        @return:
        """
        return DRFResponse(
            data=dict(
                response_code=400,
                response_message=message,
                data=JsonSerializable.format(data),
                success=False,
                error_code=status,
                error_message=error.get(str(status), ""),
                **kwargs
            ),
            status=status
        )

    @staticmethod
    def forbidden(data=None, message="Unauthorized", status=403, **kwargs):
        """
        Forbidden error response if not allowed to access
        @param data:
        @param kwargs:
        @return:
        """
        return DRFResponse(
            data=dict(
                response_code=403,
                response_message=message,
                data=JsonSerializable.format(data),
                success=False,
                error_code=status,
                error_message=error.get(str(status), ""),
                **kwargs
            ),
            status=status
        )

    @staticmethod
    def not_found(data=None, message="Not found", status=404, **kwargs):
        """
        Not found error response if view does not exists or record does not exists
        @param data:
        @param kwargs:
        @return:
        """
        return DRFResponse(
            data=dict(
                response_code=404,
                response_message=message,
                data=JsonSerializable.format(data),
                success=False,
                error_code=status,
                error_message=error.get(str(status), ""),
                **kwargs
            ),
            status=status
        )

    @staticmethod
    def upgrade_required(data=None, message="Upgrade required", status=426, **kwargs):
        """
        Upgrade required response if api version not supported
        @param data:
        @param status:
        @param kwargs:
        @return:
        """
        return DRFResponse(
            data=dict(
                response_code=426,
                response_message=message,
                data=JsonSerializable.format(data),
                success=False,
                error_code=status,
                error_message=error.get(str(status), ""),
                **kwargs
            ),
            status=status
        )

    @staticmethod
    def method_not_allowed(data=None, message="Method not Allowed", status=405, **kwargs):
        """
        Upgrade required response if api version not supported
        @param data:
        @param status:
        @param kwargs:
        @return:
        """
        return DRFResponse(
            data=dict(
                response_code=405,
                response_message=message,
                data=JsonSerializable.format(data),
                success=False,
                error_code=status,
                error_message=error.get(str(status), ""),
                **kwargs
            ),
            status=status
        )

    @staticmethod
    def resource_gone(data=None, message="Gone", status=410, **kwargs):
        """
        Upgrade required response if api version not supported
        @param data:
        @param status:
        @param kwargs:
        @return:
        """
        return DRFResponse(
            data=dict(
                response_code=410,
                response_message=message,
                data=JsonSerializable.format(data),
                success=False,
                error_code=status,
                error_message=error.get(str(status), ""),
                **kwargs
            ),
            status=status
        )

    @staticmethod
    def resource_deprecated(data=None, message="Deprecated API", status=299, **kwargs):
        """
        Upgrade required response if api version not supported
        @param data:
        @param status:
        @param kwargs:
        @return:
        """
        return DRFResponse(
            data=dict(
                response_code=299,
                response_message=message,
                data=JsonSerializable.format(data),
                success=False,
                error_code=status,
                error_message=error.get(str(status), ""),
                **kwargs
            ),
            status=status
        )

    @staticmethod
    def validation_error(data=None, message="Mandatory fields", status=422, **kwargs):
        """
        Validation Error if any mandatory field is  not provided
        :param data:
        :param kwargs:
        :return:
        """
        return DRFResponse(
            data=dict(
                response_code=422,
                response_message=message,
                data=JsonSerializable.format(data),
                success=False,
                error_code=status,
                error_message=error.get(str(status), ""),
                **kwargs
            ),
            status=status
        )
