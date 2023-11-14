import pytest


def test_root(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.json()
    assert data == {"Hello": "World"}
    assert isinstance(data, dict)


@pytest.mark.parametrize('item_id, q', [(1, '3'), (2, '4'), (3, None)])
def test_items(client, item_id, q):
    response = client.get(f'/items/{item_id}', params={'q': q})
    assert response.status_code == 200
    data = response.json()
    assert data == {"item_id": item_id, "q": q if q is not None else ''}
    assert isinstance(data, dict)
