# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import high_availability_pb2 as high__availability__pb2


class HighAvailabilityManagerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.listMembers = channel.unary_unary(
                '/HighAvailabilityManager/listMembers',
                request_serializer=high__availability__pb2.ListMembersRequest.SerializeToString,
                response_deserializer=high__availability__pb2.ListMembersResponse.FromString,
                )
        self.notifyNewMember = channel.unary_unary(
                '/HighAvailabilityManager/notifyNewMember',
                request_serializer=high__availability__pb2.NotifyNewMemberRequest.SerializeToString,
                response_deserializer=high__availability__pb2.NotifyNewMemberResponse.FromString,
                )


class HighAvailabilityManagerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def listMembers(self, request, context):
        """List current living members.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def notifyNewMember(self, request, context):
        """Notify current members that there is a new member added.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HighAvailabilityManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'listMembers': grpc.unary_unary_rpc_method_handler(
                    servicer.listMembers,
                    request_deserializer=high__availability__pb2.ListMembersRequest.FromString,
                    response_serializer=high__availability__pb2.ListMembersResponse.SerializeToString,
            ),
            'notifyNewMember': grpc.unary_unary_rpc_method_handler(
                    servicer.notifyNewMember,
                    request_deserializer=high__availability__pb2.NotifyNewMemberRequest.FromString,
                    response_serializer=high__availability__pb2.NotifyNewMemberResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'HighAvailabilityManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HighAvailabilityManager(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def listMembers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HighAvailabilityManager/listMembers',
            high__availability__pb2.ListMembersRequest.SerializeToString,
            high__availability__pb2.ListMembersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def notifyNewMember(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HighAvailabilityManager/notifyNewMember',
            high__availability__pb2.NotifyNewMemberRequest.SerializeToString,
            high__availability__pb2.NotifyNewMemberResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)