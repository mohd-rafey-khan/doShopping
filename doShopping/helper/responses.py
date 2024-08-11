from .encoder import JsonSerializable
from .error_codes import error


class Response:
    """
    Response format for the APIs
    """

    @staticmethod
    def success(data=None, message="Operation completed!", status=None, **kwargs):
        """
        Success response
        @param data:
        @param kwargs:
        @return:
        """
        return dict(
            response_code=200,
            response_message=message,
            data=JsonSerializable.format(data),
            success=True,
            error_code=status,
            error_message=error.get(str(status), ""),
            **kwargs
        ), 200

    @staticmethod
    def server_error(data=None, message="Internal server error", status=None, **kwargs):
        """
        Internal server error response
        @param data:
        @param kwargs:
        @return:
        """
        return dict(
            response_code=500,
            response_message=message,
            data=JsonSerializable.format(data),
            success=False,
            error_code=status,
            error_message=error.get(str(status), ""),
            **kwargs
        ), 500

    @staticmethod
    def unauthorized(data=None, message="Unauthorized", status=None, **kwargs):
        """
        Unauthorized response if authentication failed
        @param data:
        @param kwargs:
        @return:
        """
        return dict(
            response_code=401,
            response_message=message,
            data=JsonSerializable.format(data),
            success=False,
            error_code=status,
            error_message=error.get(str(status), ""),
            **kwargs
        ), 401

    @staticmethod
    def bad_request(data=None, message="Bad Request!", status=None, **kwargs):
        """
        Bad request response if not allowed functionality
        @param data:
        @param status:
        @param kwargs:
        @return:
        """
        return dict(
            response_code=400,
            response_message=message,
            data=JsonSerializable.format(data),
            success=False,
            error_code=status,
            error_message=error.get(str(status), ""),
            **kwargs
        ), 400

    @staticmethod
    def forbidden(data=None, message="Unauthorized", status=None, **kwargs):
        """
        Forbidden error response if not allowed to access
        @param data:
        @param kwargs:
        @return:
        """
        return dict(
            response_code=403,
            response_message=message,
            data=JsonSerializable.format(data),
            success=False,
            error_code=status,
            error_message=error.get(str(status), ""),
            **kwargs
        ), 403

    @staticmethod
    def not_found(data=None, message="Not found", status=None, **kwargs):
        """
        Not found error response if view does not exists or record does not exists
        @param data:
        @param kwargs:
        @return:
        """
        return dict(
            response_code=404,
            response_message=message,
            data=JsonSerializable.format(data),
            success=False,
            error_code=status,
            error_message=error.get(str(status), ""),
            **kwargs
        ), 404

    @staticmethod
    def upgrade_required(data=None, message="Upgrade required", status=None, **kwargs):
        """
        Upgrade required response if api version not supported
        @param data:
        @param status:
        @param kwargs:
        @return:
        """
        return dict(
            response_code=426,
            response_message=message,
            data=JsonSerializable.format(data),
            success=False,
            error_code=status,
            error_message=error.get(str(status), ""),
            **kwargs
        ), 426

    @staticmethod
    def method_not_allowed(data=None, message="Method not Allowed", status=None, **kwargs):
        """
        Upgrade required response if api version not supported
        @param data:
        @param status:
        @param kwargs:
        @return:
        """
        return dict(
            response_code=405,
            response_message=message,
            data=JsonSerializable.format(data),
            success=False,
            error_code=status,
            error_message=error.get(str(status), ""),
            **kwargs
        ), 405

    @staticmethod
    def resource_gone(data=None, message="Gone", status=None, **kwargs):
        """
        Upgrade required response if api version not supported
        @param data:
        @param status:
        @param kwargs:
        @return:
        """
        return dict(
            response_code=410,
            response_message=message,
            data=JsonSerializable.format(data),
            success=False,
            error_code=status,
            error_message=error.get(str(status), ""),
            **kwargs
        ), 410

    @staticmethod
    def resource_deprecated(data=None, message="Deprecated API", status=None, **kwargs):
        """
        Upgrade required response if api version not supported
        @param data:
        @param status:
        @param kwargs:
        @return:
        """
        return dict(
            response_code=299,
            response_message=message,
            data=JsonSerializable.format(data),
            success=False,
            error_code=status,
            error_message=error.get(str(status), ""),
            **kwargs
        ), 299

    @staticmethod
    def validation_error(data=None, message="Mandatory fields", status=None, **kwargs):
        """
        Validation Error if any mandatory field is  not provided
        :param data:
        :param kwargs:
        :return:
        """
        return dict(
            response_code=422,
            response_message=message,
            data=JsonSerializable.format(data),
            success=False,
            error_code=status,
            error_message=error.get(str(status), ""),
            **kwargs
        ), 422
