import pytest
from httpx import AsyncClient
from app.main import app

client = AsyncClient()


@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello Work"}


@pytest.mark.asyncio
async def test_read_item():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": None}


@pytest.mark.asyncio
async def test_update_item():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.put("/items/1", json={"name": "foobar", "price": 122.11})
    assert response.status_code == 200
    assert response.json() == {"item_name": "foobar", "item_id": 1}


@pytest.mark.asyncio
async def test_update_item_fail():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.put("/items/1", json={"nameS": "foobar", "price": 122.11})
    assert response.status_code == 422
