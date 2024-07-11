from doipy.actions.doip import create
from doipy.constants import DOIPOperation, DOType, TypeIdentifier, ResponseStatus
from doipy.exceptions import InvalidRequestException, AuthenticationException
from doipy.models import FdoInput
from doipy.socket_utils import create_socket, send_message, finalize_segment, finalize_socket, read_response, \
    get_settings


def create_fdo(fdo_input: FdoInput):

    # get service settings
    target_id, ip, port = get_settings(fdo_input.fdo_service_ref)

    # create first message
    message_1 = {
        'targetId': f'{target_id}',
        'operationId': DOIPOperation.CREATE.value,
    }

    # check that either a username, password or token is provided
    authentication = fdo_input.authentication
    if 'username' not in authentication and 'clientId' not in authentication and 'token' not in authentication:
        raise AuthenticationException('Provide token, username or client_id')

    # provide correct set of authentication credentials
    authentication_message = {}
    if 'token' in authentication:
        authentication_message['authentication'] = {
            'token': authentication['token']
            }
    elif 'clientId' in authentication:
        if 'password' in authentication:
            authentication_message['clientId'] = authentication['client_id']
            authentication_message['authentication'] = {
                'password': authentication['password']
            }
        else:
            raise AuthenticationException('Provide password')
    else:
        if 'password' in authentication:
            authentication_message['authentication'] = {
                'username': authentication['username'],
                'password': authentication['password']
            }
        else:
            raise AuthenticationException('Provide password')
    message_1 = message_1 | authentication_message

    # create second message
    message_2 = {
        # TODO: type should not be part of the DOIP message, but of the adaptor (?)
        'type': DOType.FDO.value,
        'attributes': {
            'content': {
                'id': '',
                'name': 'FAIR Digital Object',
                # FDO_Profile_Ref: mandatory
                TypeIdentifier.FDO_PROFILE_REF.value: fdo_input.fdo_profile_ref,
                # FDO_Type_Ref: mandatory
                TypeIdentifier.FDO_TYPE_REF.value: fdo_input.fdo_type_ref
            }
        }
    }
    # FDO_Rights_Ref: optional
    if fdo_input.fdo_rights_ref:
        message_2['attributes']['content'][TypeIdentifier.FDO_RIGHTS_REF.value] = fdo_input.fdo_rights_ref
    # FDO_Genre_Ref: optional
    if fdo_input.fdo_genre_ref:
        message_2['attributes']['content'][TypeIdentifier.FDO_GENRE_REF.value] = fdo_input.fdo_genre_ref

    # create the data and metadata DOs
    if fdo_input.data_and_metadata:
        data_refs = []
        metadata_refs = []
        for item in fdo_input.data_and_metadata:
            # create the data do
            if item.data_bitsq or item.data_values:
                response = create(fdo_input.fdo_service_ref, DOType.DO.value, 'Data-DO', item.data_bitsq,
                                  item.data_values, authentication_message)
                data_ref = response[0]['output']['id']
                data_refs.append(data_ref)
            # create the metadata do
            if item.metadata_bitsq or item.metadata_values:
                response = create(fdo_input.fdo_service_ref, DOType.DO.value, 'Metadata-DO',
                                  item.metadata_bitsq, item.metadata_values, authentication_message)
                metadata_ref = response[0]['output']['id']
                metadata_refs.append(metadata_ref)
        if data_refs:
            message_2['attributes']['content'][TypeIdentifier.FDO_DATA_REFS.value] = data_refs
        if metadata_refs:
            message_2['attributes']['content'][TypeIdentifier.FDO_MD_REFS.value] = metadata_refs

        # create socket
        with create_socket(ip, port) as ssl_sock:

            # create the FDO
            send_message(message_1, ssl_sock)
            finalize_segment(ssl_sock)

            send_message(message_2, ssl_sock)
            finalize_segment(ssl_sock)
            finalize_socket(ssl_sock)

            response = read_response(ssl_sock)

        if response[0]['status'] == ResponseStatus.SUCCESS.value:
            return response
        raise InvalidRequestException(response)
