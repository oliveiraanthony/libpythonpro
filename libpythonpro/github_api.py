from urllib3 import request


def buscar_avatar(usuario):
    """
    Busca o avatar de um usuario no github
    :param usuario: str com nome de usuário
    :return: str com o link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'

    resp = request.get(url)
    return resp.joson()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('oliveiraanthony'))
