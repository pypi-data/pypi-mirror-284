import uuid
from pathlib import Path

from doipy.exceptions import InvalidRequestException
from doipy.constants import DOIPOperation, ResponseStatus
from doipy.socket_utils import create_socket, send_message, finalize_socket, finalize_segment, read_response, \
    get_settings


def hello(service: str):
    # get service settings
    target_id, ip, port = get_settings(service)
    # create request message
    message = {
        'targetId': f'{target_id}',
        'operationId': DOIPOperation.HELLO.value
    }
    # send request and return response
    with create_socket(ip, port) as ssl_sock:
        send_message(message, ssl_sock)
        finalize_segment(ssl_sock)
        finalize_socket(ssl_sock)
        response = read_response(ssl_sock)
        return response


def list_operations(service):
    # get service settings
    target_id, ip, port = get_settings(service)
    # create request message
    message = {
        'targetId': f'{target_id}',
        'operationId': DOIPOperation.LIST_OPERATION.value
    }

    # send request and read response
    with create_socket(ip, port) as ssl_sock:
        send_message(message, ssl_sock)
        finalize_segment(ssl_sock)
        finalize_socket(ssl_sock)
        response = read_response(ssl_sock)
        return response


def create(service: str, do_type: str, do_name: str, bitsq: Path, metadata: dict, authentication_message: dict):

    # get service settings
    target_id, ip, port = get_settings(service)

    # create first message
    message_1 = {
        'targetId': f'{target_id}',
        'operationId': DOIPOperation.CREATE.value
    }
    message_1 = message_1 | authentication_message

    # create second message: DO of type document in Cordra for the file which is added
    message_2 = {
        'type': do_type,
        'attributes': {
            'content': {
                'id': '',
                'name': do_name
            }
        }
    }

    # add metadata to DO
    if metadata:
        message_2['attributes']['content'] = message_2['attributes']['content'] | metadata

    with create_socket(ip, port) as ssl_sock:

        send_message(message_1, ssl_sock)
        finalize_segment(ssl_sock)

        if bitsq:
            # add information on files to DO
            filename = bitsq.name
            my_uuid = str(uuid.uuid4())
            message_2['elements'] = [
                {
                    'id': my_uuid,
                    'type': 'text/plain',
                    'attributes': {
                        'filename': filename
                    }
                }
            ]
            # third message
            message_3 = {
                'id': my_uuid
            }
            send_message(message_2, ssl_sock)
            finalize_segment(ssl_sock)

            send_message(message_3, ssl_sock)
            finalize_segment(ssl_sock)

            # send content of files
            buffer_size = 1024
            with open(bitsq, 'rb') as f:
                while bytes_read := f.read(buffer_size):
                    ssl_sock.sendall(bytes_read)
                finalize_segment(ssl_sock)

        finalize_socket(ssl_sock)

        response = read_response(ssl_sock)
    if response[0]['status'] == ResponseStatus.SUCCESS.value:
        return response
    raise InvalidRequestException(response)


def update(service: str, client_id: str, password: str, do_type: str):
    # TODO fix message

    # get service settings
    target_id, ip, port = get_settings(service)

    with create_socket(ip, port) as ssl_sock:
        message = {
            'clientId': client_id,
            'targetId': target_id,
            'operationId': DOIPOperation.UPDATE.value,
            'authentication': {
                'password': password
            }
        }
        send_message(message, ssl_sock)
        string1 = f'https://cordra.testbed.pid.gwdg.de/objects/{target_id}?payload=file'
        string2 = f'https://cordra.testbed.pid.gwdg.de/objects/{target_id}'
        message = {
            'type': do_type,
            'attributes': {
                'content': {
                    'id': '',
                    'Payload': string1,
                    'Metadata': string2
                }
            }
        }
        send_message(message, ssl_sock)
        finalize_socket(ssl_sock)
        response = read_response(ssl_sock)
        return response


def search(service: str, query: str = 'type:Document', username: str = None, password: str = None):
    # TODO fix message

    # get service settings
    target_id, ip, port = get_settings(service)

    message = {
        'targetId': f'{target_id}',
        'operationId': DOIPOperation.SEARCH.value,
        'attributes': {
            'query': query
        }
    }
    if username and password:
        message['authentication'] = {
            'username': username,
            'password': password
        }

    with create_socket(ip, port) as ssl_sock:
        send_message(message, ssl_sock)
        finalize_socket(ssl_sock)
        response = read_response(ssl_sock)
        return response


def retrieve(service: str, do: str):
    # get service settings
    _, ip, port = get_settings(service)
    # create message
    message = {
        'targetId': do,
        'operationId': DOIPOperation.RETRIEVE.value
    }
    # send request and return response
    with create_socket(ip, port) as ssl_sock:
        send_message(message, ssl_sock)
        finalize_segment(ssl_sock)
        finalize_socket(ssl_sock)
        response = read_response(ssl_sock)
        return response


# delete
