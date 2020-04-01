import molotov

@molotov.scenario(60)
async def scenario_one(session):

    async with session.get("http://localhost:5000/") as resp:
        res = await resp.json()
        assert res['result'] == 'OK'
        assert resp.status == 200

@molotov.scenario(40)
async def scenario_two(session):

    resp = await session.post("http://localhost:5000", params={'q': 'devops'})
    redirect_status = resp.history[0].status
    error = "unexpected redirect status: %s" % redirect_status
    assert redirect_status == 302, error